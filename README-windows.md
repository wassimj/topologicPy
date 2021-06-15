This projects creates a Topologic python module from the Topologic C++ sources (available at https://github.com/NonManifoldTopology/Topologic.git)

### Install on Windows 10

**If you wish to install only for Blender, please scroll down to the bottom of this page**

The instructions below are for Microsoft Windows 10. In these instructions we assume *Visual Studio Community 2017* *opencascade 7.5.0* and *python3.9.X*. We also assume that your account has Adminstrator priviliges.

1. **Install Topologic and needed dependencies (git, python, cmake, and cppyy)**
Follow the instructions at http://github.com/wassimj/topologic

2. **Install TopologicPy**

```
cd C:/Users/*homefolder*/topologicbim
git clone https://github.com/wassimj/topologicPy.git
cd C:/Users/*homefolder*/topologicbim/topologicPy/cpython
python setup.py build
python setup.py install
```

3. **Test**

Test:
```
cd C:/Users/*homefolder*/topologicbim/topologicPy/
python example.py
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
### How to install for Blender

Blender 2.9.3 uses python 3.9.2. Therefore, it is advisable to create a virtual environment and install cppyy and TopologicPy in that environment. You can then simply point Blender's python to use the files in that virtual envrionment. Here is one way to accomplish that using Anaconda

1. **Download Anaconda** 

Download the individual version of Anaconda from https://www.anaconda.com/products

2. **Open the CMD.exe Prompt**

After install, select the CMD.exe Prompt from the *Home* tab in the *Anaconda Navigator*

3. **Create a virtual environment compatible with the version of python installed in Blender**

* Open Blender
* Choose scripting layout
* At the python console type:
```
bpy.app.version
```
* Make a note of the first two numbers and combine them preceeded with the word 'Blender'. For example if you see (2,93,0) then make a note of **Blender293**. This will be the name of your virtual environment. You have to follow this rule for the scripts to work correctly.
* Make note of the python version being used. We will assume it is python 3.9.2. Go back to the Anaconda CMD.exe Prompt and type the following:

```
conda create --name Blender293 python=3.9.2
conda activate Blender
```

4. **Install cppyy**

Stay in the Anaconda CMD.exe Prompt and type the following:

```
pip install cppyy --upgrade
```

5. **Re-install TopologicPy**

Stay in the Anaconda CMD.exe Prompt and type the following:

```
cd C:/Users/*homefolder*/topologicbim/topologicPy/cpython
python setup.py build
python setup.py install
```
6. **Test in Blender**

At the scripting command prompt in Blender, type the following script.

**WARNING: Replace the topologic egg name with the correct and latest installed version!**

Make note of the anaconda virtual environments folder path. This may be something like:

```
C:\\ProgramData\\anaconda3\\envs\\Blender293\\lib\\site-packages
```
and the path to the topologic egg may then be
```
C:\\ProgramData\\anaconda3\\envs\\Blender293\\lib\\site-packages\\topologic-0.5-py3.9.egg
```
**WARNING: Go into that folder and delete any previous versions of the topologic egg.**
```
import sys
import os, re
from os.path import expanduser
from sys import platform
import bpy
home = expanduser("~")
blenderVersion =  "Blender"+str(bpy.app.version[0])+str(bpy.app.version[1])
if platform == 'win32':
  if os.path.exists('C:\\ProgramData\\anaconda3\\envs'):
    conda = 'C:\\ProgramData\\anaconda3\\envs'
  elif os.path.exists(home+'\\anaconda3\\envs'):
    conda = home+'\\anaconda3\\envs'
  else:
    raise Exception("Error: Could not find: "+home+'\\anaconda3\\envs nor '+'C:\\ProgramData\\anaconda3\\envs')
  sitePackages = '\\lib\\site-packages'
  blenderName = '\\'+[name for name in os.listdir(conda) if name.startswith(blenderVersion)][0]
  topologicEggName = '\\'+[name for name in os.listdir(conda+blenderName+sitePackages) if name.startswith('topologic')][0]
  if os.path.exists(conda+blenderName+sitePackages):
    sys.path.append(conda+blenderName+sitePackages)
  else:
    raise Exception("Error: Could not find "+conda+blenderName+sitePackages)
  if os.path.exists(conda+blenderName+sitePackages+topologicEggName):
    sys.path.append(conda+blenderName+sitePackages+topologicEggName)
  else:
    raise Exception("Error: Could not find "+conda+blenderName+sitePackages+topologicEggName)

import cppyy
from topologic import Vertex, Edge, Wire, Face, Shell, Cell, CellComplex, Cluster, Topology, Graph, Dictionary

v1 = Vertex.ByCoordinates(0,0,0)
v2 = Vertex.ByCoordinates(10,10,10)
e1 = Edge.ByStartVertexEndVertex(v1, v2)
c1 = e1.Centroid()
print([c1.X(), c1.Y(), c1.Z()])
```

If you see the following, then all is fine:

```
[5.0, 5.0, 5.0]
```
