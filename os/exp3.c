#include <stdio.h>

typedef struct {
    int id;
    int arrival;
    int priority;
    int burst;
} process;

process arr[10];
process output[10];

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
    int timespent = 0;
    int executed[] = {0,0,0,0,0,0,0,0,0,0};
    int sizeExecuted = 0;
    
    while (sizeExecuted != n) {
        int i;
        int minarrive = timespent;
        int priority = 1000; //took large value to avoid bugs by taking arr.priority[0]
        
        process currentProcess;
        int currentProcessIndex;
        
        // figure out the process to select withh respect to arrival and Priority
        for (i = 0; i < n; i++) {
            if (minarrive >= arr[i].arrival && priority >= arr[i].priority && executed[i] != 1) {
                currentProcess = arr[i];
                priority = currentProcess.priority;
                currentProcessIndex = i;
            }
        }

        timespent += currentProcess.burst;
        executed[currentProcessIndex] = 1;
        
        for (int j = 0; j < n; j++) {
            printf(" %d ", executed[j]);
        }
        printf("\n");
        
        // store process in array for later use
        output[sizeExecuted] = currentProcess;
        sizeExecuted++;
        
    }
    
    printf("Output\n\n");
    
    printf("\n+----------+----------+----------+----------+\n");
    printf("|    ID    | Arrival  | Priority |Burst time|\n");
    printf("+----------+----------+----------+----------+\n");
    
    for (int i = 0; i < sizeExecuted; i++) {
        printf("|    %-6d|    %-6d|    %-6d|    %-6d|\n", output[i].id, output[i].arrival, output[i].priority, output[i].burst);
        printf("+----------+----------+----------+----------+\n");
    }
    
    return 0;
}
