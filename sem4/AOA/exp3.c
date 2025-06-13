#include <stdio.h>

#define INF 10000

int v;
void prims();
void printPrims();
void getNeighbour(int src);
int minEdge(); 

int D[100][100];  
int visited[100];  
int parent[100];   
int key[100];      

void main() {
    printf("Enter number of vertices: ");
    scanf("%d", &v);

    for (int i = 0; i < v; i++) {
        for (int j = 0; j < v; j++) {
            printf("Enter weight at edge(%d, %d) (Enter 10000 for infinity): ", i, j);
            scanf("%d", &D[i][j]);
        }
    }

    for (int i = 0; i < v; i++) {
        visited[i] = 0; 
        key[i] = INF;   
        parent[i] = -1; 
    }

    key[0] = 0; 
    prims();
    printPrims();
}

void prims() {
    for (int count = 0; count < v - 1; count++) {
        int u = minEdge(); 
        visited[u] = 1; 

        for (int i = 0; i < v; i++) {
            if (visited[i] == 0 && D[u][i] != INF && D[u][i] < key[i]) {
                key[i] = D[u][i]; 
                parent[i] = u;     
            }
        }
    }
}

int minEdge() {
    int min = INF, min_index;

    for (int i = 0; i < v; i++) {
        if (visited[i] == 0 && key[i] < min) {
            min = key[i];
            min_index = i;
        }
    }
    return min_index;
}

void printPrims() {
    printf("Edge   Weight\n");
    for (int i = 1; i < v; i++) {
        printf("%d - %d   %d\n", parent[i], i, D[parent[i]][i]);
    }
}
