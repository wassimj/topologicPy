This projects creates a Topologic python module from the Topologic C++ sources (included in this repo)



### Install on Linux

Any recent distribution should have all the tools needed. The instructions below are for Debian-based distributions, but other distributions should have corresponding packages too.

1. **Install dependencies**

```
sudo apt-get install bzip2 unzip cmake make g++ git libgl-dev libglu-dev libpng-dev libxmu-dev libxi-dev libtbb-dev tcl-dev tk-dev zlib1g-dev libharfbuzz-dev libfreetype-dev libfreeimage-dev libocct-*-dev
```

2. **Install cppyy via pip**: This is needed at runtime by the topologic module:

```
sudo pip3 install cppyy
```
3. **Build Topologic**

```
git clone https://github.com/NonManifoldTopology/Topologic.git
cd Topologic
mkdir build
cd build
cmake ..
make
sudo make install
```
4. **Install the library** (On most debian-based distros, /usr/local/lib is not part of standard library paths. If we are going to use it here (which is the recommended location for self-compiled files), we need to run ldconfig afterwards):

```
sudo cp TopologicCore/libTopologicCore.so /usr/local/lib
sudo ldconfig /usr/local/lib
```

5. **Install the python module**: This will install the python module locally, in your .local/lib/python* user folder, which does not require the use of *sudo*. For system-wide install, you can use `/usr/local/lib` in the command below instead of `~/.local/lib`.

```
git clone http://github.com/wassimj/TopologicPy
cd TopologicPy/cpython
python3 setup.py build
python3 setup.py install --user
```



### Testing

In a Python console, type:

```
import topologic
```

If no error message appears, everything was correctly installed.



### Using the module

There is an [example.py](example.py) test file we have used to test the module. This example shows how you can use the Python/C++ to make calls directly to Topologic:

```
# import the topologic submodules
from topologic import Vertex, Edge, Topology

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

### Rebuilding the Python module

In case you need to rebuild the Python module (make sure you have root privileges eg sudo -i):

1. cd into ./cpython/
```
cd ./cpython/
```
2. Run build
```
python3 setup.py build
```
2. Run install
```
python3 setup.py install
```





