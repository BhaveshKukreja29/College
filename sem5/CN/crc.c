#include <stdio.h>
#include <string.h>

int main() {
    int choice;
    char data_str[100], gen_str[50];
    int data[150], gen[50];
    int data_len, gen_len, total_len;
    int i, j;

    printf("1. Generate CRC Code\n");
    printf("2. Verify CRC Code\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("\n-- CRC Generation --\n");
            printf("Enter data bits: ");
            scanf("%s", data_str);
            printf("Enter generator polynomial: ");
            scanf("%s", gen_str);

            data_len = strlen(data_str);
            gen_len = strlen(gen_str);
            total_len = data_len + gen_len - 1;

            for (i = 0; i < data_len; i++) data[i] = data_str[i] - '0';
            for (i = 0; i < gen_len; i++) gen[i] = gen_str[i] - '0';
            for (i = data_len; i < total_len; i++) data[i] = 0;

            printf("\n[Step 1] Data with %d zeros appended: ", gen_len - 1);
            for (i = 0; i < total_len; i++) printf("%d", data[i]);
            printf("\n");

            for (i = 0; i <= total_len - gen_len; i++) {
                if (data[i] == 1) {
                    for (j = 0; j < gen_len; j++) {
                        data[i + j] = data[i + j] ^ gen[j];
                    }
                }
            }

            printf("[Step 2] CRC Checksum (Remainder): ");
            for (i = data_len; i < total_len; i++) printf("%d", data[i]);
            printf("\n");

            printf("[Step 3] Final message to be transmitted: %s", data_str);
            for (i = data_len; i < total_len; i++) printf("%d", data[i]);
            printf("\n");
            break;

        case 2:
            printf("\n-- CRC Verification --\n");
            printf("Enter received message (data + CRC): ");
            scanf("%s", data_str);
            printf("Enter generator polynomial: ");
            scanf("%s", gen_str);

            data_len = strlen(data_str);
            gen_len = strlen(gen_str);

            for (i = 0; i < data_len; i++) data[i] = data_str[i] - '0';
            for (i = 0; i < gen_len; i++) gen[i] = gen_str[i] - '0';

            for (i = 0; i <= data_len - gen_len; i++) {
                if (data[i] == 1) {
                    for (j = 0; j < gen_len; j++) {
                        data[i + j] = data[i + j] ^ gen[j];
                    }
                }
            }

            int is_error = 0;
            printf("\n[Computation] Remainder after division: ");
            for (i = data_len - (gen_len - 1); i < data_len; i++) {
                printf("%d", data[i]);
                if (data[i] != 0) {
                    is_error = 1;
                }
            }
            printf("\n");

            if (is_error) {
                printf("\n[Result] Error detected. The remainder is not zero.\n");
            } else {
                printf("\n[Result] No error detected. The remainder is zero.\n");
            }
            break;

        default:
            printf("Invalid choice.\n");
            break;
    }
    return 0;
}
