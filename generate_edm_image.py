#import bioformats as bf
import javabridge
import numpy as np
import tifffile as tiff #for reading tiff files
import lxml as xml
import ctypes
import math
import time
#from ctypes import cdll as libraryLoader 
from ctypes import *
#import ctypes
#import imagecodecs as codecs
import matplotlib.pyplot as plot
#import bioformats.formatreader as reader
import os
#import zarr #for parallel computing

###image = np.empty(size, np.uint8)

process_image_lib = None
OUTPUT_DIRNAME = os.getcwd() + os.sep + "outputs" + os.sep
OUTPUT_STRIPS_DIRNAME = OUTPUT_DIRNAME + os.sep + "strips" + os.sep

try:
    os.mkdir(OUTPUT_DIRNAME)
except FileExistsError as e:
    print(e)
try:
    os.mkdir(OUTPUT_STRIPS_DIRNAME)
except FileExistsError as e:
    print(e)
try:
    PROCESS_IMAGE_LIBRARY = "process_image_lib.so"
    LIB_PATH = os.getcwd() + os.sep + PROCESS_IMAGE_LIBRARY
    process_image_lib = ctypes.CDLL(LIB_PATH)
except Exception as e:
    print (e)
    
def write_tiff_file(dirname,
                    filename, 
                    data:np.ndarray):
                    oldDir = os.getcwd()
                    os.chdir(str(dirname))
                    writer = tiff.TiffWriter(str(filename))
                    writer.write(data)
                    writer.close()
                    os.chdir(str(oldDir))
	
def process_image_strips(imagePixels: np.ndarray, 
                         imagePixelsAxes: tuple,         # describes the image as Y height, X width, S sampleSize (3 is 3 dtypes) 
                         stripOffsets: tiff.TiffTag,     # describes the offsets in the image data of the strip
                         stripCounts: tiff.TiffTag,                              
                         rowsPerStrip,                   # describes the rows per strip as given from the TiffFile metadata
                         outputDirname,
                         processImageStripLibrary):      # shared library for processing strips
                         IMAGE_BOX_SIZE_WIDTH  = 2
                         IMAGE_BOX_SIZE_HEIGHT = 2
                         #presume X resolution is fair number, it divides by 2
                         #presume Y resolution is fair number, it divides by 2
                         #process the image strips as 2x2 box which calculates
                         #the light point of the EDM by referencing the four corners
                         #of the BOX (TOP_LEFT, TOP_RIGHT, BOTTOM_RIGHT, BOTTOM_LEFT)
                         #print (imageBytes)
                         #print (stripOffsets)
                         #print (stripCounts)
                         imageShape = imagePixels.shape  # shape describes the image (height,width,samples)
                         print (imagePixelsAxes)                                     
                         imageWidth = imageShape[imagePixelsAxes.index('X')]         #axe which describes image height or YResolution
                         imageHeight = imageShape[imagePixelsAxes.index('Y')]        #axe which describes image width  or XResolution
                         imageChannelCount = imageShape[imagePixelsAxes.index('S')]  #axe which describes image sample size or ChannelCount
                         print ("imageShape = " + 
                                str(imageShape))        #(YResolution, XResolution, channelComponents) format
                         print ("imagePixels.count = " + str(len(imagePixels)))
                         offsetsArray = stripOffsets.value                           #offsets where strips start (byte position in imagePixels)
                         countsArray = stripCounts.value                             #after count strips end (byte position in imagePixels)
                         offsetCountPairs = zip(offsetsArray,countsArray)            #pair offsets and counts for each strip
                         for pair in offsetCountPairs:                               #process each strip
                            offset = int(pair[0] / imageChannelCount)
                            count  = int(pair[1] / imageChannelCount)
                            strip  = imagePixels[offset:(offset + count)]
                            plot.title("initial signal representation")
                            plot_strip_channels(strip,imagePixelsAxes)
                            if int(offset + count) > int(imageHeight):
                                    count = int(imageHeight - count);
                            if (strip.shape[imagePixelsAxes.index('Y')] == 0):
                                   continue 
                            print ("imageHeight = " + str(imageHeight))
                            print ("offset  = " + str(offset))
                            print ("count = " + str(count))
                            print ("strip start at " +  str(offset))
                            print ("strip end at " +    str(offset+count))
                            print ("size = " +          str(strip.shape))
                            plot_strip_channels(strip,imagePixelsAxes)
                            startTime = time.time()
                            process_image_strip(strip,imagePixelsAxes)
                            stopTime = time.time()
                            print ("Execution time for strip from bytes " + 
                            	str(offset) + " " + "to " +
                            	str(offset + count) + " " + "is " +
                            	str(stopTime-startTime) + " " + "seconds")
                            write_tiff_file(outputDirname, "strip_" + str(strip.shape[0]) + "_" + str(strip.shape[1]) + "_" + str(strip.shape[2]) + ".tiff",
                                strip)                   
                            #boxesYOffsets = range(stripPixelIndexStart + stripShape[imageAxes.index('Y'), IMAGE_BOX_SIZE_HEIGHT, imageHeight)
                            #boxesXOffsets = range(stripPixelIndexStart, IMAGE_BOX_SIZE_WIDTH , imageWidth)
                            numBoxesX = offset / IMAGE_BOX_SIZE_WIDTH
                            numBoxesY = (offset + count) / IMAGE_BOX_SIZE_HEIGHT
                            #print (strip)
                            print (str(strip.shape))
                            #print(pair)
                            #print(strip)
                            #for offset in stripOffsets.value:
                            #@print (offset)
                            #for count in stripCounts.value:
                            #print (count)
def plot_strip_channels(strip,axes):
    shape = strip.shape
    xCount = shape[axes.index('X')]
    yCount = shape[axes.index('Y')]
    samples = shape[axes.index('S')]
    '''
    plot the discrete signal representation of each channel for each strip in the image
    plot the discrete signal using the Diract delta function
    use the c library to compute the Dirac delta function in each point of the input signal 
    plot.plot(strip[0])
    '''
    plot.plot(strip[0])
    plot.title(str(xCount) + "_" + str(yCount) + "_" + str(samples))
    plot.show()
    for channel in range(0,samples):
        for x in range (0,int(xCount-1)):
            continue
            #for y in range (0,int(yCount-1)):
                #signalPoint = strip[y][x][channel]
                #print("printing")
                #plot.title(signalPoint)
                #plot.plot()
                #'''
                #plot each signal channel independently
                #'''

def process_image_strip(image_strip: np.ndarray, 
                        image_axes:tuple): 
    print (image_strip.dtype)
    print (image_strip.shape)
    strip_width = int(image_strip.shape[image_axes.index('X')])
    strip_height = int(image_strip.shape[image_axes.index('Y')])
    if (strip_height == 0):
        return
    #stripChannelCount = image_strip.shape[image_axes.index('S')]
    pixel_size = image_strip.dtype
    print ("image height = " + str(strip_width))
    print ("image width = " + str(strip_height))
    for channel in range(0, image_strip.shape[image_axes.index('S')]):
        for imageXCoordinate in range (0,int(strip_width-1)):
            if (strip_width == 0):
                break
            for imageYCoordinate in range (0,int(strip_height-1)):
                if (strip_height == 0):
                    break
                top_left_corner = tuple([imageYCoordinate,imageXCoordinate])
                top_right_corner = tuple([imageYCoordinate,imageXCoordinate+1])
                bottom_left_corner = tuple([imageYCoordinate+1,imageXCoordinate])
                bottom_right_corner = tuple([imageYCoordinate+1,imageXCoordinate+1])

                pixel_left_top = (image_strip[top_left_corner[0]][top_left_corner[1]][channel])
                pixel_right_top = (image_strip[top_right_corner[0]][top_right_corner[1]][channel])
                pixel_left_bottom = (image_strip[bottom_left_corner[0]][bottom_left_corner[1]][channel])
                pixel_right_bottom = (image_strip[bottom_right_corner[0]][bottom_right_corner[1]][channel])
                for boxXCoordinate in range (imageXCoordinate,imageXCoordinate+1):
                    for boxYCoordinate in range (imageYCoordinate,imageYCoordinate+1):
                        process_image_lib.emptyFunction
                        #print ("stripHeight = " + str(strip_height))
                        #print ("stripWidth = " + str(strip_width))
                        #print ("boxXCoordinate = " + str(boxXCoordinate))
                        #print ("boxYCoordinate = " + str(boxYCoordinate))


#JARS_DIR_JAR = os.getcwd() + os.sep + "libraries" + os.sep + "bioformats" + os.sep + "jar"
JARS_DIR_ARTIFACTS = os.getcwd() + os.sep + "libraries" + os.sep + "bioformats" + os.sep + "artifacts"
JARS = list()
#JARS.append([JARS_DIR_JAR + os.sep + file for file in os.listdir(JARS_DIR_JAR)])
#JARS.append([str(JARS_DIR_ARTIFACTS + os.sep + file) for file in os.listdir(JARS_DIR_ARTIFACTS)])
print (JARS)

DATASET_DIR = os.getcwd() + os.sep + "../" + os.sep + "laborator" + os.sep + "Data" + os.sep + "CCS" + os.sep + "Detectie_Regiuni_Poligonale"
DATASETS = [str(DATASET_DIR + os.sep + file) for file in os.listdir(DATASET_DIR)]

OUTPUTS = [datasetFile + "_output" for datasetFile in DATASETS]

#print (JARS)
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
pages = tiffFile.pages
print ("pages length = " + str(len(tiffFile.series)))
print ("page shape = " + str(len(tiffFile.series[0].shape)))
print ("page dtype = " + str(len(tiffFile.series[0].dtype)))
print ("page axes = " + tiffFile.series[0].axes)
print ("pages.axes = " + str(pages[0].axes) + " shape = " + str(pages[0].shape))
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
image_rows_per_strip = image_metadata['RowsPerStrip']

for tag in image.tags:
    tag_name, tag_value = tag.name, tag.value
    print (tag_name)
    print (tag_value)

#print (image_data_type)
#print (tiffFile.filename)
#print(image.size)
#print (image.dtype);
#print (type(image_X_resolution))
#print (tiffFile.filename + " resolution is ")
#print (image_shape)
#print (image_strip_offsets.name)
#print (image_strip_offsets.code)
#print (image_strip_offsets.dtype)
#print (image_strip_offsets.count)
#print (image_strip_offsets.value)
#print (image_strip_offsets.valueoffset)
#print (image_strip_offsets.offset)
#print (image_strip_offsets.parent)
process_image_strips(image_data, image_axes, image_strip_offsets, image_strip_counts, image_rows_per_strip, OUTPUT_STRIPS_DIRNAME, process_image_lib)
                         
javabridge.kill_vm()
##
###for file in files:
    ###print ("file = " + file)
###
