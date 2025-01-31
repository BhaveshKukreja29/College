#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100

#define UP '^'
#define LEFT '<'
#define DIAGONAL '\'

void printLCS(char direction[MAX][MAX], char *X, int i, int j) {
    if (i == 0 || j == 0) {
        return;
    }
    if (direction[i][j] == DIAGONAL) {
        printLCS(direction, X, i - 1, j - 1);
        printf("%c", X[i - 1]);
    } else if (direction[i][j] == UP) {
        printLCS(direction, X, i - 1, j);
    } else {
        printLCS(direction, X, i, j - 1);
    }
}

void printarray(char arr[MAX][MAX], int m, int n) {
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            printf("%c ", arr[i][j]);
        }
        printf("\n");
    }
}

void LCS(char *X, char *Y, int m, int n) {
    int dp[MAX][MAX] = {0};
    char direction[MAX][MAX] = {0};


    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (X[i - 1] == Y[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
                direction[i][j] = DIAGONAL; 
            } else if (dp[i - 1][j] >= dp[i][j - 1]) {
                dp[i][j] = dp[i - 1][j];
                direction[i][j] = UP; 
            } else {
                dp[i][j] = dp[i][j - 1];
                direction[i][j] = LEFT; 
            }
        }
    }

    printf("DP Table:\n");
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            printf("%d ", dp[i][j]);
        }
        printf("\n");
    }

    printf("\nDirection Table:\n");
    printarray(direction, m, n);

    printf("\nLongest Common Subsequence: ");
    printLCS(direction, X, m, n);
    printf("\n");
}

int main() {
    char X[MAX], Y[MAX];

    printf("Enter the first string: ");
    scanf("%s", X);
    printf("Enter the second string: ");
    scanf("%s", Y);

    int m = strlen(X);
    int n = strlen(Y);

    LCS(X, Y, m, n);

    return 0;
}
