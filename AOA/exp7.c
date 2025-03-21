#include <stdio.h>

int D[100][100]; 
int P[100][100];

void floyd(int v);

void main() {
    int v;
    printf("Enter number of vertices: ");
    scanf("%d", &v);
    
    for (int i = 0; i < v; i++) {
        for (int j = 0; j < v; j++) {
            printf("Enter weight at edge(%d, %d) (Enter 1000 for infinity): ", i, j);
            scanf("%d", &D[i][j]);
            
            if (i != j && D[i][j] != 1000) {
                P[i][j] = i;  
            } else {
                P[i][j] = -1; 
            }
        }
    }
    
    floyd(v);
}

void floyd(int v) {
    for (int k = 0; k < v; k++) {
        for (int i = 0; i < v; i++) {
            for (int j = 0; j < v; j++) {
                if (D[i][j] > D[i][k] + D[k][j]) {
                    D[i][j] = D[i][k] + D[k][j];  
                    P[i][j] = P[k][j];  
                }
            }
        }
        
        printf("K = %d: \n", k);
        printf("Distance Matrix:\n");
        for (int i = 0; i < v; i++) {
            for (int j = 0; j < v; j++) {
                printf(" %-4d ", D[i][j]);
            }
            printf("\n");
        }

        printf("Predecessor Matrix:\n");
        for (int i = 0; i < v; i++) {
            for (int j = 0; j < v; j++) {
                printf(" %-4d ", P[i][j]);
            }
            printf("\n");
        }
    }
}
