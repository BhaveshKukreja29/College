#include <stdio.h>
#include <stdlib.h>

void mergesort(int low, int high);
void merge(int low, int mid, int high);

int arr[100];
int brr[100];

int main() {
    int n;
    printf("Enter number of requests: ");
    scanf("%d", &n);

    printf("\nEnter the track requests: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int head;
    printf("Enter the starting location: ");
    scanf("%d", &head);

    char direction;
    printf("Enter direction (L for left, R for right): ");
    scanf(" %c", &direction);

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

    int temp, total = 0, prev = head;
    printf("Seek sequence: %d", head);

    if (direction == 'R' || direction == 'r') {
        //move right till last
        temp = idx;
        while (temp < n) {
            total += abs(arr[temp] - prev);
            printf(" -> %d", arr[temp]);
            prev = arr[temp];
            temp++;
        }

        //left until first
        temp = idx - 1;
        while (temp >= 0) {
            total += abs(arr[temp] - prev);
            printf(" -> %d", arr[temp]);
            prev = arr[temp];
            temp--;
        }
    } else {
        //left till first
        temp = idx - 1;
        while (temp >= 0) {
            total += abs(arr[temp] - prev);
            printf(" -> %d", arr[temp]);
            prev = arr[temp];
            temp--;
        }

        //right till last
        temp = idx;
        while (temp < n) {
            total += abs(arr[temp] - prev);
            printf(" -> %d", arr[temp]);
            prev = arr[temp];
            temp++;
        }
    }

    printf("\nTotal seek time: %d\n", total);
    
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
    int l = low, r = mid + 1, i = low;

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
