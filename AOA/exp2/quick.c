#include <stdio.h>

int arr[100];
int size;

void quick(int low, int high);
int partition(int low, int high);

int main() {
	int i;
	printf("Enter size of array: ");
	scanf("%d", &size);
	
	for (i = 0; i < size; i++) {
		printf("Enter element no. %d: ", i + 1);
		scanf("%d", &arr[i]);
	}
	
	printf("\n");
	printf("Original array: ");
	for (i = 0; i < size; i++) {
		printf(" %d ", arr[i]);
	} 
	printf("\n");
	quick(0, size - 1);
	
	printf("\n");
	printf("Sorted array: ");
	for (i = 0; i < size; i++) {
		printf(" %d ", arr[i]);
	}
		
	return 0;
}

void quick(int low, int high) {
	if (low < high) {
		int q = partition(low, high);
		quick(low, q - 1);
		quick(q + 1, high);
	}
}

int partition(int low, int high) {
	int p = arr[low];
	int i = low;
	int j;
	
	for(j = i + 1; j <= high; j++) {
		if (arr[j] < p) {
			i = i + 1;
			int temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
		}
	}
	
	int temp = arr[p];
	arr[p] = arr[i];
	arr[i] = temp;
	
	return i;
}
