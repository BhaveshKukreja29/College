#include <stdio.h>
#include <stdlib.h>

void mergesort(int low, int high);
void merge(int low, int mid, int high);

int arr[100];
int brr[100];

int main() {
    int n, range;
    printf("Enter the available number of tracks: ");
    scanf("%d", &range);

    printf("Enter number of requests: ");
    scanf("%d", &n);

    int sub = 0;
    printf("\nEnter the track requests:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] < 0 || arr[i] >= range) {
            printf("%d is out of range.\n", arr[i]);
            arr[i] = -1;
            sub++;
        }
    }

    int head;
    printf("Enter the starting location: ");
    scanf("%d", &head);

    char direction;
    printf("Enter direction (L for left, R for right): ");
    scanf(" %c", &direction);

    int valid[100];
    int k = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] != -1) {
            valid[k++] = arr[i];
        }
    }

    valid[k++] = head;
    for (int i = 0; i < k; i++) arr[i] = valid[i];

    mergesort(0, k - 1);

    int idx = -1;
    for (int i = 0; i < k; i++) {
        if (arr[i] == head) {
            idx = i;
            break;
        }
    }

    int temp, total = 0, prev = head;
    printf("Seek sequence:\n%d", head);

    if (direction == 'R' || direction == 'r') {
        //move right until last request
        temp = idx + 1;
        while (temp < k) {
            total += abs(arr[temp] - prev);
            printf(" -> %d", arr[temp]);
            prev = arr[temp];
            temp++;
        }

        //move left until first request
        temp = idx - 1;
        while (temp >= 0) {
            total += abs(arr[temp] - prev);
            printf(" -> %d", arr[temp]);
            prev = arr[temp];
            temp--;
        }
    } else {
        //move left until first request
        temp = idx - 1;
        while (temp >= 0) {
            total += abs(arr[temp] - prev);
            printf(" -> %d", arr[temp]);
            prev = arr[temp];
            temp--;
        }

        //move right until last request
        temp = idx + 1;
        while (temp < k) {
            total += abs(arr[temp] - prev);
            printf(" -> %d", arr[temp]);
            prev = arr[temp];
            temp++;
        }
    }

    printf("\nTotal seek time: %d\n", total);
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
