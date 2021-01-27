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

def getVertices(topology):
  vertices = create_stl_list(Vertex.Ptr)
  topology.Vertices(vertices)
  vertices = convert_to_py_list(vertices)
  return vertices

def getEdges(topology):
  edges = create_stl_list(Edge.Ptr)
  topology.Edges(edges)
  edges = convert_to_py_list(edges)
  return edges

def getWires(topology):
  wires = create_stl_list(Wire.Ptr)
  topology.Wires(wires)
  wires = convert_to_py_list(wires)
  return wires

def getFaces(topology):
  faces = create_stl_list(Face.Ptr)
  topology.Faces(faces)
  faces = convert_to_py_list(faces)
  return faces

def getCells(topology):
  cells = create_stl_list(Cell.Ptr)
  topology.Cells(cells)
  cells = convert_to_py_list(cells)
  return cells

def getCellComplexes(topology):
  cellComplexes = create_stl_list(CellComplex.Ptr)
  topology.CellComplexes(cellComplexes)
  cellComplexes = convert_to_py_list(cellComplexes)
  return cellComplexes

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

# driver code
v1 = Vertex.ByCoordinates(0,0,0)
v2 = Vertex.ByCoordinates(10,10,10)
e1 = Edge.ByStartVertexEndVertex(v1, v2)
e2 = TopologyUtility.Translate(e1, 5, 5, 5)
e2 = fixTopologyClass(e2)
verts = getVertices(e2)
for aVert in verts:
  print([aVert.X(), aVert.Y(), aVert.Z()])
