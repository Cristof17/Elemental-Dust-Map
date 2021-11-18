typedef struct coordinate {
    float real_plane_coordinate;
} coordinate_t;

typedef struct point {
    coordinate_t x;
    coordinate_t y;
} point_t;

typedef struct boundary {
    point_t P1; 
    point_t P2;
    point_t P3;
    point_t P4;
} boundary_t;

typedef struct luminosity {
    float luminosity;
} luminosity_t;

typedef struct pixel {
    point_t pixel_coordinates;
    boundary_t pixel_boundary;     
    luminosity_t luminosity;
} pixel_t;

typedef struct edp {
    pixel_t pixel;
} EDP_t;

typedef struct edm {
    EDP_t * edp_rectangle; 
} EDM_t;
