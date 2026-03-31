#include <stdio.h>
#include <string.h>

char password[] = "password";

int get_password()
{
    int auth_ok = 0;
    char buff[16];

    printf("Enter password: ");
    scanf("%s", buff);

    if (strncmp(buff, password, sizeof(password)) == 0)
        auth_ok = 1;

    return auth_ok;
}

void success()
{
    printf("Success!\n");
}

int main(int argc, char **argv)
{
    int res = get_password();

    if (res == 0)
    {
        printf("Failure \n");
        return 0;
    }

    success();
    return 0;
}
