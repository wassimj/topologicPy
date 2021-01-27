bl_info = {
    "name": "Topologic test",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
import bmesh
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector
import math

import sys
sys.path.append('/usr/local/lib/python3.8/dist-packages')
from topologic import Vertex, Edge, Wire, Face, Shell, Cell, CellComplex, Cluster, Topology, Graph, Dictionary, Attribute, AttributeManager, VertexUtility, EdgeUtility, WireUtility, ShellUtility, CellUtility, TopologyUtility

import cppyy

def create_stl_list(cppyy_data_type):
  values = cppyy.gbl.std.list[cppyy_data_type]()
  return values

def convert_to_stl_list(py_list, cppyy_data_type):
  values = create_stl_list( cppyy_data_type )
  for i in py_list:
    values.push_back( i )
  return values

def convert_to_py_list(stl_list):
  py_list = []
  i  =  stl_list.begin()
  while (i != stl_list.end()):
    py_list.append( i.__deref__() )
    _ = i.__preinc__()
  return py_list

def classByType(argument):
  switcher = {
    1: Vertex,
    2: Edge,
    4: Wire,
    8: Face,
    16: Shell,
    32: Cell,
    64: CellComplex,
    128: Cluster }
  return switcher.get(argument, Topology)

def fixTopologyClass(topology):
  topology.__class__ = classByType(topology.GetType())
  return topology

def getSubTopologies(topology, subTopologyClass):
  pointer = subTopologyClass.Ptr
  values = cppyy.gbl.std.list[pointer]()
  if subTopologyClass == Vertex:
    _ = topology.Vertices(values)
  elif subTopologyClass == Edge:
    _ = topology.Edges(values)
  elif subTopologyClass == Wire:
    _ = topology.Wires(values)
  elif subTopologyClass == Face:
    _ = topology.Faces(values)
  elif subTopologyClass == Shell:
    _ = topology.Shells(values)
  elif subTopologyClass == Cell:
    _ = topology.Cells(values)
  elif subTopologyClass == CellComplex:
    _ = topology.CellComplexes(values)
 
  py_list = []
  i  =  values.begin()
  while (i != values.end()):
    py_list.append(fixTopologyClass(Topology.DeepCopy(i.__deref__())))
    _ = i.__preinc__()
  return py_list

def vertexIndex(v, vertices, tolerance):
    index = None
    v._class__ = Vertex
    for i in range(len(vertices)):
        vertices[i].__class__ = Vertex
        d = VertexUtility.Distance(v, vertices[i])
        if d <= tolerance:
            index = i
            break
    return index

def meshData(topology):
    type = classByType(topology.GetType())
    if type == Cluster or type == CellComplex or type == Cell or type == Shell:
        topFaces = getSubTopologies(topology, Face)
        topVertices = getSubTopologies(topology, Vertex)
    else:
        topFaces = []
        topVertices = []
    vertices = []
    for aVertex in topVertices:
        vertices.append(tuple([aVertex.X(), aVertex.Y(), aVertex.Z()]))
    faces = []
    for aFace in topFaces:
        wires = getSubTopologies(aFace, Wire)
        wire = wires[0]
        faceVertices = getSubTopologies(wire, Vertex)
        tempList = []
        for aVertex in faceVertices:
            index = vertexIndex(aVertex, topVertices, 0.0001)
            tempList.append(index)
        faces.append(tuple(tempList))
    return [vertices, faces]

def edgesByVertices(vertices):
    edges = []
    edges = cppyy.gbl.std.list[Edge.Ptr]()
    for i in range(len(vertices)-1):
        v1 = vertices[i]
        v2 = vertices[i+1]
        e1 = Edge.ByStartVertexEndVertex(v1, v2)
        #edges.append(e1)
        edges.push_back(e1)
    # connect the last vertex to the first one
    v1 = vertices[len(vertices)-1]
    v2 = vertices[0]
    e1 = Edge.ByStartVertexEndVertex(v1, v2)
    edges.push_back(e1)
    return edges

class ObjectTopologic(bpy.types.Operator):
    """Object Topologic Test"""
    bl_idname = "object.topologic"
    bl_label = "Topologic"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for object in context.selected_objects:

            bpy.ops.object.transform_apply(location = True, rotation = True, scale = True)
            depsgraph = bpy.context.evaluated_depsgraph_get()
            object = object.evaluated_get(depsgraph)
            # Get a BMesh representation
            bm = bmesh.new()   # create an empty BMesh
            bm.from_mesh(object.data)   # fill it in from a Mesh
            bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.001)
            bm.verts.ensure_lookup_table()

            vertices = []

            for v in bm.verts:
                coor = v.co[:]
                vertex = Vertex.ByCoordinates(coor[0], coor[1], coor[2])
                vertices.append(vertex)

            faces = cppyy.gbl.std.list[Face.Ptr]()

            for f in bm.faces:
                vertices_face = []
                for v in f.verts:
                    vertex = vertices[v.index]
                    vertices_face.append(vertex)
                edges = edgesByVertices(vertices_face)
                face = Face.ByEdges(edges)
                faces.push_back(face)

            cc = CellComplex.ByFaces(faces, 0.0001)
            cc1 = TopologyUtility.Translate(cc, 5, 0, 0)
            cc2 = TopologyUtility.Translate(cc1, 0.75, 0.75, 0.75)
            cc3 = Topology.Merge(cc1, cc2)

            cells = getSubTopologies(cc3, Cell)   #Cell is the imported class from topologic
            print(str(len(cells))+" cells")
            for i in range(len(cells)):
                print(str(i+1)+". "+cells[i].GetTypeAsString())
                cFaces = getSubTopologies(cells[i], Face)
                print("  "+str(len(cFaces))+" faces")
                for j in range(len(cFaces)):
                    print("   "+str(j+1)+". "+cFaces[j].GetTypeAsString())
                    fVertices = getSubTopologies(cFaces[j], Vertex)
                    print("    "+str(len(fVertices))+" vertices")
                    for k in range(len(fVertices)):
                        print("     "+str(k+1)+". "+fVertices[k].GetTypeAsString())

            md = meshData(cc3)
            print(md)
            try:
                mesh = bpy.data.meshes.new(name="TopologicMesh")
                mesh.from_pydata(md[0], [], md[1])
                # useful for development when the mesh may be invalid.
                #mesh.validate(verbose=True)
                object_data_add(context, mesh)
                print("success")
            except:
                print("error")
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(ObjectTopologic.bl_idname)

def register():
    bpy.utils.register_class(ObjectTopologic)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(ObjectTopologic)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()

