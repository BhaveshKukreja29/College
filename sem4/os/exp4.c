#include <stdio.h>

int memory[100];
char status[100];
int process[100];

void bestfit(int size);
void worstfit(int size);
void firstfit(int size);

int main() {
    int size;
    printf("Enter amount of memory blocks: ");
    scanf("%d", &size);
    for (int i = 0; i < size; i++) {
        printf("Enter memory size: ");
        scanf("%d", &memory[i]);
        
        printf("Enter status: ");
        scanf("%s", &status[i]);
        
        printf("Enter process: ");
        scanf("%d", &process[i]);
    }
    
    printf("\n+------------+------------+------------+\n");
    printf("|   Memory   |   Status   |   Process  |\n");
    printf("+------------+------------+------------+\n");
    
    for (int i = 0; i < size; i++) {
        printf("|   %-3d KB   |     %c      |     %-2d     |\n", memory[i], status[i], process[i]);
    }
    
    printf("+------------+------------+------------+\n");
    
    firstfit(size);
    bestfit(size);
    worstfit(size);
    
    return 0;
}

void firstfit(int size) {
    int meminc, idinc;
    printf("First Fit\n");
    printf("Enter memory for incoming process: ");
    scanf("%d", &meminc);
    
    printf("Enter id for incoming process: ");
    scanf("%d", &idinc);
    
    int i;
    int temp;
    for (i = 0; i < size; i++) {
        if (memory[i] > meminc && status[i] == 'F') {
            temp = i;
            break;
        }
    }
    
    printf("\n+------------+------------+------------+\n");
    printf("|   Memory   |   Status   |   Process  |\n");
    printf("+------------+------------+------------+\n");
    
    for (i = 0; i < size; i++) {
        if (temp == i) {
            printf("|   %-3d KB   |     N      |     %-2d     |\n", meminc, idinc);
            printf("|   %-3d KB   |     F      |     -1     |\n", memory[i] - meminc);
        }
        else printf("|   %-3d KB   |     %c      |     %-2d     |\n", memory[i], status[i], process[i]);
    }
    
    printf("+------------+------------+------------+\n");
}

void bestfit(int size) {
    int meminc, idinc;
    printf("Best Fit\n");

    printf("Enter memory for incoming process: ");
    scanf("%d", &meminc);
    
    printf("Enter id for incoming process: ");
    scanf("%d", &idinc);
    
    int i;
    int minind;
    for (i = 0; i < size; i++) {
        if (memory[i] > meminc && memory[i] < memory[minind] && status[i] == 'F') {
            minind = i;
        }
    }
    
    printf("\n+------------+------------+------------+\n");
    printf("|   Memory   |   Status   |   Process  |\n");
    printf("+------------+------------+------------+\n");
    
    for (i = 0; i < size; i++) {
        if (minind == i) {
            printf("|   %-3d KB   |     N      |     %-2d     |\n", meminc, idinc);
            printf("|   %-3d KB   |     F      |     -1     |\n", memory[i] - meminc);
        }
        else printf("|   %-3d KB   |     %c      |     %-2d     |\n", memory[i], status[i], process[i]);
    }
    
    printf("+------------+------------+------------+\n");
}

void worstfit(int size) {
    printf("Worst Fit\n");

    int meminc, idinc;
    printf("Enter memory for incoming process: ");
    scanf("%d", &meminc);
    
    printf("Enter id for incoming process: ");
    scanf("%d", &idinc);
    
    int i;
    int minind;
    for (i = 0; i < size; i++) {
        if (memory[i] > meminc && memory[i] > memory[minind] && status[i] == 'F') {
            minind = i;
        }
    }
    
    printf("\n+------------+------------+------------+\n");
    printf("|   Memory   |   Status   |   Process  |\n");
    printf("+------------+------------+------------+\n");
    
    for (i = 0; i < size; i++) {
        if (minind == i) {
            printf("|   %-3d KB   |     N      |     %-2d     |\n", meminc, idinc);
            printf("|   %-3d KB   |     F      |     -1     |\n", memory[i] - meminc);
        }
        else printf("|   %-3d KB   |     %c      |     %-2d     |\n", memory[i], status[i], process[i]);
    }
    
    printf("+------------+------------+------------+\n");
}
