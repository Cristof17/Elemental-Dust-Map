#import bioformats as bf
#import javabridge
import numpy as np
import tifffile as tiff #for reading tiff files
import lxml as xml
#import imagecodecs as codecs
#import matplotlib as matplotlib 
#import bioformats.formatreader as reader
import os
#import zarr #for parallel computing

###image = np.empty(size, np.uint8)

def process_image_strips(imageBytes: np.ndarray, stripOffsets: np.ndarray, stripCounts: np.ndarray):
    print (imageBytes)
    print (stripOffsets)
    print (stripCounts)

#JARS_DIR_JAR = os.getcwd() + os.sep + "libraries" + os.sep + "bioformats" + os.sep + "jar"
#JARS_DIR_ARTIFACTS = os.getcwd() + os.sep + "libraries" + os.sep + "bioformats" + os.sep + "artifacts"
#JARS = list()
#JARS.append([JARS_DIR_JAR + os.sep + file for file in os.listdir(JARS_DIR_JAR)])
#JARS.append([str(JARS_DIR_ARTIFACTS + os.sep + file) for file in os.listdir(JARS_DIR_ARTIFACTS)])
#print (JARS)

DATASET_DIR = os.getcwd() + os.sep + "laborator" + os.sep + "Data" + os.sep + "CCS" + os.sep + "Detectie_Regiuni_Poligonale"
DATASETS = [str(DATASET_DIR + os.sep + file) for file in os.listdir(DATASET_DIR)]

#print (JARS)
print (DATASETS)
#print (bf.__version__)

def myfunction():
    print (myfunction)

#javabridge.start_vm(class_path=str(JARS))
#print (bf.__name__)
#imagereader = bf.get_image_reader(key=None, path=DATASETS[0])
#metadata = javabridge.JWrapper(imagereader,imagereader.getMetadataStore())
#print(metadata.getChannelCount(0))
tiffFile = tiff.TiffFile(DATASETS[0])
pages = tiffFile.pages
image = pages[0] #numpy array
image_size = image.shape
image_index = image.index #int or tuple of int index of the page in file
image_data_type = image.dtype #numpy.dtype or NONE
image_shape = image.shape #tuple of int , dimensions in IFD
image_axes = image.axes #string 'S' sample, 'X' width, 'Y' length, 'Z' depth
image_colorMap = image.colormap #numpy.ndarray color lookup table
image_shape = image.shaped #tuple of int 0 : separate samplesperpixel or 1 
                           #             1 : imagedepth Z or 1
                           #             2 : imagelength Y
                           #             3 : imagewidth X
                           #             4 : contig samplesperpixel or 1
image_data = image.asarray()
image_metadata = image.tags #TiffTags multidict in IFD
image_width = image_metadata['ImageWidth']
image_height = image_metadata['ImageLength']
image_bits_per_sample = image_metadata['BitsPerSample']
image_compression = image_metadata['Compression']
image_color_space = image_metadata['PhotometricInterpretation']
image_fill_order = image_metadata['FillOrder'] #MSB2LSB
image_X_resolution = image_metadata['XResolution'] # python tuple
image_Y_resolution = image_metadata['YResolution'] # python tuple
image_samples_per_pixel = image_metadata['SamplesPerPixel']
image_source_and_version= image_metadata['Software']
image_timestamp = image_metadata['DateTime']
image_artist = image_metadata['Artist']
image_sample_format = image_metadata['SampleFormat']
image_strip_offsets = image_metadata['StripOffsets']
image_strip_counts = image_metadata['StripByteCounts']


for tag in image.tags:
    tag_name, tag_value = tag.name, tag.value
    print (tag_name)
    print (tag_value)
print (image_data_type)
print (tiffFile.filename)
print(image.size)
print (image.dtype);
print (type(image_X_resolution))
print (tiffFile.filename + " resolution is ")
print (image_shape)
process_image_strips(image_data, image_strip_offsets, image_strip_counts)
#javabridge.kill_vm()
###
###for file in files:
    ###print ("file = " + file)
###
