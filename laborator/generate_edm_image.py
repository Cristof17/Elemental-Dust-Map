import bioformats
import javabridge
import numpy as np
import tifffile as tiff
import lxml as xml
import imagecodecs as codecs
import matplotlib as matplotlib 
import bioformats.formatreader as reader
import os

###image = np.empty(size, np.uint8)

JARS_DIR_JAR = os.getcwd() + os.sep + "libraries" + os.sep + "bioformats" + os.sep + "jar"
JARS_DIR_ARTIFACTS = os.getcwd() + os.sep + "libraries" + os.sep + "bioformats" + os.sep + "artifacts"
JARS = list()
JARS.append([JARS_DIR_JAR + os.sep + file for file in os.listdir(JARS_DIR_JAR)])
JARS.append([str(JARS_DIR_ARTIFACTS + os.sep + file) for file in os.listdir(JARS_DIR_ARTIFACTS)])

DATASET_DIR = os.getcwd() + os.sep + "Data" + os.sep + "CCS" + os.sep + "Detectie_Regiuni_Poligonale"
DATASETS = [str(DATASET_DIR + os.sep + file) for file in os.listdir(DATASET_DIR)]

print (JARS)
print (DATASETS)
print (bioformats.__version__)

def myfunction():
    print (myfunction)

javabridge.start_vm(class_path=str(JARS))
javabridge.kill_vm()

###
###for file in files:
    ###print ("file = " + file)
###
