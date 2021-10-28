#include <stdio.h>
#include "entities.h"
#define SUCCESS 0
#define FAIL -1

int main(int argc, char **argv) {
    if (argc == 1) {
        fprintf(stdout,"%s <raster_image_file> \n",argv[0]);
        return FAIL;
    }
    return SUCCESS;
}
