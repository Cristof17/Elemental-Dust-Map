#include <stdio.h>
#include <stdlib.h>
#include "entities.h"
#define SUCCESS 0
#define FAIL -1

int read_raster_image(FILE *raster_image, pixel_t *pixels);

int main(int argc, char **argv) {
    if (argc == 1) {
        fprintf(stdout,"%s <raster_image_file> \n",argv[0]);
        return FAIL;
    }
    FILE *image_file = fopen(argv[0], "r");
    pixel_t **pixels = (pixel_t **) calloc(1,sizeof(pixel_t *));
    int rc = read_raster_image(image_file, pixels[0]);
    if (rc == FAIL) {
        perror("error reading image_file");
        return FAIL;
    }
    fclose(image_file);
    return SUCCESS;
}
