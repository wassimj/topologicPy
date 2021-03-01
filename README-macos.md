This projects creates a Topologic python module from the Topologic C++ sources (available at https://github.com/NonManifoldTopology/Topologic.git)

### Install on MacOS

These instructions have been tested to work on MacOS 10.15.7 Catalina. *Please make sure you have updated your OS before attempting to install topologicPy*. In these instructions we assume *python3.8* and everythng is installed in */usr/local/lib*. Please change according to your python version.

1. **Download XCode from the App Store**

2. **Download Brew**
Open a Terminal.app window and type the following:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

3. **Download OpenCascade** (Time consuming step)
Open. Terminal.app window and type the following:
```
brew tap-new $USER/local-opencascade
brew extract --version=7.4.0 opencascade $USER/local-opencascade
brew install opencascade@7.4.0
```

4. **Create a working folder**: We will assume that you will install everything in ~/topologicbim
```
mkdir ~/topologicbim
cd ~/topologicbim
```

5. **Install Topologic**
```
git clone https://github.com/NonManifoldTopology/Topologic.git
cd Topologic
mkdir build
cd build
cmake ..
make
sudo make install
cd ../..
```

4. **Install cppyy via pip**: This is needed at runtime by the topologic module:
```
sudo -H pip3 install cppyy
```

5. **Install TopologicPy**
```
cd ~/topologicbim
git clone http://github.com/wassimj/topologicPy
cd topologicPy/cpython
python3 setup.py build
sudo python3 setup.py install
```
7. **Test**

Test in a Python 3 console:
```
cd ~/topologicbim/topologicPy
python3 example.py

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
6. Print the coordinates of the centroid of e1:
   [10.0, 10.0, 10.0]
DONE
```

### Troubleshooting
If the example doesn't work for you, you may need to add /usr/local/lib to your path. In a Terminal.app window type the following:
```
sudo nano /etc/paths
```
Add /usr/local/lib as the last line, save and quit and try again.





