import cppyy
import os
headers = [
"About.h",
"Aperture.h",
"ApertureFactory.h",
"Attribute.h",
"AttributeManager.h",
"Bitwise.h",
"Cell.h",
"CellComplex.h",
"CellComplexFactory.h",
"CellFactory.h",
"Cluster.h",
"ClusterFactory.h",
"ContentManager.h",
"Context.h",
"ContextManager.h",
"Dictionary.h",
"DoubleAttribute.h",
"Edge.h",
"EdgeFactory.h",
"Face.h",
"FaceFactory.h",
"Geometry.h",
"GlobalCluster.h",
"Graph.h",
"InstanceGUIDManager.h",
"IntAttribute.h",
"Line.h",
"ListAttribute.h",
"NurbsCurve.h",
"NurbsSurface.h",
"PlanarSurface.h",
"Shell.h",
"ShellFactory.h",
"StringAttribute.h",
"Surface.h",
"TopologicalQuery.h",
"Topology.h",
"TopologyFactory.h",
"TopologyFactoryManager.h",
"Utilities.h",
"Utilities.h",
"Utilities/CellUtility.h",
"Utilities/Direction.h",
"Utilities/EdgeUtility.h",
"Utilities/FaceUtility.h",
"Utilities/ShellUtility.h",
"Utilities/TopologyUtility.h",
"Utilities/TransformationMatrix2D.h",
"Utilities/Vector.h",
"Utilities/VertexUtility.h",
"Utilities/WireUtility.h",
"Vertex.h",
"VertexFactory.h",
"Wire.h",
"WireFactory.h"
]

if (os.path.isfile("/usr/local/include/opencascade/TopoDS_Shape.hxx")):
    cppyy.add_include_path("/usr/local/include/opencascade")
elif (os.path.isfile("/usr/include/opencascade/TopoDS_Shape.hxx")):
    cppyy.add_include_path("/usr/include/opencascade")
base_dir = os.path.dirname(os.path.realpath(__file__))

if (os.path.isfile("/usr/local/include/TopologicCore/Topology.h")):
    topologic_inc = "/usr/local/include/TopologicCore"
elif (os.path.isfile("/usr/include/TopologicCore/Topology.h")):
    topologic_inc = "/usr/include/TopologicCore"
elif (os.path.isfile(base_dir + "/include/Topology.h")):
    topologic_inc = base_dir + "/include"

cppyy.add_include_path(topologic_inc)

for header in headers:
    cppyy.include(topologic_inc + "/" + header )

cppyy.load_library("TopologicCore")

from cppyy.gbl import TopologicCore
from cppyy.gbl import TopologicUtilities
Aperture = TopologicCore.Aperture
ApertureFactory = TopologicCore.ApertureFactory
Attribute = TopologicCore.Attribute
AttributeManager = TopologicCore.AttributeManager
#Bitwise = TopologicCore.Bitwise
Cell = TopologicCore.Cell
CellComplex = TopologicCore.CellComplex
CellComplexFactory = TopologicCore.CellComplexFactory
CellFactory = TopologicCore.CellFactory
CellUtility = TopologicUtilities.CellUtility
Cluster = TopologicCore.Cluster
ClusterFactory = TopologicCore.ClusterFactory
ContentManager = TopologicCore.ContentManager
Context = TopologicCore.Context
Dictionary = TopologicCore.Dictionary
Direction = TopologicUtilities.Direction
DoubleAttribute = TopologicCore.DoubleAttribute
Edge = TopologicCore.Edge
EdgeFactory = TopologicCore.EdgeFactory
EdgeUtility = TopologicUtilities.EdgeUtility
Face = TopologicCore.Face
FaceFactory = TopologicCore.FaceFactory
FaceUtility = TopologicUtilities.FaceUtility
Geometry = TopologicCore.Geometry
Graph = TopologicCore.Graph
InstanceGUIDManager = TopologicCore.InstanceGUIDManager
IntAttribute = TopologicCore.IntAttribute
Line = TopologicCore.Line
ListAttribute = TopologicCore.ListAttribute
NurbsCurve = TopologicCore.NurbsCurve
NurbsSurface = TopologicCore.NurbsSurface
PlanarSurface = TopologicCore.PlanarSurface
Shell = TopologicCore.Shell
ShellFactory = TopologicCore.ShellFactory
ShellUtility = TopologicUtilities.ShellUtility
StringAttribute = TopologicCore.StringAttribute
Surface = TopologicCore.Surface
TopologicalQuery = TopologicCore.TopologicalQuery
Topology = TopologicCore.Topology
TopologyFactory = TopologicCore.TopologyFactory
TopologyFactoryManager = TopologicCore.TopologyFactoryManager
TopologyUtility = TopologicUtilities.TopologyUtility
TransformationMatrix2D = TopologicUtilities.TransformationMatrix2D
Vector = TopologicUtilities.Vector
Vertex = TopologicCore.Vertex
VertexFactory = TopologicCore.VertexFactory
VertexUtility = TopologicUtilities.VertexUtility
Wire = TopologicCore.Wire
WireFactory = TopologicCore.WireFactory
WireUtility = TopologicUtilities.WireUtility
