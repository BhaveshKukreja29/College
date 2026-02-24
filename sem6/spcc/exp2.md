# Experiment No. 02
## Implementation of Lex Programs

**Aim:**
To write, compile, and execute Lex programs that recognise simple tokens such as words, numbers, vowels, consonants, and digits.

**Prerequisite:**
- C Programming Language

**Course Outcome:**
After successful completion of this experiment students will be able to identify and validate tokens for a given high level language and implement the synthesis phase of the compiler.

**Software used:**
- Operating System: Windows / Linux
- Lex tool: Flex
- Compiler: GCC
- Text editor (gedit / VS Code)

---

### Theory

Lex is a lexical analyzer generator used to recognise patterns in input text. A Lex program consists of three sections:

1. **Definition Section** — Contains header files, macro definitions, and global variables.
2. **Rules Section** — Contains regular expressions and corresponding actions written in C.
3. **User Code Section** — Contains auxiliary C functions and the `main()` function.

Lex converts the `.l` file into a C program (`lex.yy.c`), which is then compiled and executed.

#### General Syntax

```
%{
    /* C header files and global declarations */
%}

definitions

%%
pattern1    { action1; }
pattern2    { action2; }
%%

int main() {
    yylex();
    return 0;
}
```

---

### Procedure

1. Open terminal.
2. Create a Lex file: `program.l`
3. Generate C file using Flex: `flex program.l`
4. Compile the generated C file: `gcc lex.yy.c -o program -lfl`
5. Execute the program: `./program`
6. Enter input from keyboard (press Ctrl+D to signal EOF).

---

### Tasks

1. Lex program to count number of lines
2. Lex program to count words and characters
3. Lex program to identify vowels and consonants
4. Lex program to recognise digits and alphabets
5. Lex program to count number of digits

---

> **Roll No.:** ___________
> **Name:** ___________
> **Program:** SPCC Lab
> **Division:** C2
> **Semester:** 6
> **Batch:** C21
> **Date of Experiment:**
> **Date of Submission:**
> **Grade:**

---

### Programs

#### Program 1: Count Number of Lines

**File: `lines.l`**

```c
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
```

**How to run:**
```
flex lines.l
gcc lex.yy.c -o lines
./lines
```

---

#### Program 2: Count Words and Characters

**File: `wordchar.l`**

```c
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
```

**How to run:**
```
flex wordchar.l
gcc lex.yy.c -o wordchar
./wordchar
```

---

#### Program 3: Identify Vowels and Consonants

**File: `vowcon.l`**

```c
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
```

**How to run:**
```
flex vowcon.l
gcc lex.yy.c -o vowcon
./vowcon
```

---

#### Program 4: Recognise Digits and Alphabets

**File: `digalpha.l`**

```c
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
```

**How to run:**
```
flex digalpha.l
gcc lex.yy.c -o digalpha
./digalpha
```

---

#### Program 5: Count Number of Digits

**File: `countdig.l`**

```c
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
```

**How to run:**
```
flex countdig.l
gcc lex.yy.c -o countdig
./countdig
```

---

### Output Screenshot

*(Paste screenshot here)*

---

### Observations

- Each `.l` file was successfully converted to `lex.yy.c` using Flex, confirming that the patterns and actions follow valid Lex syntax.
- The line counter correctly increments for each `\n` character in the input stream.
- The word counter uses the pattern `[a-zA-Z]+` to match contiguous alphabetic sequences, and `yyleng` provides the matched token length for character counting.
- Vowel and consonant identification works by placing the vowel rule before the general alphabet rule — Lex applies the first matching rule when patterns overlap.
- The digit counter correctly counts individual digit characters using `[0-9]`, ignoring all other characters via the catch-all rule `.|\n`.

---

### Conclusions

This experiment demonstrates the use of Lex (Flex) as a lexical analyser generator. Each task was implemented as a `.l` file containing regular expression patterns and associated C actions. Flex compiles these specifications into a C scanner that processes input character by character. The key principle validated is that Lex uses longest-match and first-match rules to resolve pattern ambiguity, and the `yytext`/`yyleng` variables provide access to the matched lexeme. This toolchain forms the basis for building the front end of a compiler.

---

### Questions of Curiosity

**1. What is Lex?**
Lex is a tool that generates lexical analysers (scanners). It reads a specification file containing regular expression patterns and associated C actions, and produces a C source file (`lex.yy.c`) that implements a scanner recognising those patterns.

**2. What is yytext?**
`yytext` is a character pointer maintained by the Lex-generated scanner. It points to the text of the current token — i.e., the substring of the input that matched the most recent pattern rule.

**3. What is the use of yylex()?**
`yylex()` is the main scanning function generated by Lex. When called, it reads input characters, matches them against the defined patterns, and executes the corresponding action for each match. It continues until the input is exhausted or a `return` statement in an action terminates it.

**4. Difference between Lex and Yacc?**

| Aspect   | Lex                                      | Yacc                                        |
|---------|------------------------------------------|---------------------------------------------|
| Purpose | Lexical analysis (tokenisation)          | Syntax analysis (parsing)                   |
| Input   | Regular expressions                      | Context-free grammar (BNF rules)            |
| Output  | `lex.yy.c` (scanner)                     | `y.tab.c` (parser)                          |
| Phase   | First phase of compilation               | Second phase of compilation                 |
| Scope   | Recognises tokens from character streams | Validates token sequences against grammar   |

---

### References
1. Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D., *Compilers: Principles, Techniques, and Tools*, 2nd Edition, Pearson Education.
2. Alfred V. Aho and Jeffrey D. Ullman, *Principles of Compiler Design*, Addison-Wesley.
