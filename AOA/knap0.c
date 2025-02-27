#include <stdio.h>

typedef struct Object {
    int profit;
    int weight;
} object;

object arr[10];

void knapsack10(int size, int m);
void print2D(int a[][10], int size, int m);
void printchar2D(char a[][10], int size, int m);

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
    printf("+------------+------------+------------+\n\n");
    
    printf("Enter the capacity of sack: ");
    scanf("%d", &m);
    
    knapsack10(size, m);
}

void knapsack10(int size, int m) {
    
    int DP[size + 1][m + 1];
    char keep[size + 1][m + 1];
    
    for (int i = 0; i <= size; i++) {
        for (int j = 0; j <= m; j++) {
            DP[i][j] = 0;
        }
    }
    
    for (int i = 0; i <= size; i++) {
        for (int j = 0; j <= m; j++) {
            keep[i][j] = '-';
        }
    }
    
    for (int i = 1; i <= size; i++) {
        for (int j = 1; j <= m; j++) {
            if (arr[i - 1].weight <= j) {
                if (arr[i - 1].profit + DP[i - 1][j - arr[i - 1].weight] > DP[i - 1][j]) {
                    DP[i][j] = arr[i - 1].profit + DP[i - 1][j - arr[i - 1].weight];
                    keep[i][j] = '^';
                }
                
                else {
                    DP[i][j] = DP[i - 1][j];
                    keep[i][j] = 'x';
                }
            }
            
            else {
                DP[i][j] = DP[i - 1][j]; 
                keep[i][j] = 'x';
            }
        }
        
       for (int j = 0; j <= m; j++) {
           printf("Index %d and %d: %d\n", i, j, DP[i][j]);
       }
    }
    
    printf("\nKnapsack table\n");
    printf("+---------------------------------------------------------+\n");
    for (int i = 0; i <= size; i++) {
        for (int j = 0; j <= m; j++) {
            printf("| %-2d |", DP[i][j]);
        }
        printf("\n");
    }    
    printf("+---------------------------------------------------------+\n");
    
    printf("\n");
    printf("\nKeep table\n");
    printf("+---------------------------------------------------------+\n");
    for (int i = 0; i <= size; i++) {
        for (int j = 0; j <= m; j++) {
            printf("| %-2c |", keep[i][j]);
        }
        printf("\n");
    }
    printf("+---------------------------------------------------------+\n"); 
}
