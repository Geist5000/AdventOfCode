#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "stdbool.h"


int main() {
    FILE *file = fopen("data.txt", "r");

    u_long maxCalorie = 0;
    u_long current = 0;
    char currentCalorie[255];
    bool eof = false;
    do {
        eof = NULL == fgets(currentCalorie, 255, file);
        u_long count = strlen(currentCalorie);
        if (count > 2 || count == 2 && currentCalorie[0] != '\r') {
            char *end;
            long currentNumber = strtol(currentCalorie, &end, 10);
            current += currentNumber;

        } else {
            if (current > maxCalorie) {
                maxCalorie = current;
            }
            current = 0;
        }
    } while (!eof);

    if (current > maxCalorie) {
        maxCalorie = current;
    }

    printf("%lu", maxCalorie);
    return EXIT_SUCCESS;
}