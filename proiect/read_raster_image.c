#include <stdio.h>
#include <stdint.h>
#include "entities.h"
#define SUCCESS 0
#define FAIL -1

typedef struct raster_image {
    uint8_t r;
} raster_image;

int read_raster_image(FILE *raster_image, pixel_t *pixels) {
    if (raster_image == NULL) {
        return FAIL;
    }
    char one_char = 0;
    char two_char = 0;
    uint32_t file_size = 0;
    uint16_t unused = 0;
    uint32_t offset = 0;
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
    return SUCCESS;
}
