from topologic import Vertex, Topology, Dictionary, Attribute, AttributeManager, IntAttribute, DoubleAttribute, StringAttribute
import cppyy
from cppyy.gbl.std import string, list

# Create an Integer Value
intVal = IntAttribute(340)

# Create a Double Value
doubleVal = DoubleAttribute(120.567)

# Create a String Value
s = string("Hello World")
stringVal = StringAttribute(s)

# Create a list of values
values = cppyy.gbl.std.list[Attribute.Ptr]()
values.push_back(intVal)
values.push_back(doubleVal)
values.push_back(stringVal)

# Create a list of keys
intKey = string("int")
doubleKey = string("double")
stringKey = string("string")

keys = cppyy.gbl.std.list[string]()
keys.push_back(intKey)
keys.push_back(doubleKey)
keys.push_back(stringKey)

# Create a Dictionary
d = Dictionary.ByKeysValues(keys, values)

# Create a Vertex
v = Vertex.ByCoordinates(0,0,0)

# Assign Dictionary
v.SetDictionary(d)

# Retrieve Dictionary
dict = v.GetDictionary()

# Retrieve Values from Dictionary
newIntValue = dict.ValueAtKey(intKey)
newDoubleValue = dict.ValueAtKey(doubleKey)
newStringValue = dict.ValueAtKey(stringKey)

# Bind Retrieved Int Value and Print it
i = cppyy.bind_object(newIntValue.Value(), 'IntegerStruct')
print(str(i.getInteger)+" <--- Should be 340")

# Bind Retrieved Double Value and Print It
j = cppyy.bind_object(newDoubleValue.Value(), 'DoubleStruct')
print(str(j.getDouble)+" <--- Should be 120.567")

# Bind Retrieved String Value and Print It (How??)
k = cppyy.bind_object(newStringValue.Value(), 'StringStruct')
print(k.getString+" <--- Should be Hello World")

