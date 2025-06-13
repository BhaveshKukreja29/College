#include <stdio.h>

int main(){
    int arr[100];
    int size, i, j, k;
    printf("Enter array size: ");
    scanf("%d", &size);
    
    for (i = 0; i < size; i++) {
        printf("Enter element %d: ", i + 1);
        scanf("%d", &arr[i]);
    }
    
    printf("Original array: ");
    
    for (i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    for (i = 1; i < size; i ++){
        int temp = arr[i];
        j = i - 1;
        
        while (j >= 0 && arr[j] > temp) {
            arr[j + 1] = arr[j];
            j--;
        }
        
        arr[j + 1] = temp;
        
        printf("For pass %d: ", i);
        for (k = 0; k < size; k++) {
            printf("%d ", arr[k]);
        }
        printf("\n");
    }
    
    printf("\nSorted array: ");
    
    for (i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
