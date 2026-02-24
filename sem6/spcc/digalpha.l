%{
#include <stdio.h>
%}

%%
[0-9]       { printf("%s is a digit\n", yytext); }
[a-zA-Z]    { printf("%s is an alphabet\n", yytext); }
.|\n        { ; }
%%

int main() {
    yylex();
    return 0;
}

int yywrap() { return 1; }
