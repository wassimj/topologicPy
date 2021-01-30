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
from topologic import Vertex, Edge, Wire, Face, Shell, Cell, CellComplex, Cluster, Topology, Graph, Dictionary, Attribute, AttributeManager, VertexUtility, EdgeUtility, WireUtility, FaceUtility, ShellUtility, CellUtility, TopologyUtility

import cppyy

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
  topologies = cppyy.gbl.std.list[pointer]()
  if subTopologyClass == Vertex:
    _ = topology.Vertices(topologies)
  elif subTopologyClass == Edge:
    _ = topology.Edges(topologies)
  elif subTopologyClass == Wire:
    _ = topology.Wires(topologies)
  elif subTopologyClass == Face:
    _ = topology.Faces(topologies)
  elif subTopologyClass == Shell:
    _ = topology.Shells(topologies)
  elif subTopologyClass == Cell:
    _ = topology.Cells(topologies)
  elif subTopologyClass == CellComplex:
    _ = topology.CellComplexes(topologies)
 
  for aTopology in topologies:
    fixTopologyClass(aTopology)
  return topologies

def vertexIndex(v, vertices, tolerance):
    index = None
    v._class__ = Vertex
    i = 0
    for aVertex in vertices:
        aVertex.__class__ = Vertex
        d = VertexUtility.Distance(v, aVertex)
        if d <= tolerance:
            index = i
            break
        i = i+1
    return index

def triangulate(faces):
    py_triangles = []
    for aFace in faces:
        wires = cppyy.gbl.std.list[Wire.Ptr]()
        _ = aFace.InternalBoundaries(wires)
        stl_triangles = cppyy.gbl.std.list[Face.Ptr]()
        if wires != None:
            FaceUtility.Triangulate(aFace, 0.0, stl_triangles)
        else:
            stl_triangles.push_back(aFace)
        for aTriangle in stl_triangles:
            py_triangles.append(aTriangle)
    return py_triangles

def meshData(topology):
    type = classByType(topology.GetType())
    if type == Cluster or type == CellComplex or type == Cell or type == Shell:
        topFaces1 = getSubTopologies(topology, Face)
        topFaces = triangulate(topFaces1)
        topEdges = getSubTopologies(topology, Edge)
        topVertices = getSubTopologies(topology, Vertex)
    elif type == Wire:
        topFaces = []
        topEdges = getSubTopologies(topology, Edge)
        topVertices = getSubTopologies(topology, Vertex)
    elif type == Edge:
        topFaces = []
        topEdges = cppyy.gbl.std.list[Edge.Ptr]()
        top.Edges.push_back(topology)
        topVertices = getSubTopologies(topology, Vertex)
    elif type == Vertex:
        topFaces = []
        topEdges = []
        topVertices = cppyy.gbl.std.list[Vertex.Ptr]()
        topVertices.push_back(topology)
    else:
        topFaces = []
        topEdges = []
        topVertices = []
    vertices = []
    for aVertex in topVertices:
        vertices.append(tuple([aVertex.X(), aVertex.Y(), aVertex.Z()]))
    faces = []
    for aFace in topFaces:
        wires = getSubTopologies(aFace, Wire)
        wire = wires.front()
        faceVertices = getSubTopologies(wire, Vertex)
        tempList = []
        for aVertex in faceVertices:
            index = vertexIndex(aVertex, topVertices, 0.0001)
            tempList.append(index)
        faces.append(tuple(tempList))
    edges = []
    for anEdge in topEdges:
        edgeVertices = getSubTopologies(anEdge, Vertex)
        tempList = []
        for aVertex in edgeVertices:
            index = vertexIndex(aVertex, topVertices, 0.0001)
            tempList.append(index)
        edges.append(tuple(tempList))
    return [vertices, edges, faces]

class ObjectTopologic(bpy.types.Operator):
    """Object Topologic Test"""
    bl_idname = "object.topologic"
    bl_label = "Topologic"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        try:
            f = open("/home/wassim/Downloads/Tower.brep", "r")
            brepString = f.read()
            cc = Topology.ByString(brepString)
            md = meshData(cc)
            mesh = bpy.data.meshes.new(name="TopologicTower")
            mesh.from_pydata(md[0], md[1], md[2])
            object_data_add(context, mesh)
            g = Graph.ByTopology(cc, True, False, False, False,False, False, 0.0001)
            gw = g.Topology()
            mesh = bpy.data.meshes.new(name="TopologicDualGraph")
            md = meshData(gw)
            mesh.from_pydata(md[0], md[1], md[2])
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
