build:
	gcc -c generate_edm_from_raster.c -o generate_edm_from_raster.o
	gcc -c main.c -o main.o
	gcc generate_edm_from_raster.o main.o -o main
run:
	./main
clean:
	rm -rf generate_edm_from_raster.o main.o main
.PHONY: clean
