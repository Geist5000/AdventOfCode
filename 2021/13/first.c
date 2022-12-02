#include "stdio.h"


int main() {
    FILE *file = fopen("data.txt", "r");

    char buff[100];

    int x, y;

    fscanf(file, "%d,%d", &x, &y);
    printf("%d %d", x,y);
    fclose(file);
    return 0;
}