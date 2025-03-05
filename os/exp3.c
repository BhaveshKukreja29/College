#include <stdio.h>

typedef struct {
    int id;
    int arrival;
    int priority;
    int burst;
} process;

process arr[10];
int output[10];

int main() {
    printf("Enter number of processes: ");
    int n;
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) {
        printf("Enter id: ");
        scanf("%d", &arr[i].id);
        
        printf("Enter arrival: ");
        scanf("%d", &arr[i].arrival);
        
        printf("Enter priority: ");
        scanf("%d", &arr[i].priority);
        
        printf("Enter burst time: ");
        scanf("%d", &arr[i].burst);
    }
    
    printf("\n+----------+----------+----------+----------+\n");
    printf("|    ID    | Arrival  | Priority |Burst time|\n");
    printf("+----------+----------+----------+----------+\n");
    
    for (int i = 0; i < n; i++) {
        printf("|    %-6d|    %-6d|    %-6d|    %-6d|\n", arr[i].id, arr[i].arrival, arr[i].priority, arr[i].burst);
        printf("+----------+----------+----------+----------+\n");
    }
    
    //non pre emptive scheduling
    
    // for arrival i
    // get highest priority available after that time
    // execute that, add in table, increment the time spent, we can add in array
    // check for more on time after that.
    
    // get first arrival
    int timespent;
    int minarrive = 0;
    int i = 0;
    while (i < n) {
        for (int j = 0; j < n; j++) {
            if (minarrive > arr[i].arrival) {
                minarrive = arr[i].arrival
            }
        }
        i++;
    }
    return 0;
}
