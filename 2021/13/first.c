#include "stdio.h"


int main() {
    FILE *file = fopen("data.txt", "r");

    char buff[100];

    fgets(buff, 100, file);
    printf("%s", buff);
    fclose(file);
    return 0;
}