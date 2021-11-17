#include <stdio.h>
#include "entities.h"
#define BLACK 0
#define WHITE 1
#define SUCCESS 0
#define FAIL 1

EDP_t *generate_edp_from_pixel(uint8_t raster_pixel, uint8_t raster_pixel_x, uint8_t raster_pixel_y) {
	EDP_t *edp = (EDP_t *)malloc(1 * sizeof(EDP_t));
	edp -> luminosity_t = (float) raster_pixel;
	edp -> pixel.pixel_boundary.P1.x = raster_pixel_x;
	edp -> pixel.pixel_boundary.P1.y = raster_pixel_y;
	edp -> pixel.pixel_boundary.P2.x = raster_pixel_x + 1;
	edp -> pixel.pixel_boundary.P2.y = raster_pixel_y;
	edp -> pixel.pixel_boundary.P3.x = raster_pixel_x + 1;
	edp -> pixel.pixel_boundary.P3.y = raster_pixel_y + 1;
	edp -> pixel.pixel_boundary.P4 = raster_pixel_x;
	edp -> pixel.pixel_boundary.P4 = raster_pixel_y + 1;
	edp -> pixel.pixel_coordinates.x = (float) raster_pixe_x;
	edp -> pixel.pixel_coordinates.y = (float) raster_pixe_y;
	return edp;
}

EDM_t *generate_edm_from_raster(EDP_t* light_sources, size_t light_sources_size) {
	if (raster_image == NULL) {
	    	return NULL;	
	}
}
