#include <stdio.h>

int main()
{
    char buff[5];

    printf("My stack looks like:\n%p\n%p\n%p\n%p\n%p\n%p\n%p\n%p\n%p\n%p\n");

    buff[5] = 'A';  /* Out-of-bounds write — buffer overflow */

    printf("%c\n", buff[5]);

    printf("My new stack looks like:\n%p\n%p\n%p\n%p\n%p\n%p\n%p\n%p\n%p\n%p\n");

    return 0;
}
