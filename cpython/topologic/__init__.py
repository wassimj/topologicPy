'''
// This file is part of Topologic software library.
// Copyright(C) 2019, Cardiff University and University College London
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU Affero General Public License for more details.
//
// You should have received a copy of the GNU Affero General Public License
// along with this program. If not, see <https://www.gnu.org/licenses/>.
'''
import cppyy
import os
import platform
import sys

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

def pythonize_topologic_printing(klass, name):
    if 'GetTypeAsString' in klass.__dict__:
        klass.__str__ = klass.__repr__ = lambda self: str("<Topologic "+self.GetTypeAsString()+">")
    elif "Dictionary" in klass.__repr__():
        klass.__str__ = klass.__repr__ = lambda self: str("<Topologic Dictionary>")

cppyy.py.add_pythonization(pythonize_topologic_printing, 'TopologicCore')

system = platform.system()
if system != 'Windows':
    if (os.path.isdir("/usr/local/include/opencascade")):
        cppyy.add_include_path("/usr/local/include/opencascade")
    elif (os.path.isdir("/usr/include/opencascade")):
        cppyy.add_include_path("/usr/include/opencascade")
    if (os.path.isdir("/usr/local/include/TopologicCore")):
        topologic_inc = "/usr/local/include/TopologicCore"
    elif (os.path.isdir("/usr/include/TopologicCore")):
        topologic_inc = "/usr/include/TopologicCore"
    if (os.path.isdir("/usr/local/lib")):
        cppyy.add_library_path("/usr/local/lib")
else:
    win_prefix = "E:/Documents/Projects/TopologicFinal/topologic"
    topologic_inc = "{}/TopologicCore/include".format( win_prefix )
    opencascade_prefix = "C:/OpenCASCADE-7.4.0-vc14-64"
    cppyy.add_include_path("{}/opencascade-7.4.0/inc".format(opencascade_prefix))
    cppyy.add_library_path("{}/output/x64/Release".format(win_prefix))
    cppyy.add_library_path("{}/opencascade-7.4.0/win64/vc14/bin".format(opencascade_prefix))

cppyy.add_include_path(topologic_inc)

cppyy.load_library("TopologicCore")

for header in headers:
    cppyy.include(topologic_inc + "/" + header )

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

# Define structs to retrieve int, double, and string values
# Create an Integer Structure
cppyy.cppdef("""
   struct IntegerStruct { int getInteger; };
   void* create_intstruct() { return new IntegerStruct{42}; }
   """)
# Create a Double Structure
cppyy.cppdef("""
   struct DoubleStruct { double getDouble; };
   void* create_doublestruct() { return new DoubleStruct{42.42}; }
   """)
# Create a String Structure
cppyy.cppdef("""
   struct StringStruct { std::string getString;};
   void* create_stringstruct() { return new StringStruct{"Hello World!"}; }
   """)
'''
cppyy.gbl.TopologicCore.Aperture.Ptr = cppyy.gbl.TopologicCore.Aperture.__class__.Ptr
cppyy.gbl.TopologicCore.Cell.Ptr = cppyy.gbl.TopologicCore.Cell.__class__.Ptr
cppyy.gbl.TopologicCore.CellComplex.Ptr = cppyy.gbl.TopologicCore.CellComplex.__class__.Ptr
cppyy.gbl.TopologicCore.Cluster.Ptr = cppyy.gbl.TopologicCore.Cluster.__class__.Ptr
cppyy.gbl.TopologicCore.Edge.Ptr = cppyy.gbl.TopologicCore.Edge.__class__.Ptr
cppyy.gbl.TopologicCore.Face.Ptr = cppyy.gbl.TopologicCore.Face.__class__.Ptr
cppyy.gbl.TopologicCore.Graph.Ptr = cppyy.gbl.TopologicCore.Graph.__class__.Ptr
cppyy.gbl.TopologicCore.Shell.Ptr = cppyy.gbl.TopologicCore.Shell.__class__.Ptr
cppyy.gbl.TopologicCore.Vertex.Ptr = cppyy.gbl.TopologicCore.Vertex.__class__.Ptr
cppyy.gbl.TopologicCore.Wire.Ptr = cppyy.gbl.TopologicCore.Wire.__class__.Ptr
'''
