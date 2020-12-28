from topologic import Vertex, Edge

v1 = Vertex.ByCoordinates(0,0,0)
v2 = Vertex.ByCoordinates(20,20,20)
l1 = Edge.ByStartVertexEndVertex(v1, v2)


v1 = Vertex.ByCoordinates(0,0,0)
v2 = Vertex.ByCoordinates(20,20,20)
l1 = Edge.ByStartVertexEndVertex(v1, v2)

sv = l1.StartVertex()
ev = l1.EndVertex()
# Assign your output to the OUT variable.
OUT = [sv.X(), sv.Y(), sv.Z(), ev.X(), ev.Y(), ev.Z()]
print("Module output is:")
print(OUT)
