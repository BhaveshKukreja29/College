%{
#include <stdio.h>
int words = 0, chars = 0;
%}

%%
[a-zA-Z]+   { words++; chars += yyleng; }
.           { chars++; }
\n          { ; }
%%

int main() {
    yylex();
    printf("Total words: %d\n", words);
    printf("Total characters: %d\n", chars);
    return 0;
}

int yywrap() { return 1; }
