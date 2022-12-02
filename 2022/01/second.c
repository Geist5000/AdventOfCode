#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "stdbool.h"

#define TOP_COUNT 3

int main() {
    FILE *file = fopen("data.txt", "r");

    if (file == NULL) {
        printf("couldn't open file");
    }

    u_long maxCalories[] = {0, 0, 0};
    u_long current = 0;
    char currentCalorie[255];
    bool eof = false;
    do {
        eof = NULL == fgets(currentCalorie, 255, file);
        u_long count = strlen(currentCalorie);
        if (eof == false && (count > 2 || count == 2 && currentCalorie[0] != '\r')) {
            char *end;
            long currentNumber = strtol(currentCalorie, &end, 10);
            current += currentNumber;

        } else {
            u_long toCheck = current;
            for (int i = 0; i < TOP_COUNT; ++i) {
                if (maxCalories[i] < toCheck) {
                    u_long temp = maxCalories[i];
                    maxCalories[i] = toCheck;
                    toCheck = temp;
                    i = -1;
                }
            }
            current = 0;
        }
    } while (!eof);
    fclose(file);

    u_long toCheck = current;
    for (int i = 0; i < TOP_COUNT; ++i) {
        if (maxCalories[i] < toCheck) {
            u_long temp = maxCalories[i];
            maxCalories[i] = toCheck;
            toCheck = temp;
            i = -1;
        }
    }


    u_long sum = 0;
    for (int i = 0; i < TOP_COUNT; ++i) {
        sum += maxCalories[i];
    }

    printf("%lu", sum);
    return EXIT_SUCCESS;
}