from cffi import FFI
ffi = FFI()
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
header_string = ""
for header in headers:
    header_string += "#include \"./include/{}\"\r\n".format( header, )
print( header_string )

ffibuilder = FFI()
ffibuilder.set_source('_libTopologicCore',
        header_string,
  include_dirs = ['./include'],
  libraries = ['TopologicCore'],
  library_dirs = ['./']
)

ffibuilder.compile()
