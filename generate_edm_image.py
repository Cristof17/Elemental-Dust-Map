#import bioformats as bf
#import javabridge
import numpy as np
import tifffile as tiff #for reading tiff files
import lxml as xml
import ctypes
from ctypes import cdll as libraryLoader 
#import imagecodecs as codecs
#import matplotlib as matplotlib 
#import bioformats.formatreader as reader
import os
#import zarr #for parallel computing

###image = np.empty(size, np.uint8)

def process_image_strips(
    imagePixels: np.ndarray, 
    imagePixelsAxes: tuple, #describes the image as Y height, X width, S sampleRate
    stripOffsets: tiff.TiffTag, 
    stripCounts: tiff.TiffTag,
    processImageStripLibrary):
    #presume X resolution is fair number, it divides by 2
    #presume Y resolution is fair number, it divides by 2
    #process the image strips as 2x2 box which calculates
    #the light point of the EDM by referencing the four corners
    #of the BOX (TOP_LEFT, TOP_RIGHT, BOTTOM_RIGHT, BOTTOM_LEFT)
    IMAGE_BOX_SIZE_WIDTH = 2
    IMAGE_BOX_SIZE_HEIGHT = 2
    #print (imageBytes)
    #print (stripOffsets)
    #print (stripCounts)
    imageShape = imagePixels.shape
    print (imagePixelsAxes)
    imageWidth = imageShape[imagePixelsAxes.index('Y')]         #axe which describes image height
    imageHeight = imageShape[imagePixelsAxes.index('X')]        #axe which describes image width
    imageChannelCount = imageShape[imagePixelsAxes.index('S')]  #axe which describes image sample size
    print ("imageShape = " + str(imageShape))                   #(YResolution, XResolution, channelComponents) format
    offsetsArray = stripOffsets.value                           #start of strip (byte position in imagePixels)
    countsArray = stripCounts.value                             #end of strip (byte position in imagePixels)
    offsetCountPairs = zip(stripOffsets.value,stripCounts.value)#pair offsets and counts for each strip
    for offsetCountPair in offsetCountPairs:                    #process each strip
        if offsetCountPair[0] + offsetCountPair[1] > imagePixels.size/imageChannelCount:
            break
        offset = offsetCountPair[0]
        count  = offsetCountPair[1]
        stripPixelIndexStart =  int(offset/imageChannelCount)   #position of the strip in the image pixels
        stripPixelIndexEnd   =  int((offset + count)/imageChannelCount) #position of the strip in image pixels
        strip = imagePixels[stripPixelIndexStart:stripPixelIndexEnd]      #strip from the image pixels
        print ("strip start at " +  str(stripPixelIndexStart))
        print ("strip end at " +    str(stripPixelIndexEnd))
        print ("size = " +          str(strip.shape))
        print ("Strip pixels start " + str(stripPixelIndexStart))
        print ("Strip pixels end   " + str(stripPixelIndexStart + strip.shape[imagePixelsAxes.index('Y')]))
        pixelsStrip = imagePixels[stripPixelIndexStart:stripPixelIndexStart + strip.shape[imagePixelsAxes.index('Y')]]
        print ("pixelsStrip.shape = " + str(pixelsStrip.shape))
        #boxesYOffsets = range(stripPixelIndexStart + stripShape[imageAxes.index('Y'), IMAGE_BOX_SIZE_HEIGHT, imageHeight)
        #boxesXOffsets = range(stripPixelIndexStart, IMAGE_BOX_SIZE_WIDTH , imageWidth)
        numBoxesX = stripPixelIndexStart /  IMAGE_BOX_SIZE_WIDTH
        numBoxesY = stripPixelIndexEnd  /   IMAGE_BOX_SIZE_HEIGHT
        print (strip)
        #print(pair)
        #print(strip)
    #for offset in stripOffsets.value:
        #@print (offset)
    #for count in stripCounts.value:
        #print (count)
        

#JARS_DIR_JAR = os.getcwd() + os.sep + "libraries" + os.sep + "bioformats" + os.sep + "jar"
#JARS_DIR_ARTIFACTS = os.getcwd() + os.sep + "libraries" + os.sep + "bioformats" + os.sep + "artifacts"
#JARS = list()
#JARS.append([JARS_DIR_JAR + os.sep + file for file in os.listdir(JARS_DIR_JAR)])
#JARS.append([str(JARS_DIR_ARTIFACTS + os.sep + file) for file in os.listdir(JARS_DIR_ARTIFACTS)])
#print (JARS)

DATASET_DIR = os.getcwd() + os.sep + "../" + os.sep + "laborator" + os.sep + "Data" + os.sep + "CCS" + os.sep + "Detectie_Regiuni_Poligonale"
DATASETS = [str(DATASET_DIR + os.sep + file) for file in os.listdir(DATASET_DIR)]

OUTPUTS = [datasetFile + "_output" for datasetFile in DATASETS]

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
process_image_lib = None
try:
    PROCESS_IMAGE_STRIP_LIBRARY = "process_image_strip.so"
    process_image_lib = libraryLoader.LoadLibrary(os.getcwd() + os.sep + PROCESS_IMAGE_LIBRARY)
except Exception as e:
    print (e)
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
process_image_strips(image_data, image_axes, image_strip_offsets, image_strip_counts,process_image_lib)
#javabridge.kill_vm()
###
###for file in files:
    ###print ("file = " + file)
###
