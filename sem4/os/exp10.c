#include <stdio.h>
#include <stdbool.h>

int main() {
    int processes, resources;

    printf("Enter number of processes: ");
    scanf("%d", &processes);
    printf("Enter number of resources: ");
    scanf("%d", &resources);

    int alloc[processes][resources], max[processes][resources], need[processes][resources], avail[resources];

    printf("\nEnter allocation matrix:\n");
    for (int i = 0; i < processes; i++) {
        for (int j = 0; j < resources; j++) {
            scanf("%d", &alloc[i][j]);
        }
    }

    printf("\nEnter maximum matrix:\n");
    for (int i = 0; i < processes; i++) {
        for (int j = 0; j < resources; j++) {
            scanf("%d", &max[i][j]);
            need[i][j] = max[i][j] - alloc[i][j]; //compute need
        }
    }

    printf("\nEnter available resources:\n");
    for (int i = 0; i < resources; i++) {
        scanf("%d", &avail[i]);
    }

    // Banker's Algorithm
    int finished[processes], safeSeq[processes], count = 0;
    for (int i = 0; i < processes; i++) finished[i] = 0;

    while (count < processes) {
        bool found = false;
        for (int i = 0; i < processes; i++) {
            if (!finished[i]) {
                bool canExecute = true;
                for (int j = 0; j < resources; j++) {
                    if (need[i][j] > avail[j]) {
                        canExecute = false;
                        break;
                    }
                }
                if (canExecute) {
                    for (int j = 0; j < resources; j++) {
                        avail[j] += alloc[i][j];
                    }
                    safeSeq[count++] = i;
                    finished[i] = 1;
                    found = true;
                }
            }
        }
        if (!found) break;
    }

    if (count == processes) {
        printf("\nSystem is in a safe state.\nSafe sequence: ");
        for (int i = 0; i < processes; i++) {
            printf("P%d ", safeSeq[i]);
        }
        printf("\n");
    } else {
        printf("\nSystem is NOT in a safe state.\n");
    }

    return 0;
}
