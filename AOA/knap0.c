#include <stdio.h>

typedef struct Object {
    int profit;
    int weight;
} object;

object arr[10];

void knapsack10(int m);
void print2D(int a[][], int size, int m);

void main() {
    int size;
    int m;
    printf("Enter number of elements (less than 10): ");
    scanf("%d", &size);
    
    for (int i = 0; i < size; i++) {
        printf("Enter profit of %d element: ", i + 1);
        scanf("%d", &arr[i].profit);
        
        printf("Enter weight of %d element: ", i + 1);
        scanf("%d", &arr[i].weight);
        
        printf("\n");
    }
    
    printf("\n+------------+------------+------------+\n");
    printf("| Element No.|   Profit   |   Weight   |\n");
    printf("+------------+------------+------------+\n");

    for (int i = 0; i < size; i++) {
        printf("| %-10d | %-10d | %-10d |\n", i + 1, arr[i].profit, arr[i].weight);
    }
    
    printf("Enter the capacity of sack: ");
    scanf("%d", &m);

    printf("+------------+------------+------------+\n");
    
    knapsack10(size, m);
}

void knapsack10(int size, int m) {
    
    int DP[size + 1][m + 1] = {0};
    char keep[size + 1][m + 1] = {'X'};
    
    
    print2D(DP, size, m);
    print2D(keep, size, m);
}

void print2D(int a[][], size, m) {
    for (int i = 0; i < size; i++) {
        printf("+------------+------------+------------+\n");
        for (int j = 0; j < m; j++) {
            printf("| %-4d |", a[i][j]);
        }
        printf("+------------+------------+------------+\n");
    }
}







