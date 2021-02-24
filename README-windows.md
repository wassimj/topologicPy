This projects creates a Topologic python module from the Topologic C++ sources (available at https://github.com/NonManifoldTopology/Topologic.git)

### Install on Windows 10

The instructions below are for Microsoft Windows 10. In these instructions we assume *Visual Studio Community 2017* *opencascade 0.7.4* and *python3.8.8*. We also assume that your account has Adminstrator priviliges.

**WARNING:** Due to a bug in cppyy this installation will not work if your user home folder has a space in its name. You will need to fix that before you install this software. There are instructions on-line on how to do that without creating a new account, but you need to be careful with things like OneDrive, Outlook and other installed software that stores the user folder name. **Do this at your own risk**

1. **Create a topologicbim working folder**: We will assume that your home folder is called *homefolder* and you will install everything in *homefolder*/topologicbim

2. **Install Visual Studio Community 2017**

Download from https://visualstudio.microsoft.com/vs/older-downloads/

3. **Install Git**

Download from https://git-scm.com/download/win

4. **Install Python 3.8.8**

**WARNING:** Do not install from the Microsoft Store
Download from https://www.python.org/downloads/windows/

**WARNING:** When installing python make sure you tick the box on the installation screen to add python to the path. For example see the image below:

![python installation window](https://blog.uvm.edu/tbplante/files/2020/07/path-install.png)

5. **Install cmake 3.19.5**

Download from https://cmake.org/download/

Scroll down and look for the latest release and choose the *Windows win64-x64 Installer* 

6. **Install cppyy via pip**: This is needed at runtime by the topologic module:

Go to the Start Menu in the lower left corner Search for the Visual Studio 2017 Folder and expand it Choose *x64 Native Tools Command Prompt.* In the window that appears type:
```
pip install cppyy
```

7. **Install Opencascade 0.7.4.0**

Download from https://old.opencascade.com/content/previous-releases

Choose  *Windows installer VC++ 2017 64 bit: opencascade-7.4.0-vc14-64.exe (237 061 168 bytes)*

This will automatically install opencascade in:
```
C:/OpenCASCADE-7.4.0-vc14-64
```
Do **NOT** change the location and name of this folder.

8. **Fix a file in the Opencascade installation**

Unfortunately, there is a small change needed in the opencascade files for TopologicPy to work. The file that needs to be edited in opencascade is:
```
C:\OpenCASCADE-7.4.0-vc14-64\opencascade-7.4.0\inc\Standard_Macro.hxx.
```
You need to change line 67 from 
```
#if defined(__has_cpp_attribute)
```
to 
```
 #if defined(__has_cpp_attribute) && !defined(__CLING__)
```

9. **Install Topologic**

Go to the Start Menu in the lower left corner
Search for the Visual Studio 2017 Folder and expand it
Choose *x64 Native Tools Command Prompt*
In the window that appears type:
```
cd C:/Users/*homefolder*/topologicbim
git clone https://github.com/NonManifoldTopology/Topologic.git
cd Topologic
WindowsBuild.bat
```
10. **Set the Environment Variable**

A window will open with a folder that has all the DLL files. Copy the path of this folder and add it to the **PATH** environment variable:
```
. In Search, search for and then select: System (Control Panel)
. Click the Advanced system settings link.
. Click Environment Variables. ...
. In the Edit System Variable (or New System Variable) window, add the folder to the PATH environment variable.
```
11. **Download TopologicPy**

stay in the same window
```
cd C:/Users/*homefolder*/topologicbim
git clone https://github.com/wassimj/topologicPy.git
cd topologicPy/cpython
python setup.py build
python setup.py install
```
12. **Fix the windir_prefix**

Edit the ```C:/Users/*homefolder*/topologicbim/topologicPy/cpython/topologic/__init.py``` file and look for the *windir_prefix*
Set it to the location of the Topologic installation (e.g. windir_prefix = "C:/Users/*homefolder*/topologicbim/Topologic")

13. **Install TopologicPy**

```
cd C:/Users/*homefolder*/topologicbim/topologicPy/cpython
python setup.py build
python setup.py install
```

14. **Test**

Test in a Python 3 console:
```
python
import topologic
import cppyy
```
If no error message appears, everything was correctly installed.

### Using the module

There is an [example.py](C:/Users/*homefolder*/topologicbim/topologicPy/example.py) test file we have used to test the module. This example shows how you can use the Python/C++ to make calls directly to Topologic:

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



