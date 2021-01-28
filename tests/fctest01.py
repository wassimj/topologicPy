from topologic import Vertex, Edge, Wire, Face, Cell, CellComplex, Cluster, Topology, Graph, Aperture, TopologyUtility, CellUtility
import cppyy
import Part

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
        py_list.append( Topology.DeepCopy(i.__deref__()) )
        _ = i.__preinc__()
    return py_list

# Convert Tower to CellComplex
tower = App.ActiveDocument.getObject("tower")
tower.ViewObject.Transparency = 75
towerString = tower.Shape.exportBrepToString()
cellComplex = Topology.ByString(towerString)
cellComplex.__class__ = cppyy.gbl.TopologicCore.Topology
apertures = App.ActiveDocument.getObject("apertures")
apertures.ViewObject.Transparency = 20
aperturesString = apertures.Shape.exportBrepToString()
apertures = Topology.ByString(aperturesString)

apertureFaces = cppyy.gbl.std.list[Face.Ptr]()
apertures.Faces(apertureFaces)

apList = convert_to_py_list(apertureFaces)
for anAperture in apList:
    Aperture.ByTopologyContext(anAperture, cellComplex)

#cellComplex = Topology.AddApertures(cellComplex, apertureFaces)
graph = Graph.ByTopology(cellComplex, False, True, False, False, True, False, 0.0001)
graphWire = graph.Topology()

sh=Part.Shape()
sh.importBrepFromString(str(graphWire.String()))
Part.show(sh)
