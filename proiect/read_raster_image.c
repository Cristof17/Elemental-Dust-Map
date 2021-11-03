#include <stdio.h>
#include <stdint.h>
#include "entities.h"
#include <string.h>
#define SUCCESS 0
#define FAIL -1

typedef struct raster_image {
    uint8_t r;
} raster_image;

typedef struct bm_header {
    uint32_t size;
} bm_header_t;

typedef struct bm_core {
    bm_header_t header;
    uint16_t bcWidth;
    uint16_t bcHeight;
    uint16_t bcPlanes;
    uint16_t bcBitCount;
} bm_core_t;

typedef struct bm_info {
    bm_header_t header;
    uint32_t biWidth;
    uint32_t biHeight;
    uint16_t biPlanes;
    uint16_t biBitCount;
    uint32_t biCompression;
    uint32_t biSizeImage;
    uint32_t biXPelsPerMeter;
    uint32_t biYPelsPerMeter;
    uint32_t biClrUsed;
    uint32_t biClrImporatant;
} bm_info_t;

int read_raster_image(FILE *raster_image, pixel_t **pixels) {
    if (raster_image == NULL) {
        return FAIL;
    }
    char one_char = 0;
    char two_char = 0;
    uint32_t file_size = 0;
    uint16_t unused = 0;
    uint32_t offset = 0;
    bm_header_t image_header;
    bm_core_t bm_core_header;
    bm_info_t bm_info_header;
    size_t bytes_read = fread(&one_char,1,1,raster_image);
    bytes_read = fread(&two_char,1,1,raster_image);
    if (bytes_read == 0) {
        return FAIL;
    }
    if (!(one_char == 'B' && two_char == 'M')) {
        return FAIL;
    }
    bytes_read = fread(&file_size,1,4,raster_image);
    if (bytes_read == 0) {
        return FAIL; 
    }
    bytes_read = fread(&unused,1,2,raster_image);
    if (bytes_read == 0) {
        return FAIL;
    }
    bytes_read = fread(&unused,1,2,raster_image); 
    if (bytes_read == 0) {
        return FAIL;
    }
    bytes_read = fread(&offset,1,4,raster_image);
    if (bytes_read == 0) {
        return FAIL;
    }
    bytes_read = fread(&unused,1,offset,raster_image);
    if (bytes_read == 0) {
        return FAIL;
    }
    bytes_read = fread(&image_header,1,4,raster_image);
    if (bytes_read == 0) {
        return FAIL;
    }
    int bm_header_size = (int) image_header.size;
    if (bm_header_size == 12) {
        bytes_read = fread(&bm_core_header,1,8,raster_image);//8 is 12 -4 header
        memcpy(&(image_header.size),&(bm_core_header.header.size),sizeof(image_header));
        if (bytes_read == 0) {
            return FAIL;
        }
    } else if (bm_header_size == 40) {
        bytes_read = fread(&(bm_info_header),1,36,raster_image);//36 is 40 -4 header
        memcpy(&(image_header.size),&(bm_info_header.header.size),sizeof(image_header));
        if (bytes_read == 0) {
            return FAIL;
        }
    }
    return SUCCESS;
}
