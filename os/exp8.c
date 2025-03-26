//take input array of locations with requests
// take start position 
// take direction, then go in reverse

#include <stdio.h>
#include <stdlib.h>

#include <stdio.h>

int size;

void mergesort(int low, int high);
void merge(int low, int mid, int high);

int arr[100];
int brr[100];

int main(){
    int n;
    int range;
    printf("Enter the available number of tracks: ");
    scanf("%d", &range);
    
    printf("Enter number of requests: ");
    scanf("%d", &n);

    printf("\n");
    for (int i = 0; i < n; i++) {
        printf("Enter the track number: ");
        scanf("%d", &arr[i]);
    }
    
    int head;
    printf("Enter the starting location: ");
    scanf("%d", &head);
    
    mergesort(0, n - 1);
    
    int idx = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] >= head) {
            idx = i;
            break;
        }
    }
    if (idx == -1) {
        idx = n - 1;
    }
    
    int temp = idx;
    int total = 0;
    int prev = head;
    printf("%d", arr[temp++]);
    
    while (temp != n) {
        total += abs(arr[temp] - prev);
        printf("-> %d ", arr[temp]);
        prev = arr[temp];
        temp++;
    }
    
    temp = idx - 1;
    while (temp >= 0) {
        total += abs(arr[temp] - prev);
        printf("-> %d ", arr[temp]);
        prev = arr[temp];
        temp--;
    }
    
    printf("\nTotal seek time: %d", total);
    printf("\nAverage seek time: %.2f", (float)total / n);
    
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
}
