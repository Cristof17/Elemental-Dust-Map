#define SUCCESS 0
#define FAIL -1

int read_raster_image(FILE *raster_image, pixel_t *pixels) {
    if (raster_image == NULL) {
        return FAIL;
    }
    return SUCCESS;
}
