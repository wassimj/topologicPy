# About

This module integrates a set of Python bindings for the Topologic module.

# Installation on Ubuntu

This guide explains how to setup Topologic and its Python bindings on a fresh Ubuntu instance.

# Requirements

Any recent version of Ubuntu should work. However it is recommended to use Ubuntu >= 20. During our testing
we used: Ubuntu 20.10

# Start Install

## Step 1. Update package manager
```
sudo apt-get install -y bzip2 \
	cmake \
	g++ \
	git \
	libharfbuzz-dev \
	make \
	libgl-dev \
	libglu-dev \
	libpng-dev \
	libxmu-dev \
	libxi-dev \
	libtbb-dev \
	tcl \
	tcl-dev \
	tk \
	tk-dev \
	unzip \
	zlib1g-dev \
	&& apt-get update -y
```
 
## Step 2. Install Freetype

```
cd /usr/src/
wget https://netactuate.dl.sourceforge.net/project/freetype/freetype2/2.9.1/freetype-2.9.1.tar.gz
tar xvf freetype-2.9.1.tar.gz
cd freetype-2.9.1
./configure && make && make install
```

## Step 3. Install FreeImage

```
cd /usr/src/
wget https://managedway.dl.sourceforge.net/project/freeimage/Source%20Distribution/3.18.0/FreeImage3180.zip
unzip FreeImage3180.zip
cd FreeImage && \
	make && \
	make install
```

## Step 4. Install OpenCascade (this is very time-consuming. There may be a shorter method to get the files)

```
cd /usr/src/
wget https://github.com/tpaviot/oce/releases/download/official-upstream-packages/opencascade-7.4.0.tgz
cd opencascade-7.4.0
mkdir build && \
	cd build && \
	cmake .. && \
	make && \
	make install
```

## Step 5. Install cppyy

```
sudo pip3 install cppyy
```

## Step 6. Install Topologic

```
cd /usr/src/
git clone https://github.com/NonManifoldTopology/Topologic.git
cd Topologic
mkdir build && \
	cd build && \
	cmake -DCMAKE_CXX_FLAGS=-I\ /usr/local/include/opencascade .. && \
	make
```

## Step 7. Setup Python bindings

```
cd /usr/src/
sudo git clone https://github.com/wassimj/topologic.git
cd Topologic
cd cpython
python3 setup.py build
python3 setup.py install
```

# Testing

You can use the Python setup scripts to build the module locally.

To build the module:

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

# Run example

There is an example test file we have used to test the module. This example, while basic, shows how you can
use the Python/C++ to make calls directly to Topologic.

Running the example:

```
cd ..
python3 ./example.py
```

Example output
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
