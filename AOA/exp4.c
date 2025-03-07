#include <stdio.h>

//Set initial distances for all vertices: 0 for the source vertex, and infinity for all the other.
//Choose the unvisited vertex with the shortest distance from the start to be the current vertex.
//So the algorithm will always start with the source as the current vertex.
//For each of the current vertex's unvisited neighbor vertices, calculate the distance from the source and update the distance 
//if the new, calculated, distance is lower.
//We are now done with the current vertex, so we mark it as visited. A visited vertex is not checked again.
//Go back to step 2 to choose a new current vertex, and keep repeating these steps until all vertices are visited.
//In the end we are left with the shortest path from the source vertex to every other vertex in the graph.

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

void dijkstra(src);

int main()
{
    printf("Enter number of edges: ");
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("Enter weight for edge (%d, %d): ", i, j);
            scanf("%d", &adj[i][j]);
        }
    }
    
    printf("Adjacency matrix\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf(" %-4d ", adj[i][j]);
        }
        printf("\n");
    }
    
    printf("Available vertices\n");
    for (int i = 0; i < n; i++) {
        printf(" %d ", i);
    }
    
    int src;
    printf("\nEnter source vertex: ");
    scanf("%d", &src);
    
    if (src >= n) {
        printf("Error, vertex doesn't exist.\n");
        return 0;
    }
    
    dijkstra(src);
    
    return 0;
}

void dijkstra(src) {
    arr[src].visited = 1;
    arr[src].parent = NILL;
    arr[src].costFromSource = 0;
    
    for (int i = 0; i < n; i++) {
        if (i != src) {
            arr[i].visited = 0;
            arr[i].parent = NILL;
            arr[i].costFromSource = INFINITY;
        }
    }
    
    
    
}

















