#include <stdio.h>

typedef struct {
    int id;
    int size;
    int allocated;
} process;

int main() {
    int total, partSize;
    printf("Enter total memory: ");
    scanf("%d", &total);
    printf("Enter partition size: ");
    scanf("%d", &partSize);

    int parts = total / partSize;
    printf("Total partitions: %d\n", parts);

    int n;
    printf("Enter number of processes: ");
    scanf("%d", &n);

    process p[n];

    for (int i = 0; i < n; i++) {
        printf("Enter size of process %d: ", i + 1);
        scanf("%d", &p[i].size);
        p[i].id = i + 1;
        p[i].allocated = 0;
    }

    int used = 0;
    for (int i = 0; i < n && used < parts; i++) {
        if (p[i].size <= partSize) {
            p[i].allocated = 1;
            used++;
            printf("Process %d allocated to partition %d\n", p[i].id, used);
        } else {
            printf("Process %d too big for partition\n", p[i].id);
        }
    }

    for (int i = 0; i < n; i++) {
        if (!p[i].allocated && p[i].size <= partSize)
            printf("Process %d not allocated (partitions full)\n", p[i].id);
    }

    printf("Internal fragmentation: %d\n", used * (partSize) - total + (total - (used * partSize)));
    return 0;
}
