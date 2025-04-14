#include <stdio.h>

#define MAX 100

int size;
int capacity[MAX][MAX];
int remain[MAX][MAX];
int visited[MAX];
int parent[MAX];

int dfs(int s, int v);
int fordfulkerson(int src, int sink);

int main() 
{
    int src, sink;
    
    printf("Enter the number of vertices: ");
    scanf("%d", &size);
    
    for (int i = 0; i < size; i++) 
    {
        for (int j = 0; j < size; j++) 
        {
            printf("Capacity of (%d, %d): ", i, j);
            scanf("%d", &capacity[i][j]);
            remain[i][j] = capacity[i][j];
        }
    }
    
    printf("Enter source: ");
    scanf("%d", &src);
    
    printf("Enter sink: ");
    scanf("%d", &sink);

    if (src >= size || sink >= size || src < 0 || sink < 0) 
    {
        printf("Invalid source or sink. Exiting...\n");
        return 1;
    }

    else if (src == sink)
    {
        printf("Source and sink is the same vertex.\n\nTotal Flow is: 0\n");
    }
    else
    {
        int totalFlow = fordfulkerson(src, sink);
        
        printf("Total Flow is: %d\n", totalFlow);
    }
    return 0;
}

int fordfulkerson(int src, int sink)
{
    int totalFlow = 0;

    for (int i = 0; i < size; i++) 
    {
        visited[i] = 0;
        parent[i] = -1;
    }

    int pathExist = dfs(src, sink);
    
    while(pathExist) 
    {
        //find bottleneck
        //to find bottleneck, we must compare capacity of path starting from sink
        int currentParent = parent[sink];
        int currentChild = sink;
        int bottleneck = remain[currentParent][currentChild];

        if (currentParent == -1)
        {
            break;
        }
        
        while(currentParent != -1) 
        {
            if (bottleneck > remain[currentParent][currentChild]) 
            {
                bottleneck = remain[currentParent][currentChild];
            }
            currentChild = currentParent;
            currentParent = parent[currentParent];
        }

        //Initially I forgot these two lines which caused an infinity loop
        currentChild = sink;
        currentParent = parent[sink];

        //add total_flow with bottleneck
        totalFlow += bottleneck;
        
        //update remain matrix by [u][v] -= bottleneck and [v][u] += bottleneck
        while(currentParent != -1) 
        {
            remain[currentParent][currentChild] -= bottleneck;
            remain[currentChild][currentParent] += bottleneck;
            
            currentChild = currentParent;
            currentParent = parent[currentParent];
        }
        
        //clear history
        for (int i = 0; i < size; i++) 
        {
            visited[i] = 0;
            parent[i] = -1;
        }

        //dfs again
        pathExist = dfs(src, sink);
    }

    return totalFlow;
}

int dfs(int s, int v) 
{
    //this dfs avoids already visited paths since we're using remain matrix.
    visited[s] = 1;
    if (s == v) 
    {
        return 1;
    } 
    else 
    {
        for (int i = 0; i < size; i++) 
        {
            if (!visited[i] && remain[s][i] > 0)
            {
                parent[i] = s;
                if (dfs(i, v)) 
                {
                    return 1;
                }
            }
        }
        
        return 0;
    }
}
