import cppyy
import os
headers = [
"Utilities.h",
"About.h",
"CellComplex.h",
"ContextManager.h",
"GlobalCluster.h",
"NurbsSurface.h",
"Topology.h",
"Wire.h",
"Aperture.h",
"CellComplexFactory.h",
"DoubleAttribute.h",
"Graph.h",
"PlanarSurface.h",
"TopologyFactory.h",
"WireFactory.h",
"ApertureFactory.h",
"CellFactory.h",
"Edge.h",
"InstanceGUIDManager.h",
"Shell.h",
"TopologyFactoryManager.h",
"Attribute.h",
"Cluster.h",
"EdgeFactory.h",
"IntAttribute.h",
"ShellFactory.h",
"AttributeManager.h",
"ClusterFactory.h",
"Face.h",
"Line.h",
"StringAttribute.h",
"Utilities.h",
"Bitwise.h",
"ContentManager.h",
"FaceFactory.h",
"ListAttribute.h",
"Surface.h",
"Vertex.h",
"Cell.h",
"Context.h",
"Geometry.h",
"NurbsCurve.h",
"TopologicalQuery.h",
"VertexFactory.h",
"Utilities/CellUtility.h",
"Utilities/Direction.h",
"Utilities/EdgeUtility.h",
"Utilities/FaceUtility.h",
"Utilities/ShellUtility.h",
"Utilities/TopologyUtility.h",
"Utilities/TransformationMatrix2D.h",
"Utilities/Vector.h",
"Utilities/VertexUtility.h",
"Utilities/WireUtility.h"
]

cppyy.add_include_path("/usr/local/include/opencascade")
base_dir = os.path.dirname(os.path.realpath(__file__))
cppyy.add_include_path(base_dir + "/include")
for header in headers:
    cppyy.include( base_dir + "/include/" + header )


#cppyy.load_library("libTopologicCore.so")
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
