#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int binaryToDecimal(char *binary) {
    int decimal = 0;
    while (*binary) {
        decimal = decimal * 2 + (*binary++ - '0');
    }
    return decimal;
}

int main() {
    int process, pageSize, mmSize;

    printf("Enter size of process (in KB): ");
    scanf("%d", &process);

    printf("Enter size of page (in bytes): ");
    scanf("%d", &pageSize);

    printf("Enter size of main memory (in MB): ");
    scanf("%d", &mmSize);

    double frames = (mmSize * pow(2, 20)) / pageSize;
    double entries = ceil((process * pow(2, 10)) / pageSize);
    double pa = ceil(log2(mmSize)) + 20;
    double la = ceil(log2(process)) + 10;
    double offset = log2(pageSize);
    double pageBits = la - offset;

    printf("Total number of frames in main memory: %.0lf\n", frames);
    printf("Number of entries in page table: %.0lf\n", entries);
    printf("Number of bits in physical address: %.0lf\n", pa);
    printf("Number of bits in logical address: %.0lf\n", la);
    printf("Offset bits: %.0lf\n", offset);
    printf("Page bits: %.0lf\n", pageBits);

    int input;
    printf("Enter the number of input values in page table: ");
    scanf("%d", &input);

    int pageno[input], frameno[input], valid[input];
    printf("Enter page table in form of page_no frame_no valid_bit:\n");
    for (int i = 0; i < input; i++) {
        scanf("%d %d %d", &pageno[i], &frameno[i], &valid[i]);
    }

    char log[100];
    printf("Enter the logical address (binary): ");
    scanf("%s", log);

    char getpage[100], offsetbit[100];
    strncpy(getpage, log, (int)pageBits);
    getpage[(int)pageBits] = '\0';
    strcpy(offsetbit, log + (int)pageBits);

    int finalp = binaryToDecimal(getpage);
    int chk = -1;
    for (int i = 0; i < input; i++) {
        if (pageno[i] == finalp) {
            chk = i;
            break;
        }
    }

    if (chk != -1 && valid[chk] == 1) {
        printf("Page hit\n");

        char physicaladd[100] = "";
        int frame = frameno[chk];
        int framebits = pa - offset;

        for (int i = (int)framebits - 1; i >= 0; i--) {
            physicaladd[i] = (frame % 2) + '0';
            frame /= 2;
        }
        physicaladd[(int)framebits] = '\0';

        strcat(physicaladd, offsetbit);
        printf("Physical address is: %s\n", physicaladd);
    } else {
        printf("Page fault\n");
    }

    return 0;
}
