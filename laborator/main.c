#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    FILE *file = fopen(argv[0], "rw");
    fclose(file);
    return 0;
}
