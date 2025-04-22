#include <stdio.h>

typedef struct {
    int id;
    int size;
    int allocated; // 0 for no, 1 for yes
} process;

int main() {
    int total;
    printf("Enter total memory available: ");
    scanf("%d", &total);

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

    printf("Allocation Result:\n");
    for (int i = 0; i < n; i++) {
        if (p[i].size <= total) {
            total -= p[i].size;
            p[i].allocated = 1;
            printf("Process %d allocated\n", p[i].id);
        } else {
            printf("Process %d not allocated (insufficient memory)\n", p[i].id);
        }
    }

    printf("Remaining memory: %d\n", total);
    return 0;
}
