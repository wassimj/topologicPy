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
“Dictionary.h”,
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
NurbsSurface = TopologicCore.NurbsSurface
Topology = TopologicCore.Topology
Wire = TopologicCore.Wire
Aperture = TopologicCore.Aperture
CellComplex = TopologicCore.CellComplex
CellComplexFactory = TopologicCore.CellComplexFactory
DoubleAttribute = TopologicCore.DoubleAttribute
Graph = TopologicCore.Graph
PlanarSurface = TopologicCore.PlanarSurface
TopologyFactory = TopologicCore.TopologyFactory
WireFactory = TopologicCore.WireFactory
ApertureFactory = TopologicCore.ApertureFactory
CellFactory = TopologicCore.CellFactory
Edge = TopologicCore.Edge
InstanceGUIDManager = TopologicCore.InstanceGUIDManager
Shell = TopologicCore.Shell
TopologyFactoryManager = TopologicCore.TopologyFactoryManager
Attribute = TopologicCore.Attribute
Cluster = TopologicCore.Cluster
EdgeFactory = TopologicCore.EdgeFactory
IntAttribute = TopologicCore.IntAttribute
ShellFactory = TopologicCore.ShellFactory
AttributeManager = TopologicCore.AttributeManager
ClusterFactory = TopologicCore.ClusterFactory
Face = TopologicCore.Face
Line = TopologicCore.Line
StringAttribute = TopologicCore.StringAttribute
#Bitwise = TopologicCore.Bitwise
ContentManager = TopologicCore.ContentManager
FaceFactory = TopologicCore.FaceFactory
ListAttribute = TopologicCore.ListAttribute
Surface = TopologicCore.Surface
Vertex = TopologicCore.Vertex
Cell = TopologicCore.Cell
Context = TopologicCore.Context
Geometry = TopologicCore.Geometry
NurbsCurve = TopologicCore.NurbsCurve
TopologicalQuery = TopologicCore.TopologicalQuery
VertexFactory = TopologicCore.VertexFactory
CellUtility = TopologicUtilities.CellUtility
Direction = TopologicUtilities.Direction
EdgeUtility = TopologicUtilities.EdgeUtility
FaceUtility = TopologicUtilities.FaceUtility
ShellUtility = TopologicUtilities.ShellUtility
TopologyUtility = TopologicUtilities.TopologyUtility
TransformationMatrix2D = TopologicUtilities.TransformationMatrix2D
Vector = TopologicUtilities.Vector
VertexUtility = TopologicUtilities.VertexUtility
WireUtility = TopologicUtilities.WireUtility
