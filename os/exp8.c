//take input array of locations with requests
// take start position 
// take direction, then go in reverse

#include <stdio.h>
#include <stdlib.h>

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

    int sub = 0;
    printf("\n");
    for (int i = 0; i < n; i++) {
        printf("Enter the track number: ");
        scanf("%d", &arr[i]);
        if (arr[i] < 0 || arr[i] >= range) {
            printf("\n%d is out of range.\n", arr[i]);
            arr[i] = -1; 
            sub++;
        }
    }
    
    int head;
    printf("Enter the starting location: ");
    scanf("%d", &head);

    char dir;
    printf("Enter direction (L for left, R for right): ");
    scanf(" %c", &dir);

    int valid[100];
    int k = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] != -1) {
            valid[k++] = arr[i];
        }
    }

    valid[k++] = head; 
    if (dir == 'R' || dir == 'r') {
        valid[k++] = range - 1;
    } else {
        valid[k++] = 0;
    }

    for (int i = 0; i < k; i++) arr[i] = valid[i];
    mergesort(0, k - 1);

    int idx = -1;
    for (int i = 0; i < k; i++) {
        if (arr[i] == head) {
            idx = i;
            break;
        }
    }

    int total = 0;
    int prev = head;

    printf("Seek Sequence:\n");

    if (dir == 'R' || dir == 'r') {
        //move right first
        for (int i = idx + 1; i < k; i++) {
            total += abs(arr[i] - prev);
            printf("%d -> ", arr[i]);
            prev = arr[i];
        }
        //then left
        for (int i = idx - 1; i >= 0; i--) {
            total += abs(arr[i] - prev);
            printf("%d -> ", arr[i]);
            prev = arr[i];
        }
    } else {
        //move left first
        for (int i = idx - 1; i >= 0; i--) {
            total += abs(arr[i] - prev);
            printf("%d -> ", arr[i]);
            prev = arr[i];
        }
	//then right
        for (int i = idx + 1; i < k; i++) {
            total += abs(arr[i] - prev);
            printf("%d -> ", arr[i]);
            prev = arr[i];
        }
    }

    printf("END\n");
    printf("Total seek time: %d\n", total);
    printf("Average seek time: %.2f\n", (float)total / (n - sub));

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
	
	for (int j = low; j <= high; j++) {
		arr[j] = brr[j];
	}
}
