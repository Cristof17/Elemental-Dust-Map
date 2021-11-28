#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <errno.h>
#include "entities.h"
#define BLACK 0
#define WHITE 1
#define SUCCESS 0
#define FAIL 1
#define ERRNULLPTR 2

#define EDP_COUNT 1
#define POINT_COUNT 4
#define PIXEL_COUNT 1
#define BOUNDARY_COUNT 1
#define LUMINOSITY_COUNT 1

typedef size_t iterator_t;

static EDP *generate_edps_from_pixel(uint8_t raster_x,
								uint8_t raster_y, uint8_t image_bpp,
								uint8_t raster_value);
static void empty_function(void);

static int edp_boundary_point_coordinate_value_init(
								coordinate_t *coordinate, uint8_t value);

int
edp_boundary_point_coordinate_value_init(coordinate_t *coordinate, 
								uint8_t value) {
	if (coordinate_x != NULL) {
		if (value > 0) {
			coordinate_x->coordinate_value = (float) value;
			return SUCCESS;
		} else {
			return EINVAL;
	} else {
		return ENULLPTR;
	}
return FAIL;
}


/*
 * bpp BITS PER PIXEL
 */
EDP_t *
generate_edps_from_pixel(uint8_t raster_x, uint8_t raster_y,
							 	uint8_t image_bpp, uint32_t raster_value) 
{
	EDP_t *edp = NULL;
	pixel_t *pixels = NULL;
	point_t *points = NULL;
	boundary_t *boundaries = NULL;
	coodinate_t *coordinates = NULL;
	luminosity_t *luminosity = NULL;
	
	edps = (edp_t*) malloc(EDP_COUNT * 
									sizeof(edp[0]));
	pixels = (pixel_t*) malloc(PIXEL_COUNT * 
									sizeof(pixels[0]));
	points = (point_t*) malloc(POINT_COUNT * 
									sizeof(points[0]));
	coordinates = (coordinate_t*) malloc(COORDINATES_COUNT * 
									sizeof(coordinates[0]));
	boundaries = (boundary_t*) malloc(BOUNDARY_COUNT * 
									sizeof(bounding_box[0]));
	luminosity = (luminosity*) malloc(LUMINOSITIY_COUNT * 
									sizeof(luminosity[0]));

	edp_pixel_boundary_point_coordinate_value_init(coordinates[0],raster_x);
	edp_pixel_boundary_point_coordinate_value_init(coordinates[1],raster_y);
	edp_pixel_boundary_point_coordinate_value_init(coordinates[2],raster_x+1);
	edp_pixel_boundary_point_coordinate_value_init(coordinates[3],raster_y);
	edp_pixel_boundary_point_coordinate_value_init(coordinates[4],raster_x+1);
	edp_pixel_boundary_point_coordinate_value_init(coordinates[4],raster_x+1);
	edp_pixel_boundary_point_coordinate_value_init(coordinates[5],raster_x);
	edp_pixel_boundary_point_coordinate_value_init(coordinates[6],raster_y+1);

	edp_pixel_boundary_point_init(
									coordinates[0],coordinates[1],
									coordinates[2],coordinates[3]);
	int i = 0;

	edp = (EDP*)malloc(1 * sizeof(edp[0]));
	pixel = (pixel_t*)malloc(1 * sizeof(pixel[0]));

	for (i = 0; i < raster_value; i++) {
	}
	edp->edp_pixel.pixel_luminosity.luminosity_value = 
					(float) pixel_value;
	edp->edp_pixel.pixel_boundary_point_top_left.
					point_coordinate_x.coordinate_value = 
					raster_x;
	edp->edp_pixel.pixel_boundary_point_top_left.
					point_coordinate_y.coordinate_value = 
					raster_y;
	edp->edp_pixel.pixel_boundary_point_top_right.
					point_coordinate_x.coordinate_value =
				 	raster_x + 1;
	edp->edp_pixel.pixel_boundary_point_top_left.
					point_coordinate_y.coordinate_value = 
					raster_y;
	edp->edp_pixel.pixel_boundary_point_bottom_right.
					point_coordinate_x.coordinate_value =
				 	raster_x + 1;
	edp-> pixel.pixel_boundary.P1.y.real_plane_coordinate  = raster_pixel_y;
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
