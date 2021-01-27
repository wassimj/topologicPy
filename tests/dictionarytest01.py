from topologic import Vertex, Topology, Dictionary, Attribute, AttributeManager, IntAttribute, DoubleAttribute, StringAttribute
import cppyy
from cppyy.gbl.std import string, list


def create_stl_list( cppyy_data_type ):
    values = cppyy.gbl.std.list[cppyy_data_type]()
    return values


def convert_to_stl_list( py_list, cppyy_data_type ):
    values = create_stl_list( cppyy_data_type )
    for i in py_list:
        values.push_back( i )
    return values

def convert_to_py_list( stl_list ):
    py_list = []
    i  =  stl_list.begin()
    while (i != stl_list.end()):
       py_list.append( i.__deref__() )
       _ = i.__preinc__()

    return py_list


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

# Create an Integer Structure
cppyy.cppdef("""
   struct IntStruct { int getInt; };
   void* create_intstruct() { return new IntStruct{42}; }
   """)

# Bind Retrieved Int Value and Print it
i = cppyy.bind_object(newIntValue.Value(), 'IntStruct')
print(str(i.getInt)+" <--- Should be 340")

# Create a Double Structure
cppyy.cppdef("""
   struct DoubleStruct { double getDouble; };
   void* create_doublestruct() { return new DoubleStruct{42.42}; }
   """)
# Bind Retrieved Double Value and Print It
j = cppyy.bind_object(newDoubleValue.Value(), 'DoubleStruct')
print(str(j.getDouble)+" <--- Should be 120.567")

# Create a String Structure (How??)
cppyy.cppdef("""
   struct StringStruct { char* getString;};
   void* create_stringstruct() { return new StringStruct{"Hello World!"}; }
   """)
# Bind Retrieved String Value and Print It (How??)
k = cppyy.bind_object(newStringValue.Value(), 'StringStruct')
print(k.getString+" <--- Should be Hello World")

