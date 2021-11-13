### Compile
- install cmake
#### Linux
- install cmake
```
apt-get install cmake
```
- install **tifffile** python library for tifffile parsing
	- _documentation_ for TIFF in **documentation** folder 
```
pip install tifffile 
```
- install numpy for image data
	- _documentation_ for numpy in **documentation** folder 
```
pip install numpy
```
###alternatively use imread
- install zarr for compression formats
	- **required version** 2021.11.2
	- **tested on little endian platforms**
	- **python3.7 versions are deprecated**
```
pip install zarr
```
- install CPython for zarr **maybe it is necessary; didn't use zarr so far**
	- Cpython 3.10.0, 64bit
**this is for C**
```
pip install cpython
```

### this is for Java VM 
### TIFF File parser which uses java VM, **not working**
- install **ant**
```
sudo apt-get install ant for building libraries
```
**use bioformats.formatreader for reading**
***documentation at https://pythonhosted.org/python-bioformats/_modules/bioformats/formatreader.html***

```
pip install python-bioformats
```
### install javabridge
```
pip install javabridge
```
**required version 1.21.3**

```
pip install Matplotlib 
```
**required version** 3.4.3

```
pip install lxml
```
**required version 4.6.3**

```
pip install imagecodecs
```
**required version 2021.8.26**

