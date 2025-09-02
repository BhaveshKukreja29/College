#include <stdio.h>

int main() {
    int choice;
    printf("Hamming Code Implementation\n");
    printf("1. Generate Hamming Code\n");
    printf("2. Find and Correct Error\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);
    printf("\n");

    if (choice == 1) {
        int data_bits[20];
        int m, p = 0, n, i, j, k;

        printf("Enter number of data bits: ");
        scanf("%d", &m);
        printf("Enter data bits (Seperate each bit by a space): ");
        for (i = 0; i < m; i++) {
            scanf("%d", &data_bits[i]);
        }

        while ((1 << p) < (m + p + 1)) {
            p++;
        }
        n = m + p;
        
        printf("\n--- COMPUTATION ---\n");
        printf("Data bits (m) = %d, Required parity bits (p) = %d, Total bits (n) = %d\n", m, p, n);

        int codeword[n + 1];
        j = 0;
        k = 0;
        for (i = 1; i <= n; i++) {
            if (i == (1 << k)) {
                codeword[i] = 0;
                k++;
            } else {
                codeword[i] = data_bits[j];
                j++;
            }
        }
        printf("\n1. Initial Codeword Structure:\n");
        printf("Position:  ");
        for (i = 1; i <= n; i++) printf("%-3d", i);
        printf("\nType:      ");
        j = 1; k = 1;
        for (i = 1; i <= n; i++) {
            if (i == (1 << (k - 1))) {
                printf("P%-2d", k++);
            } else {
                printf("D%-2d", j++);
            }
        }
        printf("\nValue:     ");
        for (i = 1; i <= n; i++) printf("%-3d", codeword[i]);
        printf("\n");


        printf("\n2. Calculating Parity Bit Values (for Even Parity):\n");
        for (i = 0; i < p; i++) {
            int parity_pos = 1 << i;
            int one_count = 0;
            printf("\n -> For P%d at position %d, checking bits: ", i + 1, parity_pos);
            for (j = parity_pos; j <= n; j++) {
                if (((j >> i) & 1) && (j != parity_pos)) {
                     printf("%d ", j);
                     if (codeword[j] == 1) one_count++;
                }
            }
            if (one_count % 2 != 0) {
                codeword[parity_pos] = 1;
            }
            printf("\n    Count of 1s in corresponding data bits is %d. Setting P%d = %d.\n", one_count, i + 1, codeword[parity_pos]);
        }

        printf("\n--- RESULT ---\n");
        printf("Final Generated Hamming Code: ");
        for (i = 1; i <= n; i++) {
            printf("%d", codeword[i]);
        }
        printf("\n");

    } else if (choice == 2) {
        int received_code[30];
        int n, p = 0, i, j, k;

        printf("Enter length of received codeword: ");
        scanf("%d", &n);
        printf("Enter received codeword bits: ");
        for (i = 1; i <= n; i++) {
            scanf("%d", &received_code[i]);
        }

        while ((1 << p) <= n) {
            p++;
        }

        printf("\n--- COMPUTATION ---\n");
        int error_pos = 0;
        for (i = 0; i < p; i++) {
            int parity_pos = 1 << i;
            int one_count = 0;
            printf("Checking P%d group (position %d):\n", i + 1, parity_pos);
            printf("  > Bits checked: ");
            for (j = parity_pos; j <= n; j++) {
                if ((j >> i) & 1) {
                    printf("%d ", j);
                    if (received_code[j] == 1) one_count++;
                }
            }
            
            if (one_count % 2 != 0) {
                printf("\n  > Number of 1s is %d (ODD). Parity check FAILED.\n", one_count);
                error_pos += parity_pos;
            } else {
                printf("\n  > Number of 1s is %d (EVEN). Parity check PASSED.\n", one_count);
            }
        }

        printf("\n--- RESULT ---\n");
        if (error_pos == 0) {
            printf("Syndrome is 0. No error detected.\n");
        } else if (error_pos > n) {
            printf("Syndrome is %d. Error position is out of bounds.\n", error_pos);
            printf("This indicates multiple bit errors, which cannot be corrected.\n");
        } else {
            printf("Syndrome is %d. Error detected at position %d.\n", error_pos);
            received_code[error_pos] = 1 - received_code[error_pos];
            printf("Corrected Codeword: ");
            for (i = 1; i <= n; i++) printf("%d", received_code[i]);
            printf("\n");
        }
        
        printf("Data bits from (corrected) codeword: ");
        k = 0;
        for (i = 1; i <= n; i++) {
            if (i == (1 << k)) {
                k++;
            } else {
                if(i <= n) printf("%d", received_code[i]);
            }
        }
        printf("\n");

    } else {
        printf("Invalid choice.\n");
    }

    return 0;
}
