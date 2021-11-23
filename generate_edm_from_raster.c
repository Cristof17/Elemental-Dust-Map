#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include "entities.h"
#define BLACK 0
#define WHITE 1
#define SUCCESS 0
#define FAIL 1

typedef size_t iterator_t;

/*
 * bpp BITS PER PIXEL
 */
EDP_t *generate_edps_from_pixel(uint8_t raster_pixel_x, uint8_t raster_pixel_y, uint8_t bpp, int pixel_value) {
	EDP_t *edp = (EDP_t *)malloc(pixel_value * sizeof(EDP_t));
	for (int i = 0; i < pixel_value; i++) {
	}
	edp -> pixel.luminosity.luminosity = (float) pixel_value;
	edp -> pixel.pixel_boundary.P1.x.real_plane_coordinate = raster_pixel_x;
	edp -> pixel.pixel_boundary.P1.y.real_plane_coordinate  = raster_pixel_y;
	edp -> pixel.pixel_boundary.P2.x.real_plane_coordinate = raster_pixel_x + 1;
	edp -> pixel.pixel_boundary.P2.y.real_plane_coordinate = raster_pixel_y;
	edp -> pixel.pixel_boundary.P3.x.real_plane_coordinate = raster_pixel_x + 1;
	edp -> pixel.pixel_boundary.P3.y.real_plane_coordinate = raster_pixel_y + 1;
	edp -> pixel.pixel_boundary.P4.x.real_plane_coordinate = raster_pixel_x;
	edp -> pixel.pixel_boundary.P4.x.real_plane_coordinate = raster_pixel_y + 1;
	edp -> pixel.pixel_coordinates.x.real_plane_coordinate = (float) raster_pixel_x;
	edp -> pixel.pixel_coordinates.y.real_plane_coordinate = (float) raster_pixel_y;
	return edp;
}

void emptyFunction() {
}

EDM_t *generate_edm_from_edp(EDP_t* light_sources, size_t light_sources_size) {
	if (light_sources == NULL) {
	    	return NULL;	
	}
	iterator_t it = 0;
	for (it = 0; it < light_sources_size; it++) {
		EDP_t edp = light_sources[it];
	}
}
