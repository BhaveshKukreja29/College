#include <stdio.h>

int size;
int arr[100];
int brr[100];
int pass = 1;

void mergesort(int low, int high);
void merge(int low, int mid, int high);

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
	mergesort(0, size - 1);
	
	printf("\n");
	printf("Sorted array: ");
	for (i = 0; i < size; i++) {
		printf(" %d ", brr[i]);
	}
		
	return 0;
}

void mergesort(int low, int high) {
	if (low < high) {
		int mid = (high + low) / 2;
		
		mergesort(low, mid);
		mergesort(mid + 1, high);
		
		merge(low, mid, high);
	}
}
void merge(int low, int mid, int high) {
	int l = low;
	int r = mid + 1;
	
	int i = low;
	while (l <= mid && r <= high) {
		if (arr[l] < arr[r]) {
			brr[i++] = arr[l++];
		} else {
			brr[i++] = arr[r++];
		}
	}
	
	while (l <= mid) {
		brr[i++] = arr[l++];
	}
	
	while (r <= high) {
		brr[i++] = arr[r++];
	}
	
	int j = low;
	while (j <= high) {
		arr[j] = brr[j];
		j++;
	}
	
	
	j = 0;
	printf("Pass %d: ", pass++);
	while (j < size) {
		printf(" %d ", arr[j++]);
	}
	printf("\n");
}
