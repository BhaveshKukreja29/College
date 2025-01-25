#include <stdio.h>

int main(){
    int arr[100];
    int size, i, j, k;
    
    int min;
    int counter = 0, temp = 0, min_ind = 0;
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
    printf("\n\n");
    
    do{
        
        min = arr[counter];
        min_ind = counter;
        
        for (i = counter; i < size; i++) {
            if (min > arr[i]) {
                min = arr[i];
                min_ind = i;
            }
        }
        
        temp = arr[counter];
        arr[counter] = arr[min_ind];
        arr[min_ind] = temp;
        
        counter++;
        
        printf("For pass %d: ", counter);
        for (k = 0; k < size; k++) {
            printf("%d ", arr[k]);
        }
        printf("\n");
    }while(counter < size);
    
    printf("\nSorted array: ");
    
    for (i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
