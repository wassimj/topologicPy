import cppyy
headers = [
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
"Utilities/CellUtility",
"Utilities/Direction",
"Utilities/EdgeUtility",
"Utilities/FaceUtility",
"Utilities/ShellUtility",
"Utilities/TopologyUtility",
"Utilities/TransformationMatrix2D",
"Utilities/Vector",
"Utilities/VertexUtility",
"Utilities/WireUtility.h"
]

for header in headers:
    cppyy.include(header)

cppyy.load_library("topologic")

from cppyy.gbl import About
from cppyy.gbl import CellComplex
from cppyy.gbl import ContextManager
from cppyy.gbl import GlobalCluster
from cppyy.gbl import NurbsSurface
from cppyy.gbl import Topology
from cppyy.gbl import Wire
from cppyy.gbl import Aperture
from cppyy.gbl import CellComplexFactory
from cppyy.gbl import DoubleAttribute
from cppyy.gbl import Graph
from cppyy.gbl import PlanarSurface
from cppyy.gbl import TopologyFactory
from cppyy.gbl import WireFactory
from cppyy.gbl import ApertureFactory
from cppyy.gbl import CellFactory
from cppyy.gbl import Edge
from cppyy.gbl import InstanceGUIDManager
from cppyy.gbl import Shell
from cppyy.gbl import TopologyFactoryManager
from cppyy.gbl import Attribute
from cppyy.gbl import Cluster
from cppyy.gbl import EdgeFactory
from cppyy.gbl import IntAttribute
from cppyy.gbl import ShellFactory
from cppyy.gbl import Utilities
from cppyy.gbl import AttributeManager
from cppyy.gbl import ClusterFactory
from cppyy.gbl import Face
from cppyy.gbl import Line
from cppyy.gbl import StringAttribute
from cppyy.gbl import Utilities
from cppyy.gbl import Bitwise
from cppyy.gbl import ContentManager
from cppyy.gbl import FaceFactory
from cppyy.gbl import ListAttribute
from cppyy.gbl import Surface
from cppyy.gbl import Vertex
from cppyy.gbl import Cell
from cppyy.gbl import Context
from cppyy.gbl import Geometry
from cppyy.gbl import NurbsCurve
from cppyy.gbl import TopologicalQuery
from cppyy.gbl import VertexFactory
from cppyy.gbl import CellUtility
from cppyy.gbl import Direction
from cppyy.gbl import EdgeUtility
from cppyy.gbl import FaceUtility
from cppyy.gbl import ShellUtility
from cppyy.gbl import TopologyUtility
from cppyy.gbl import TransformationMatrix2D
from cppyy.gbl import Vector
from cppyy.gbl import VertexUtility
from cppyy.gbl import WireUtility