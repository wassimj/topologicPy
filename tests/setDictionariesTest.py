from topologic import Vertex, Edge, Wire, Topology, Dictionary, Attribute, AttributeManager, IntAttribute, DoubleAttribute, StringAttribute
import cppyy
from cppyy.gbl.std import string, list

# Create three vertices
v1 = Vertex.ByCoordinates(0,0,0)
v2 = Vertex.ByCoordinates(10,0,0)
v3 = Vertex.ByCoordinates(10,10,0)

# Create two edges in an L-shape
e1 = Edge.ByStartVertexEndVertex(v1, v2)
e2 = Edge.ByStartVertexEndVertex(v2, v3)

# Add the two edges to a list of edges
edges = cppyy.gbl.std.list[Edge.Ptr]()
edges.push_back(e1)
edges.push_back(e2)

# Create a wire from the list of edges
w1 = Wire.ByEdges(edges)

# Create an key called "number"
intKey = string("number")

# Create three integer attributes with values 1, 2, 3
intVal1 = IntAttribute(1)
intVal2 = IntAttribute(2)
intVal3 = IntAttribute(3)

# Create three dictionaries with different values (1, 2, 3)
keys = cppyy.gbl.std.list[str]()
values = cppyy.gbl.std.list[Attribute.Ptr]()
keys.push_back(intKey)
values.push_back(intVal1)
dict1 = Dictionary.ByKeysValues(keys, values)

keys = cppyy.gbl.std.list[str]()
values = cppyy.gbl.std.list[Attribute.Ptr]()
keys.push_back(intKey)
values.push_back(intVal2)
dict2 = Dictionary.ByKeysValues(keys, values)

keys = cppyy.gbl.std.list[str]()
values = cppyy.gbl.std.list[Attribute.Ptr]()
keys.push_back(intKey)
values.push_back(intVal3)
dict3 = Dictionary.ByKeysValues(keys, values)

# Add the three dictionaries to a list of dictionaries
dictionaries = cppyy.gbl.std.list[Dictionary]()
dictionaries.push_back(dict1)
dictionaries.push_back(dict2)
dictionaries.push_back(dict3)

# Create a selectors list and add the vertices to items
selectors = cppyy.gbl.std.list[Vertex.Ptr]()
selectors.push_back(v1)
selectors.push_back(v2)
selectors.push_back(v3)

# Add the list of dictionaries to the Wire and restrict to assigning to Vertices
w1 = w1.SetDictionaries(selectors, dictionaries, Vertex.Type())

# Get the vertices of the wire
vertices = cppyy.gbl.std.list[Vertex.Ptr]()
_ = w1.Vertices(vertices)

# Cycle through the vertices, get the dictionary and print the value at the key
for aVertex in vertices:
  newDict = aVertex.GetDictionary()
  aValue = newDict.ValueAtKey(intKey)
  i = cppyy.bind_object(aValue.Value(), 'IntegerStruct')
  print(i.getInteger)

