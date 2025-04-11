#include <stdio.h>

#define MAX 100

int count = 0;

int n, target, total = 0;
int w[MAX], x[MAX];

int sumOfSubset(int i, int weight, int total);
int isOk(int i, int weight, int total);

int main() {
    //take input
    printf("Enter number of elements: ");
    scanf("%d", &n);
    
    printf("Enter elements in increasing order\n");
    
    for (int i = 0; i < n; i++) {
        scanf("%d", &w[i]);
    }
    
    printf("Enter target sum: ");
    scanf("%d", &target);
    
    for (int i = 0; i < n; i++) {
        total += w[i];
    }
    
    printf("The possible answers for target %d are: \n", target);
    
    sumOfSubset(0, 0, total);
    
    printf("\nTotal Nodes: %d", count);
    return 0;
}

int sumOfSubset(int i, int weight, int total) {
    count += 1;
    
    if (isOk(i, weight, total)) {
        if (weight == target) {
            for (int j = 0; j < n; j++) {
                if (x[j]) {
                    printf("%d ", w[j]);
                }
            }
            printf("\n");
        } else {
            x[i] = 1;
            sumOfSubset(i + 1, weight + w[i], total - w[i]);
            x[i] = 0;
            sumOfSubset(i + 1, weight, total - w[i]);
        }
    }
}

int isOk(int i, int weight, int total) {
    return ((weight + total >= target) && (weight == target || weight + w[i] <= target));
}
