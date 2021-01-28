from topologic import Vertex, Edge, Wire, Face, Cell, CellComplex, Cluster, Topology, Graph, TopologyUtility, CellUtility
import cppyy
import Part

# Convert Tower to CellComplex
tower = App.ActiveDocument.getObject("tower")
towerString = tower.Shape.exportBrepToString()
cellComplex = Topology.ByString(towerString)
cellComplex.__class__ = cppyy.gbl.TopologicCore.Topology
apertures = App.ActiveDocument.getObject("apertures")
aperturesString = apertures.Shape.exportBrepToString()
apertures = Topology.ByString(aperturesString)

apertureFaces = cppyy.gbl.std.list[Face.Ptr]()
apertures.Faces(apertureFaces)

Aperture.ByTopologyContext(anAperture, cellComplex)

#cellComplex = Topology.AddApertures(cellComplex, apertureFaces)
graph = Graph.ByTopology(cellComplex, False, True, False, False, True, False, 0.0001)
graphWire = graph.Topology()

sh=Part.Shape()
sh.importBrepFromString(str(graphWire.String()))
Part.show(sh)