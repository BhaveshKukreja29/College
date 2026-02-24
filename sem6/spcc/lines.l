%{
#include <stdio.h>
int lines = 0;
%}

%%
\n      { lines++; }
.       { ; }
%%

int main() {
    yylex();
    printf("Total lines: %d\n", lines);
    return 0;
}

int yywrap() { return 1; }
