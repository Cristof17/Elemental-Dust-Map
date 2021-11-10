#import bioformats as bf
import javabridge
import numpy as np
import tifffile as tiff #for reading tiff files
import lxml as xml
import imagecodecs as codecs
import matplotlib as matplotlib 
#import bioformats.formatreader as reader
import os
import zarr #for parallel computing

###image = np.empty(size, np.uint8)

JARS_DIR_JAR = os.getcwd() + os.sep + "libraries" + os.sep + "bioformats" + os.sep + "jar"
JARS_DIR_ARTIFACTS = os.getcwd() + os.sep + "libraries" + os.sep + "bioformats" + os.sep + "artifacts"
JARS = list()
JARS.append([JARS_DIR_JAR + os.sep + file for file in os.listdir(JARS_DIR_JAR)])
JARS.append([str(JARS_DIR_ARTIFACTS + os.sep + file) for file in os.listdir(JARS_DIR_ARTIFACTS)])
print (JARS)

DATASET_DIR = os.getcwd() + os.sep + "Data" + os.sep + "CCS" + os.sep + "Detectie_Regiuni_Poligonale"
DATASETS = [str(DATASET_DIR + os.sep + file) for file in os.listdir(DATASET_DIR)]

print (JARS)
print (DATASETS)
#print (bf.__version__)

def myfunction():
    print (myfunction)

javabridge.start_vm(class_path=str(JARS))
#print (bf.__name__)
#imagereader = bf.get_image_reader(key=None, path=DATASETS[0])
#metadata = javabridge.JWrapper(imagereader,imagereader.getMetadataStore())
#print(metadata.getChannelCount(0))
tiffFile = tiff.TiffFile(DATASETS[0])
print (tiffFile.pages)
javabridge.kill_vm()

###
###for file in files:
    ###print ("file = " + file)
###
