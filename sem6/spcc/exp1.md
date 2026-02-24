# Experiment No. 01
## Implementation of Lexical Analyzer

**Aim:**
To design and implement a Lexical Analyzer that reads a source program and identifies tokens such as keywords, identifiers, operators, literals, and separators.

**Prerequisite:**
- Any Programming Language

**Course Outcome:**
After successful completion of this experiment students will be able to identify and validate tokens for a given high level language and implement the synthesis phase of the compiler.

**Software used:**
- Python compiler

---

### Theory

A Lexical Analyzer (also called a scanner) is the first phase of a compiler. It takes the source code as input and converts it into a sequence of tokens. Each token is a meaningful unit like a keyword (`int`, `if`), identifier (`x`, `sum`), operator (`+`, `=`), or constant (`10`).

The lexical analyzer:
- Removes whitespace and comments
- Groups characters into lexemes
- Produces tokens for the syntax analyzer

#### Token Types Identified

| Token Type          | Examples                     |
|--------------------|------------------------------|
| Keywords           | `int`, `float`, `if`, `else`, `while` |
| Identifiers        | variable names               |
| Operators          | `+`, `-`, `*`, `/`, `=`, `<=`, `>=`, `==`, `!=` |
| Constants          | numbers (integer and float)  |
| Separators         | `;`, `,`, `(`, `)`, `{`, `}` |

#### Algorithm

1. Start
2. Read input source program
3. Scan characters from left to right
4. Ignore whitespace and comments
5. If character forms:
   - keyword → generate keyword token
   - identifier → generate identifier token
   - operator → generate operator token
   - constant → generate constant token
6. Repeat until end of file
7. Display token list
8. Stop

---

### Procedure

1. Open a text editor / IDE and write the code in Python.
2. Run the code.

---

### Tasks

**Input:** A program written in any high-level language (e.g., C).

Example Input:
```
int a = 10;
if (a > 5)
    a = a + 1;
```

Expected Output:
```
Keyword     : int
Identifier  : a
Operator    : =
Number      : 10
Separator   : ;
Keyword     : if
Separator   : (
Identifier  : a
Operator    : >
Number      : 5
Separator   : )
Identifier  : a
Operator    : =
Identifier  : a
Operator    : +
Number      : 1
Separator   : ;
```

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

### Program

**File: `exp1.py`**

```python
"""
Experiment 1: Lexical Analyzer
Tokenizes input lines into keywords, identifiers, numbers, operators, and separators.
"""

keywords = ['int', 'float', 'double', 'if', 'else', 'while', 'for', 'return', 'void', 'char']
operators = ['+', '-', '*', '/', '=', '<', '>', '!', '%']
separators = [';', ',', '(', ')', '{', '}', '[', ']']

def tokenize(line):
    tokens = []
    i = 0
    while i < len(line):
        ch = line[i]

        # skip whitespace
        if ch.isspace():
            i += 1
            continue

        # multi-char operators like ==, <=, >=, !=
        if ch in operators and i + 1 < len(line) and line[i + 1] == '=':
            tokens.append(('Operator', ch + '='))
            i += 2
            continue

        if ch in operators:
            tokens.append(('Operator', ch))
            i += 1
            continue

        if ch in separators:
            tokens.append(('Separator', ch))
            i += 1
            continue

        # numbers (int or float)
        if ch.isdigit():
            num = ''
            while i < len(line) and (line[i].isdigit() or line[i] == '.'):
                num += line[i]
                i += 1
            tokens.append(('Number', num))
            continue

        # keywords or identifiers
        if ch.isalpha() or ch == '_':
            word = ''
            while i < len(line) and (line[i].isalnum() or line[i] == '_'):
                word += line[i]
                i += 1
            if word in keywords:
                tokens.append(('Keyword', word))
            else:
                tokens.append(('Identifier', word))
            continue

        i += 1

    return tokens


n = int(input("Enter number of lines: "))
all_tokens = []

for x in range(n):
    line = input(f"Enter line {x + 1}: ")
    toks = tokenize(line)
    all_tokens.extend(toks)

    print(f"\n====== Line {x + 1} ======")
    for typ, val in toks:
        print(f"  {typ} : {val}")

print(f"\n{'='*40}")
print(f"Total tokens = {len(all_tokens)}")
print(f"{'='*40}")
```

---

### Output Screenshot

*(Paste screenshot here)*

---

### Observations

- Whitespace and newline characters are successfully ignored during scanning.
- Operators like `+`, `-`, `*`, `/`, and `=` are correctly identified as single-character operators.
- Multi-character operators such as `==`, `<=`, `>=`, and `!=` are correctly recognised as compound tokens rather than being split into two separate tokens.
- Reserved words (`int`, `if`, `while`, etc.) are distinguished from user-defined identifiers by checking against a predefined keyword list.
- Numeric constants, including floating-point numbers containing a decimal point, are grouped into a single `Number` token.

---

### Conclusions

This experiment demonstrates the implementation of the first phase of a compiler — the lexical analyzer. The scanner successfully converts raw source code into a stream of classified tokens by iterating through characters, handling whitespace, and grouping lexemes based on pattern rules. The approach validates that a simple state-driven character-by-character scan is sufficient for tokenising a subset of C-like source code.

---

### Questions of Curiosity

**1. What happens if the lexical analyzer does not recognize a character?**
If the scanner encounters a character that does not match any defined pattern (keyword, identifier, operator, separator, or digit), it is silently skipped. In a production compiler, such characters would be flagged as lexical errors and reported to the user with their position in the source.

**2. Why is the lexical analyzer called the first phase of a compiler?**
It is the first phase because it operates directly on the raw character stream of the source code. Every subsequent phase (syntax analysis, semantic analysis, code generation) works on the token stream produced by the lexer, not on raw characters.

**3. Can the lexical analyzer detect syntax errors? Why or why not?**
No. The lexical analyzer only validates individual tokens — it checks whether a character sequence forms a valid lexeme. It has no knowledge of how tokens should be ordered relative to each other. Structural errors like a missing semicolon or mismatched parentheses are the responsibility of the syntax analyzer (parser).

**4. What would happen if whitespace was not ignored?**
Whitespace characters (spaces, tabs, newlines) would be treated as tokens themselves. This would flood the token stream with meaningless whitespace tokens, complicating the parser and making grammar rules unnecessarily complex.

---

### References
1. Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D., *Compilers: Principles, Techniques, and Tools*, 2nd Edition, Pearson Education.
2. Alfred V. Aho and Jeffrey D. Ullman, *Principles of Compiler Design*, Addison-Wesley.
