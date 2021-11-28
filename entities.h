typedef struct coordinate {
    float coordinate_value;
} coordinate_t;

typedef struct point {
    coordinate_t *point_coordinate;
} point_t;

typedef struct boundary {
    point_t *boundary_points; 
} boundary_t;

typedef struct luminosity {
    float luminosity_value;
} luminosity_t;

typedef struct pixel {
    point_t *pixel_point;
    boundary_t *pixel_boundary;     
    luminosity_t *pixel_luminosity;
} pixel_t;


typedef struct edp {
    pixel_t *edp_pixel;
} EDP_t;

typedef struct edm {
    EDP_t *edm_edp; 
} EDM_t;
