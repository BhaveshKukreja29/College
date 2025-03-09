#include <stdio.h>

typedef struct {
    int id;
    int arrival;
    int priority;
    int burst;
    int wait;
    int turn;
} process;

process arr[10];
process output[10];

int main() {
    printf("Enter number of processes: ");
    int n;
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) {
        
        printf("For %d number process\n", i + 1);
        
        printf("Enter id: ");
        scanf("%d", &arr[i].id);
        
        printf("Enter arrival: ");
        scanf("%d", &arr[i].arrival);
        
        printf("Enter priority: ");
        scanf("%d", &arr[i].priority);
        
        printf("Enter burst time: ");
        scanf("%d", &arr[i].burst);
        
        printf("\n");
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
        int currentProcessIndex = -1;
        
        // figure out the process to select withh respect to arrival and Priority
        for (i = 0; i < n; i++) {
            if (minarrive >= arr[i].arrival && priority >= arr[i].priority && executed[i] != 1) {
                currentProcess = arr[i];
                priority = currentProcess.priority;
                currentProcessIndex = i;
            }
        }
        
        if (currentProcessIndex == -1) {
            timespent++;
            continue;
        }
        
        currentProcess.turn = timespent + currentProcess.burst - currentProcess.arrival;
        currentProcess.wait = timespent - currentProcess.arrival;

        timespent += currentProcess.burst;
        executed[currentProcessIndex] = 1;
        
        // store process in array for later use
        output[sizeExecuted] = currentProcess;
        sizeExecuted++;
        
    }
    
    printf("\nOutput Sequence with respect to ID: ");
    for (int i = 0; i < sizeExecuted; i++) {
        if (i == sizeExecuted - 1) printf(" %d", output[i].id);
        else printf("%d -->", output[i].id);
    }
    
    
    printf("\n\nSequence of execution with wait time and turnaround time");
    printf("\n+----------+----------+----------+\n");
    printf("|    ID    |Wait time |Turn time |\n");
    printf("+----------+----------+----------+\n");
    
    for (int i = 0; i < sizeExecuted; i++) {
        printf("|    %-6d|    %-6d|    %-6d|\n", output[i].id, output[i].wait, output[i].turn);
        printf("+----------+----------+----------+\n");
    }
    
    
    float aw = 0, at = 0;
    
    for (int i = 0; i < sizeExecuted; i++) {
        aw += output[i].wait;
        at += output[i].turn;
    }
    
    aw /= sizeExecuted;
    at /= sizeExecuted;
    
    printf("\nAverage Waiting Time: %.2f", aw);
    printf("\nAverage Turnaround Time: %.2f\n", at);

    
    return 0;
}
