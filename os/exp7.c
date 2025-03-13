//take input array of locations with requests
// take start position 
// find the minimum distance for first, mark it as visited

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int val;
    int visited;
} track;

int main(){
    int n;
    printf("Enter number of requests: ");
    scanf("%d", &n);
    
    track arr[n];

    
    for (int i = 0; i < n; i++) {
        printf("Enter the track number: ");
        scanf("%d", &arr[i].val);
        
        arr[i].visited = 0;
    }
    
    int head;
    printf("Enter the starting location: ");
    scanf("%d", &head);
    
    int output[n];
    
    for (int i = 0; i < n; i++) {
        int min = 10000;
        int temp = -1;
        int ind = -1;
        for (int j = 0; j < n; j++) {
            if ((arr[j].visited == 0) && (min > abs(arr[j].val - head))) {
                min = abs(arr[j].val - head);
                ind = j;
                temp = arr[j].val;
            }
        }
        
        arr[ind].visited = 1;
        head = temp;
        
        output[i] = temp;
    }
    
    for (int j = 0; j < n; j++) {
        printf(" %d ", output[j]);
        
    }
    
    return 0;
}
