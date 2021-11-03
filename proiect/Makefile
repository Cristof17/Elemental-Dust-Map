tests = Data/CCS/242_0_2638730_0_5D1327B5.tif \
        Data/CCS/242_0_2638730_0_5D1327B5.tif \
        Data/CCS/242_12_2638730_20_5D132A8C.tif \
        Data/CCS/242_16_2638730_24_5D132B0E.tif \
        Data/CCS/242_10_2638730_19_5D132A6D.tif \
        Data/CCS/242_14_2638730_22_5D132AD1.tif
build:
	gcc -c read_raster_image.c -o read_raster_image.o
	gcc -c main.c -o main.o
	gcc read_raster_image.o main.o -o main
run:
	./main 242_0_2638730_0_5D1327B5.tif
clean:
	rm -rf read_raster_image.o main.o main
.PHONY: clean
