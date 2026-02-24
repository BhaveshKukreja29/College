%{
#include <stdio.h>
%}

%%
[aeiouAEIOU]    { printf("%s is a vowel\n", yytext); }
[a-zA-Z]        { printf("%s is a consonant\n", yytext); }
.|\n            { ; }
%%

int main() {
    yylex();
    return 0;
}

int yywrap() { return 1; }
