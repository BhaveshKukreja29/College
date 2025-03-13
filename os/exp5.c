// Write a program to simulate LRU page replacement techniques
// we will replace the one that was used long time ago

//take input of frames
// take string of requests

// each page is a struct with attributes as time spent in memory
// frames is a struct array containing the element 

// have an output array of string showing hit or miss

// algorithm is to iterate over each frame element and check which element is in it.
// if there is no element matching to our request we swap the one with most time spent in memory
// after swap we have to keep the new time spent as 0

// after every request, we will increment the time spent of every process

// queue use kar to make O(n)

#include <stdio.h>

typedef struct {
    char page;
    int timespent;
} frame;

int main() {
    int n;
    printf("Enter the number of frames: ");
    scanf("%d", &n);
    
    frame frames[n];
    
    for (int i = 0; i < n; i++) {
        frames[i].page = '-';
        frames[i].timespent = 0;
    }
    
    char req[50];
    printf("Enter the string of requests: ");
    scanf("%s", req);
    
    int count;
    for (int i = 0; req[i] != '\0'; i++) {
        count += 1;
    }
    
    char output[count];
    
    printf("Frame condition at each step: \n");
    for (int i = 0; req[i] != '\0'; i++) {
        int temp = 0;
        for (int j = 0; j < n; j++) {
            if (req[i] == frames[j].page) {
                temp = 1;
                break;
            }
        }
        
        if (temp == 1) output[i] = 'H';
        
        else {
            output[i] = 'M';
            int max = -1;
            int ind;
            
            for (int j = 0; j < n; j++) {
                if (frames[j].page == '-') {
                    ind = j;
                    break;
                }
                else if (max < frames[j].timespent) {
                    max = frames[j].timespent;
                    ind = j;
                }
            }
            
            frames[ind].page = req[i];
            frames[ind].timespent = 0;
        }
        
        
        for (int j = 0; j < n; j++) {
            printf("| F%d |", j + 1);
            printf(" %c |\n", frames[j].page);
        }
        
        
        printf("\n");
        
        for (int j = 0; j < n; j++) {
            frames[j].timespent += 1;
        }
    }
    
    for (int i = 0; req[i] != '\0'; i++) {
        printf("%c ", output[i]);
    }
    
    
    
    return 0;
}
