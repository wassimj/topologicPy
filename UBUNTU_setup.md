# Installation on Ubuntu

This guide explains how to setup Topologic and its Python bindings on a fresh Ubuntu instance.

# Requirements

Any recent version of Ubuntu should work. However it is recommended to use Ubuntu >= 20. During our testing
we used: Ubuntu 20.10

# Start Install

### Step 1. Update package manager
```
apt-get install -y bzip2 \
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
 
### Step 2. Install Freetype

``
cd /usr/src/
wget https://netactuate.dl.sourceforge.net/project/freetype/freetype2/2.9.1/freetype-2.9.1.tar.gz
tar xvf freetype-2.9.1.tar.gz
cd freetype-2.9.1
./configure && make && make install
```

### Step 3. Install FreeImage

``
cd /usr/src/
wget https://managedway.dl.sourceforge.net/project/freeimage/Source%20Distribution/3.18.0/FreeImage3180.zip
unzip FreeImage3180.zip
cd FreeImage && \
	make && \
	make install
```

### Step 4. Install OpenCascade

``
cd /usr/src/
wget https://github.com/tpaviot/oce/releases/download/official-upstream-packages/opencascade-7.4.0.tgz
cd opencascade-7.4.0
mkdir build && \
	cd build && \
	cmake .. && \
	make && \
	make install
```

### Step 5. Install Topologic

``
cd /usr/src/
git clone https://github.com/NonManifoldTopology/Topologic.git
cd Topologic
mkdir build && \
	cd build && \
	cmake -DCMAKE_CXX_FLAGS=-I\ /usr/local/include/opencascade .. && \
	make
```

### Step 6. Setup Python bindings

``
cd /usr/src/
git clone https://matrixnad@bitbucket.org/matrixnad/wasim-cpython-topologic.git
cd wasim-cpython-topologic
cd cpython
python setup.py build
python setup.py install
```


## Testing

To test Topologic, please refer the test examples in [README.md](./README.md)
