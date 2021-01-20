This projects creates a Topologic python module from the Topologic C++ sources (available at https://github.com/NonManifoldTopology/Topologic.git)

### Install on Linux

Any recent distribution should have all the tools needed. The instructions below are for Debian-based distributions, but other distributions should have corresponding packages too. In these instructions we assume *python3.8* and everythng is installed in */usr/local/lib*. Please change according to your python version.

1. **Create a working folder**: We will assume that you will install everything in ~/topologicbim
```
mkdir ~/topologicbim
cd ~/topologicbim
```

2. **Install dependencies**
```
sudo apt-get install bzip2 unzip cmake make g++ git libgl-dev libglu-dev libpng-dev libxmu-dev libxi-dev libtbb-dev tcl-dev tk-dev zlib1g-dev libharfbuzz-dev libfreetype-dev libfreeimage-dev libocct-*-dev
```

3. **Install Topologic**
```
git clone https://github.com/NonManifoldTopology/Topologic.git
cd Topologic
mkdir build
cd build
cmake ..
make
sudo make install
```
At the end of this process, libTopologicCore.so should exist in /usr/local/lib

4. **Install cppyy via pip**: This is needed at runtime by the topologic module:
```
sudo apt install python3-pip
sudo pip3 install cppyy
sudo ldconfig /usr/local/lib
```

5. **Install TopologicPy**
```
cd ~/topologicbim
git clone http://github.com/wassimj/TopologicPy
cd TopologicPy/cpython
(Skip this) sudo cp libTopologicCore.so /usr/local/lib
python3 setup.py build
sudo python3 setup.py install
```

6. **Set the CPPYY_API_PATH**: edit the */etc/environment* file and add the following line
```
sudo gedit /etc/environment
```
Type the following into the file that opens
```
CPPYY_API_PATH="/usr/local/include/python3.8/CPyCppyy"
```
Save the file. Logout and log back in to continue

7. **Test**

Test in a Python 3 console:
```
python3
import topologic
import cppyy
```
If no error message appears, everything was correctly installed.

8. **Install for Blender 2.91 on Ubuntu 20.04**
Remove any previous versions of Blender
```
sudo apt install blender
```
Make sure that your blender installation is using the system's python3.8

### Using the module

There is an [example.py](~/topologicbim/TopologicPy/example.py) test file we have used to test the module. This example shows how you can use the Python/C++ to make calls directly to Topologic:

```
# import the topologic submodules
from topologic import Vertex, Edge, Wire, Face, Shell, Cell, CellComplex, Cluster, Graph, Topology

# create a vertex
v1 = Vertex.ByCoordinates(0,0,0) 

# create another vertex
v2 = Vertex.ByCoordinates(20,20,20)

# create an edge from the two vertices
e1 = Edge.ByStartVertexEndVertex(v1, v2)

# retrieve the coordinate from the start vertex of e1
sv = e1.StartVertex()
print("   "+str([sv.X(), sv.Y(), sv.Z()]))

# retrieve the coordinate from the end vertex of e1
ev = e1.EndVertex()
print("   "+str([ev.X(), ev.Y(), ev.Z()]))

# retrieve the coordinates of the centroid of e1
cv = Topology.Centroid(e1)
print("   "+str([cv.X(), cv.Y(), cv.Z()]))
```
You should see the following as an output:
```
START
1. Create Vertex (v1) at 0 0 0
2. Create Vertex (v2) at 20 20 20
3. Create an Edge (e1) connecting v1 to v2
4. Print the coordinates of the start vertext of e1:
   [0.0, 0.0, 0.0]
5. Print the coordinates of the end vertext of e1:
   [20.0, 20.0, 20.0]
5. Print the coordinates of the centroid of e1:
   [10.0, 10.0, 10.0]
DONE
```

### Troubleshooting

In case your distribution doesn't provide freetype:

```
cd /usr/src/
wget https://netactuate.dl.sourceforge.net/project/freetype/freetype2/2.9.1/freetype-2.9.1.tar.gz
tar xvf freetype-2.9.1.tar.gz
cd freetype-2.9.1
./configure && make && make install
```

In case your distribution doesn't provide freeimage:

```
cd /usr/src/
wget https://managedway.dl.sourceforge.net/project/freeimage/Source%20Distribution/3.18.0/FreeImage3180.zip
unzip FreeImage3180.zip
cd FreeImage && \
	make && \
	make install
```

In case your distribution doesn't provide opencascade (occt):

```
cd /usr/src/
wget https://github.com/tpaviot/oce/releases/download/official-upstream-packages/opencascade-7.4.0.tgz
tar xvf opencascade-7.4.0.tgz
cd opencascade-7.4.0
mkdir build && \
	cd build && \
	cmake .. && \
	make && \
	make install
```






