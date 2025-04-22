#include <stdio.h>

typedef struct {
    int id;
    int burst;
}proc;

proc p[100];

int main()
{
    int quantum = 4;
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
    
    //round robin
    int wait[n];
    int turn[n];
    
    int rmbt[n];
    for (int i = 0; i < n; i++)
    {
        rmbt[i] = p[i].burst;  // Remaining burst time
    }

    int t = 0;
    while(1)
    {
        int done = 1;
        for (int i = 0; i < n; i++)
        {
            if (rmbt[i] > 0)
            {
                done = 0;
                if (rmbt[i] > quantum)
                {
                    rmbt[i] -= quantum;
                    t += quantum;
                }
                else
                {
                    t += rmbt[i];
                    wait[i] = t - p[i].burst;
                    rmbt[i] = 0;
                }
            }
        }
        if (done)
        {
            break;
        }
    }
    
    for (int i = 0; i < n; i++) 
    {
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
