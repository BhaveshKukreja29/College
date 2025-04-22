#include <stdio.h>

typedef struct {
    int id;
    int burst;
}proc;

proc p[100];

int main()
{
    int n;
    printf("Enter number of processes: ");
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) 
    {
        printf("Enter id: ");
        scanf("%d", &p[i].id);
        
        printf("Enter burst time: ");
        scanf("%d", & p[i].burst);
        
        printf("\n");
    }
    printf("\n");
    
    //fcfs
    int wait[n];
    int turn[n];
    
    wait[0] = 0;
    turn[0] = p[0].burst;
    
    for (int i = 1; i < n; i++) 
    {
        wait[i] = turn[i - 1];
        turn[i] = wait[i] + p[i].burst;
    }
    
    printf("Wait and turn around time for each process\n");
    for (int i = 0; i < n; i++)
    {
        printf("For process %d\nWait time: %d   Turn around time: %d\n\n", i + 1, wait[i], turn[i]);
    }
    
    float avgwait = 0;
    float avgturn = 0;
    
    for (int i = 0; i < n; i++)
    {
        avgwait += wait[i];
        avgturn += turn[i];
    }
    
    
    printf("Average wait time: %.2f, Average turn around time: %.2f", avgwait / n, avgturn / n);
    
    return 0;
}
