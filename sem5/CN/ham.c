#include <stdio.h>

void main() 
{
    // take data size
    int dataBits;
    printf("Enter number of data bits: ");
    scanf("%d", &dataBits);

    int data[dataBits];
    printf("Enter data bits: ");
    for (int i = 0; i < dataBits; i++) {
        scanf("%d", &data[i]);
    }
    printf("\n");
    for (int i = 0; i < dataBits; i++) {
        printf("%d", data[i]);
    }
    printf("\n\n");

    // make the stuff
    // 2^r >= d + r + 1
    int r = 1;

    while ((1 << r) < dataBits + r + 1) {
        r++;
    }
    printf("Number of redundant bits: %d\n", r);

    int totalBits = dataBits + r;
    int codeword[totalBits + 1]; //1 based indexing cuz otherwise har jageh 1 kon kre

    int dataIdx = dataBits - 1;

    for (int i = totalBits; i >= 1; i--) {
        if ((i & (i - 1)) != 0) {
            if (dataIdx >= 0) {
                codeword[i] = data[dataIdx];
                dataIdx--;
            }
        } else {
            codeword[i] = -1;
        }
    }

    int p_pos = 1;
    for (int i = 0; i < r; i++) {
        int count = 0;

        for (int j = 1; j <= totalBits; j++) {
            if (((j & p_pos) != 0) && (codeword[j] == 1)) {
                count++;
            }
        }
        codeword[p_pos] = count % 2;
        p_pos = p_pos << 1;
    }

    printf("The final codeword is (MSB first): ");
    for (int i = 1; i <= totalBits; i++) {
        printf("%d", codeword[i]);
    }
    printf("\n");

    // take error packet with 1 bit error
    // correct the one bit error
    int error1bit[totalBits + 1];
    printf("Enter bits with 1 bit error: ");
    for (int i = 1; i <= totalBits; i++) {
        scanf("%d", &error1bit[i]);
    }

    int errorPos = 0;
    p_pos = 1;
    for (int i = 0; i < r; i++) {
        int count = 0;
        for (int j = 1; j <= totalBits; j++) {
            if (((j & p_pos) != 0) && (error1bit[j] == 1)){
                count++;
            }
        }
        if (count % 2 != 0) {
            errorPos += p_pos;
        }

        p_pos = p_pos << 1;
    }

    if (errorPos == 0) {
        printf("No error detected.");
    } else {
        error1bit[errorPos] = (error1bit[errorPos] == 0) ? 1 : 0;

        printf("The corrected codeword is: ");
        for (int i = 1; i <= totalBits; i++) {
            printf("%d", error1bit[i]);
        }
        printf("\n");
    }

    // detect 2 bit error
}