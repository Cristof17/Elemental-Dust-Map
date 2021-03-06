### Compile
#### Linux
##### Generate build configuration using cmake
1. install cmake
```
apt install cmake
```
2. run cmake
```
cmake -G Unix\ Makefiles
```
3. run make
```
make
```

- fisierul ***generate_edm_image.py*** este doar pentru a analiza mai repede rezultatele grafice pentru procesarea semnalului de intrare
- fisierul ***generate_edm_image.cpp*** este pentru a impementa algorimii de procesare a semnalului sub forma unor clase
- fisierul ***generate_edm_from_raster.c*** este pentru a rula algoritmii pentru o unitate grafica in care timpii de rulare sunt foarte importanti
- fisierul ***generate_edm_from_raster.c*** este compilat intr-o biblioteca dinamica care este:
	- link-editata intr-un fisier executabil impreuna cu clasele din fisierul ***generate_edm_image.cpp***
	- importata in scriptul python pentru a putea desena reprezentarea semnalului
### Run
#### Linux
1. install python3
```
apt install python3
```
##### Python
- install **tifffile** python library for tifffile parsing
	- _documentation_ for TIFF in **documentation** folder 
	- ***alternatively*** use imread
```
pip3 install tifffile 
```
- install **numpy** for image data
	- _documentation_ for numpy in **documentation** folder 
```
pip3 install numpy
```
- install **ctypes** for calling C functions from Python
```
pip3 install ctypes
```
- install **zarr** for compression formats
	- **required version** 2021.11.2
	- **tested on little endian platforms**
	- **python3.7 versions are deprecated**
```
pip3 install zarr
```
- install CPython for zarr **maybe it is necessary; didn't use zarr so far**
	- Cpython 3.10.0, 64bit
```
pip3 install cpython
```

###Test
#### Linux
1. install matplotlib
```
pip install matplotlib
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
####Running
#### Linux
python3 generate_edm_image.py
```

#### Cleaning
```
make clean
```
