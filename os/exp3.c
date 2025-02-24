#include <stdio.h>

void bestfit();
void worstfit();
void firstfit();

int main() {
    int memory[100];
    char *status[100];
    char *process[100];
    
    int size;
    printf("Enter amount of memory blocks: ");
    scanf("%d", &size);
    for (int i = 0; i < size; i++) {
        printf("Enter memory size: ");
        scanf("%d", &memory[i]);
        
        printf("Enter status: ");
        scanf("%s", &status[i]);
        
        printf("Enter process: ");
        scanf("%s", &process[i]);
    }
    
    printf("\n+------------+------------+------------+\n");
    printf("|   Memory   |   Status   |   Process  |\n");
    printf("+------------+------------+------------+\n");
    
    printf("loop");
    for (int i = 0; i < size; i++) {
        printf("sdf");
        printf("| %-10d KB| %-10s | %-10s |\n", memory[i], status[i], process[i]);
    }
    
    return 0;
}
