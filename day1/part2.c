
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "../utils/log.h"

int main() {
    int zeros = 0;
    FILE* input;

    LOG("start");

    input = fopen("input.txt", "r");
    
    if (NULL != input) {
        char* line = NULL;
        char buffer[8];
        int pos = 50;
        size_t size = 0;
        while (fgets(buffer, sizeof(buffer), input) != NULL) {
            size = strcspn(buffer, "\n");
            if (size < 8) {
                buffer[size] = '\0';
                size = size - 1;
            }

            if (buffer[0] == 'L') {
                buffer[0] = '-';
            } else if (buffer[0] == 'R'){
                buffer[0] = '+';
            } else {
                LOG("Weird entry in data! : %s", buffer);
                goto error;
            }

            int rotation = atoi(buffer);
            //LOG("rotation: %d", rotation);

            if (rotation == 0) {
                // This will never happen normally with our dataset, so atoi failed 
                LOG("ERROR: invalid conversion of buf to int: %s", buffer);
                goto error;
            }

            pos = pos + rotation;

            if (0 == (pos % 100)) {
                zeros++;
            }
        }

        fclose(input);
    } else {
        goto error;
    }

    LOG("total num of zeros: %d", zeros);

    return 0;

error:
    fclose(input);
    return 1;
}