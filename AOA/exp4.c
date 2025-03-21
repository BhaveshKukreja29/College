#include <stdio.h>

#define INFINITY 10000
#define NILL -10000

typedef struct {
    int parent;
    int visited;
    int costFromSource;
} node;

int n;
node arr[20];
int adj[20][20];

void dijkstra(int src);
int findMinVertex();

int main()
{
    printf("Enter number of vertices: ");
    scanf("%d", &n);
    
    printf("Enter adjacency matrix (use %d for no direct path):\n", INFINITY);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &adj[i][j]);
        }
    }
    
    printf("Adjacency matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf(" %-4d ", adj[i][j]);
        }
        printf("\n");
    }
    
    int src;
    printf("Enter source vertex: ");
    scanf("%d", &src);
    
    if (src >= n || src < 0) {
        printf("Error: vertex doesn't exist.\n");
        return 0;
    }
    
    dijkstra(src);
    
    printf("\nShortest distances from vertex %d:\n", src);
    for (int i = 0; i < n; i++) {
        if (arr[i].costFromSource == 1000) {
            printf("To %d: %s\n", i, "infinity");
            break;
        }
        printf("To %d: %d\n", i, arr[i].costFromSource);
    }
    
    return 0;
}

void dijkstra(int src) {
    for (int i = 0; i < n; i++) {
        arr[i].visited = 0;
        arr[i].parent = NILL;
        arr[i].costFromSource = INFINITY;
    }
    
    arr[src].costFromSource = 0;
    
    for (int i = 0; i < n; i++) {
        int current = findMinVertex();
        if (current == -1) break;
        
        arr[current].visited = 1;
        
        for (int neighbor = 0; neighbor < n; neighbor++) {
            if (!arr[neighbor].visited && adj[current][neighbor] != INFINITY) {
                int newDist = arr[current].costFromSource + adj[current][neighbor];
                if (newDist < arr[neighbor].costFromSource) {
                    arr[neighbor].costFromSource = newDist;
                    arr[neighbor].parent = current;
                }
            }
        }
    }
}

int findMinVertex() {
    int min = INFINITY, minIndex = -1;
    for (int i = 0; i < n; i++) {
        if (!arr[i].visited && arr[i].costFromSource < min) {
            min = arr[i].costFromSource;
            minIndex = i;
        }
    }
    return minIndex;
}
