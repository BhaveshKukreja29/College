%{
#include <stdio.h>
int digits = 0;
%}

%%
[0-9]   { digits++; }
.|\n    { ; }
%%

int main() {
    yylex();
    printf("Total digits: %d\n", digits);
    return 0;
}

int yywrap() { return 1; }
