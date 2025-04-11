#include <stdio.h>
#include <stdlib.h>

int x[100];
int n;

int place(int k, int i) {
    for (int j = 1; j < k; j++) {
        if (x[j] == i || abs(x[j] - i) == abs(j - k))
            return 0;
    }
    return 1;
}

void printSolution() {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (x[i] == j)
                printf("Q ");
            else
                printf("_ ");
        }
        printf("\n");
    }
    printf("\n");
}

void NQueens(int k) {
    for (int i = 1; i <= n; i++) {
        if (place(k, i)) {
            x[k] = i;
            if (k == n)
                printSolution();
            else
                NQueens(k + 1);
        }
    }
}

void main() {
    printf("Enter value of N: ");
    scanf("%d", &n);
    NQueens(1);
}
