from topologic import Vertex, Edge, Wire, Face, Shell, Cell, CellComplex, Cluster, Topology
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

# Create 3 Vertices
v1 = Vertex.ByCoordinates(0,0,0)
v2 = Vertex.ByCoordinates(10,0,0)
v3 = Vertex.ByCoordinates(10,10,0)

# Connect the vertices by two Edges
e1 = Edge.ByStartVertexEndVertex(v1, v2)
e2 = Edge.ByStartVertexEndVertex(v2, v3)

# Create a Wire from the two connected Edges
edges = cppyy.gbl.std.list[Edge.Ptr]()
edges.push_back(e1)
edges.push_back(e2)
w1 = Wire.ByEdges(edges)

# Compute the Centroid (Vertex) of the Wire
c1 = w1.Centroid()

# Add the Centroid to the Contents of the Wire
contents = cppyy.gbl.std.list[Topology.Ptr]()
contents.push_back(c1)
w1 = w1.AddContents(contents, Wire.Type())

# Retrieve the Contents of the Wire
wireContents = cppyy.gbl.std.list[Topology.Ptr]()
_ = Topology.Contents(w1, wireContents)

# Print the Contents and if they area Vertex, print their coordinates
for aContent in wireContents:
  aContent = fixTopologyClass(aContent)
  if aContent.GetType() == 1:
    print([aContent.X(), aContent.Y(), aContent.Z()])
