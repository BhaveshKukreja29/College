#include <stdio.h>
#include <string.h>

#define MAX 100

char text[MAX], pattern[MAX];
int lps[MAX];
int n, m;

void computeLPS();
void kmp();

int main() 
{
    printf("Enter the text: ");
    scanf("%s", text);
    
    printf("Enter the pattern: ");
    scanf("%s", pattern);
    
    n = strlen(text);
    m = strlen(pattern);
    
    computeLPS();
    kmp();
    
    return 0;    
}

void computeLPS()
{
    int len = 0;
    lps[0] = 0;
    
    int i = 1;
    
    while (i < m)
    {
        if (pattern[i] == pattern[len]) 
        {
            len++;
            lps[i] = len;
            i++;
        }
        else
        {
            if (len != 0) 
            {
                len = lps[len - 1];
            }
            else
            {
                lps[i] = 0;
                i++;
            }
        }
    }
}

void kmp()
{
    int i = 0;
    int j = 0;
    
    printf("\nPattern found at following indexes:\n\n");
    
    while (i < n)
    {
        if (text[i] == pattern[j]) 
        {
            i++;
            j++;
        }
        
        if (j == m) 
        {
            printf("%d\n", i - j);
            j = lps[j - 1];
        }
        else if (i < n && text[i] != pattern[j])
        {
            if (j != 0)
            {
                j = lps[j - 1];
            }
            else
            {
                i++;
            }
        }
    }
}
