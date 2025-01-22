#include <stdio.h>

int main(){
    int arr[100];
    int size, i, j;
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
    
    for (i = 1; i < size; i ++){
        int temp = arr[i];
        j = i - 1;
        
        while (j >= 0 && arr[j] > temp) {
            arr[j + 1] = arr[j];
            j--;
        }
        
        arr[j + 1] = temp;
    }
    
    printf("\nSorted array: ");
    
    for (i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
