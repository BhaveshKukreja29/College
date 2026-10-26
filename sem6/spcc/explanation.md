# SPCC Practical Exam — Experiments 1 to 5
## Theory + Implementation Guide (From Zero)

> **How to use this doc:** Each experiment starts with "Why does this exist?" (the big picture), then the theory you need, then a line-by-line breakdown of how the code works and how to reproduce it from scratch.

---

# Background: What is a Compiler?

A compiler converts **source code** (what you write) into **machine code** (what the CPU runs). It does this in **phases**:

```
Source Code
    │
    ▼
┌──────────────────┐
│ 1. Lexical        │ ← Exp 1 & 2
│    Analysis       │   (break code into tokens)
├──────────────────┤
│ 2. Syntax         │ ← Exp 3, 4 & 5
│    Analysis       │   (check structure / grammar)
├──────────────────┤
│ 3. Semantic       │
│    Analysis       │   (type checking, etc.)
├──────────────────┤
│ 4. Intermediate   │
│    Code Gen       │
├──────────────────┤
│ 5. Optimization   │
├──────────────────┤
│ 6. Code Gen       │
└──────────────────┘
    │
    ▼
Machine Code
```

Experiments 1-5 cover the **front end** of the compiler: breaking code into tokens and validating its grammatical structure.

---
---

# Experiment 1: Lexical Analyzer

## Why does this exist?

When you write `int a = 10;`, the compiler doesn't see words — it sees a raw stream of characters: `i`, `n`, `t`, ` `, `a`, ` `, `=`, ` `, `1`, `0`, `;`. The **lexical analyzer** (aka **scanner** or **tokenizer**) is the program that groups these characters into meaningful chunks called **tokens**.

## Core Concepts

### What is a Token?
A token is a `(type, value)` pair. For `int a = 10;`:

| Token Type   | Value |
|-------------|-------|
| Keyword     | `int` |
| Identifier  | `a`   |
| Operator    | `=`   |
| Number      | `10`  |
| Separator   | `;`   |

### Token Categories (that your code handles)

| Category     | How to identify                                      | Examples                          |
|-------------|------------------------------------------------------|-----------------------------------|
| **Keywords**    | Exact match against a predefined list                | `int`, `float`, `if`, `while`, `return` |
| **Identifiers** | Starts with letter/underscore, followed by alphanumeric/underscore | `myVar`, `count`, `_temp` |
| **Numbers**     | Starts with a digit, can contain `.` for floats       | `10`, `3.14`                      |
| **Operators**   | Single-char (`+`, `=`) or multi-char (`==`, `<=`, `!=`) | `+`, `-`, `>=`                   |
| **Separators**  | Punctuation that separates code structures             | `;`, `(`, `)`, `{`, `}`          |

### How does the scanner decide?

It reads **one character at a time** from left to right:
1. If it's whitespace → skip.
2. If it's a letter/underscore → keep reading until non-alphanumeric → you get a word → check: is it a keyword? If not, it's an identifier.
3. If it's a digit → keep reading digits (and one `.`) → you get a number.
4. If it's an operator char → peek at the next char to check for multi-char operators like `==`, `<=`.
5. If it's a separator → emit it immediately.

## How the Code Works (`exp1.py`)

```python
keywords = ['int', 'float', 'double', 'if', 'else', 'while', 'for', 'return', 'void', 'char']
operators = ['+', '-', '*', '/', '=', '<', '>', '!', '%']
separators = [';', ',', '(', ')', '{', '}', '[', ']']
```
These are your **lookup tables** — the scanner checks characters against these lists.

The main logic is a `while` loop with index `i` walking the string:

```python
i = 0
while i < len(line):
    ch = line[i]
```

**Priority order of checks:**
1. **Whitespace** → `ch.isspace()` → skip, `i += 1`
2. **Multi-char operator** → if `ch` is in operators AND next char is `=` → emit `ch + '='`, `i += 2`
3. **Single operator** → `ch in operators` → emit, `i += 1`
4. **Separator** → `ch in separators` → emit, `i += 1`
5. **Number** → `ch.isdigit()` → greedy loop collecting digits and `.`, emit
6. **Word** → `ch.isalpha() or ch == '_'` → greedy loop collecting alphanumerics → check keyword list → emit as keyword or identifier

### How to write this from scratch

1. Define the three lists (keywords, operators, separators).
2. Write a function that takes a string and returns a list of `(type, value)` tuples.
3. Use a `while` loop with an index `i`, not a `for` loop (because you sometimes need to advance `i` by more than 1).
4. Check conditions in the priority order above.
5. For numbers and words, use an inner `while` loop that keeps consuming characters.

### Sample Run

```
Input:  int x = 5 + 3;
Output:
  Keyword   : int
  Identifier: x
  Operator  : =
  Number    : 5
  Operator  : +
  Number    : 3
  Separator : ;
```

### Common Exam Questions
- **Can the lexer detect syntax errors?** No. It only validates individual tokens, not their order. `int int int` is three valid tokens; it's the parser's job to reject it.
- **What happens with unrecognized characters?** In this code, they're silently skipped. A real compiler would report a lexical error.

---
---

# Experiment 2: Lex Programs (Flex)

## Why does this exist?

Experiment 1 was a **hand-written** lexer. Experiment 2 uses a **tool called Lex (Flex)** that **generates** a lexer for you from pattern specifications. You just write regex patterns + actions, and Flex produces a C program that does the scanning.

## Core Concepts

### What is Lex/Flex?
- **Lex** = the original tool (AT&T Unix).
- **Flex** = "Fast Lex" — the modern open-source version. They're interchangeable for our purposes.

### How a `.l` file is structured

A Lex file has **three sections** separated by `%%`:

```
%{
  /* C code: includes, global variables */
%}

/* definitions (optional: named patterns) */

%%
pattern1    { action1; }
pattern2    { action2; }
%%

/* C code: main() and helper functions */
```

### Key concepts:

| Concept     | Meaning |
|------------|---------|
| `yylex()`  | The generated scanner function — call it to start scanning |
| `yytext`   | A `char*` pointing to the text that matched the current pattern |
| `yyleng`   | Length of the matched text |
| `yywrap()` | Called when input ends; return `1` to stop, `0` to continue with another file |
| `%%`       | Delimiter between sections |

### Pattern matching rules:
- **Longest match wins:** If input is `abcd` and patterns are `[a-z]` and `[a-z]+`, the `+` version matches `abcd` (longer).
- **First rule wins:** If two patterns match the same length, the one listed first is used.

### How to compile and run:
```bash
flex program.l          # generates lex.yy.c
gcc lex.yy.c -o program # compile
./program               # run (type input, press Ctrl+D to end)
```

## The 5 Sub-Programs

### Program 1: Count Lines
```c
%%
\n      { lines++; }    // every newline = one more line
.       { ; }           // dot matches any char except newline — ignore it
%%
```
**Logic:** Count `\n` characters. The `.` (dot) catches everything else and does nothing.

### Program 2: Count Words and Characters
```c
%%
[a-zA-Z]+   { words++; chars += yyleng; }   // sequence of letters = 1 word
.           { chars++; }                     // any other char = 1 character
\n          { ; }                            // ignore newlines
%%
```
**Logic:** `[a-zA-Z]+` matches one or more letters (= a word). `yyleng` gives the length of that word for character counting.

### Program 3: Identify Vowels and Consonants
```c
%%
[aeiouAEIOU]    { printf("%s is a vowel\n", yytext); }
[a-zA-Z]        { printf("%s is a consonant\n", yytext); }
.|\\n           { ; }
%%
```
**Logic:** Vowel rule is listed **before** the general letter rule. Since Flex uses first-match for equal-length matches, vowels hit the first rule, consonants fall through to the second.

### Program 4: Recognise Digits and Alphabets
```c
%%
[0-9]       { printf("%s is a digit\n", yytext); }
[a-zA-Z]    { printf("%s is an alphabet\n", yytext); }
.|\\n       { ; }
%%
```
**Logic:** Straightforward character classification.

### Program 5: Count Digits
```c
%%
[0-9]   { digits++; }
.|\\n   { ; }
%%
```
**Logic:** Increment counter for every digit character.

### For the Python equivalent (`exp2.py`)

Your `exp2.py` does all 5 tasks in pure Python using string methods (`isdigit()`, `isalpha()`, `.split()`, `.count('\n')`). It's a simulated version if you don't have Flex installed.

### Common Exam Questions
- **What is `yywrap()`?** It's called when EOF is reached. Return 1 to stop scanning.
- **Difference between Lex and Yacc?** Lex does tokenization (phase 1), Yacc does parsing (phase 2). Lex outputs `lex.yy.c`, Yacc outputs `y.tab.c`.

---
---

# Experiment 3: Left Recursion Elimination & Left Factoring

## Why does this exist?

After tokenizing (Exp 1-2), the next phase is **parsing** — checking if the token sequence follows the grammar rules of the language. The most intuitive parsers are **top-down parsers** (they start from the start symbol and try to derive the input). But top-down parsers **break** on two grammar patterns:
1. **Left recursion** → causes infinite loops
2. **Common prefixes** → parser can't decide which rule to pick

This experiment fixes both problems.

## Core Concept 1: Context-Free Grammar (CFG)

A CFG is a set of rules (productions) that describe valid programs. Example:

```
E → E + T | T
T → T * F | F
F → ( E ) | id
```

This says: "An expression E is either E+T or just T. A term T is either T*F or just F. A factor F is either (E) or an id."

**Notation:**
- **Uppercase letters** (E, T, F) = non-terminals (abstract categories)
- **Lowercase/symbols** (+, *, id, (, )) = terminals (actual tokens)
- `|` = "or" (alternative productions)
- `ε` (epsilon) = empty string (produce nothing)

## Core Concept 2: Left Recursion

**What:** A rule like `E → E + T` is left-recursive because the non-terminal E appears as the **first symbol** on the right side.

**Why it's a problem:** A top-down parser for `E` would do:
1. To parse `E`, try `E → E + T`
2. To parse that `E`, try `E → E + T`
3. To parse that `E`, try `E → E + T`
4. → **infinite loop** (never reads any input!)

**The fix:** Convert left recursion to right recursion.

### The Formula

Given: `A → Aα | β` (α is what comes after A, β is the non-recursive alternative)

Convert to:
```
A  → β A'
A' → α A' | ε
```

### Worked Example

```
E → E + T | T          (α = "+ T", β = "T")
```
Becomes:
```
E  → T E'
E' → + T E' | ε
```

**Why this works:** Instead of left-recursing (`E → E → E → ...`), the new grammar right-recurses through `E'`. Each step of `E'` **consumes** a `+ T`, and it stops when it hits `ε`. Same language, no infinite loop.

## Core Concept 3: Left Factoring

**What:** When two rules for the same non-terminal start with the same symbol:
```
S → if E then S else S
S → if E then S
```

**Why it's a problem:** A top-down parser sees `if` and can't decide which rule to use — both start with `if`.

**The fix:** Factor out the common prefix.

### The Formula

Given: `A → αβ₁ | αβ₂` (α is the common prefix)

Convert to:
```
A  → α A'
A' → β₁ | β₂
```

Now the parser reads α first, then looks at the next token to decide between β₁ and β₂.

## How the Code Works (`exp3.py`)

The code has two main functions:

### `eliminate_left_recursion(grammar, order)`
```python
for prod in prods:
    if prod[0] == nt:              # does it start with itself? → left recursive
        recursive.append(prod[1:])  # save the α part (everything after the self-reference)
    else:
        non_recursive.append(prod)  # save the β part
```

If there are recursive productions:
```python
new_nt = nt + "'"                                        # create A'
new_grammar[nt] = [p + [new_nt] for p in non_recursive]  # A → β A'
new_grammar[new_nt] = [r + [new_nt] for r in recursive] + [['e']]  # A' → α A' | ε
```

### `left_factor(grammar, order)`
```python
prefix_map = {}
for prod in prods:
    first = prod[0]          # group productions by their first symbol
    prefix_map[first].append(prod)
```

If any group has more than one production (common prefix):
```python
new_prods.append([key, new_nt])     # A → prefix A'
suffixes = [p[1:] for p in group]   # A' → suffix1 | suffix2 | ...
```

### How to write this from scratch
1. **Input:** Read grammar as a dictionary: `{'E': [['E', '+', 'T'], ['T']]}`
2. **Left recursion:** For each non-terminal, split its productions into "starts with itself" vs "doesn't". Apply the formula.
3. **Left factoring:** For each non-terminal, group productions by first symbol. If any group has >1 production, factor it out.
4. **Output:** Print the transformed grammar.

### Sample Run
```
Input:
  E → E + T | T
  T → T * F | F
  F → ( E ) | id

After Left Recursion Elimination:
  E  → T E'
  E' → + T E' | ε
  T  → F T'
  T' → * F T' | ε
  F  → ( E ) | id

After Left Factoring:
  (no change — no common prefixes)
```

### Common Exam Questions
- **Does eliminating left recursion change the language?** No, same strings are generated. Only the parse tree shape changes.
- **Can bottom-up parsers handle left recursion?** Yes! Only top-down parsers break. LR parsers are fine.

---
---

# Experiment 4: FIRST and FOLLOW Sets

## Why does this exist?

After eliminating left recursion and left factoring (Exp 3), we have a "clean" grammar. But the parser still needs to **decide which production to use** when it sees a token. That decision is made using **FIRST** and **FOLLOW** sets.

Think of it this way: if the parser is at non-terminal `A` and sees token `a`, it asks:
- "Which production of `A` can **start** with `a`?" → uses **FIRST**
- "If a production can produce ε (nothing), is `a` something that can come **after** `A`?" → uses **FOLLOW**

## FIRST Set — Theory

**FIRST(X)** = the set of terminals that can appear as the **first symbol** in any string derived from X.

### Rules:

| Situation | Rule |
|----------|------|
| X is a terminal | FIRST(X) = {X} |
| X → ε | Add ε to FIRST(X) |
| X → Y₁ Y₂ ... Yₖ | Add FIRST(Y₁) − {ε} to FIRST(X). If Y₁ can produce ε, also add FIRST(Y₂) − {ε}, and so on. If ALL of Y₁...Yₖ can produce ε, then add ε to FIRST(X). |

### Worked Example

Grammar (after left recursion elimination):
```
E  → T E'
E' → + T E' | ε
T  → F T'
T' → * F T' | ε
F  → ( E ) | id
```

| Non-terminal | FIRST set |
|-------------|-----------|
| F | { `(`, `id` } — directly from its productions |
| T' | { `*`, `ε` } — from `* F T'` and `ε` |
| T | { `(`, `id` } — FIRST(T) = FIRST(F) since F can't produce ε |
| E' | { `+`, `ε` } |
| E | { `(`, `id` } — FIRST(E) = FIRST(T) |

## FOLLOW Set — Theory

**FOLLOW(A)** = the set of terminals that can appear **immediately after** A in any valid derivation.

### Rules:

| Situation | Rule |
|----------|------|
| A is the start symbol | Add `$` (end marker) to FOLLOW(A) |
| B → α A β (A is followed by β) | Add FIRST(β) − {ε} to FOLLOW(A) |
| B → α A β and ε ∈ FIRST(β), OR B → α A (nothing after A) | Add FOLLOW(B) to FOLLOW(A) |

### Worked Example (continued)

| Non-terminal | FOLLOW set | Reasoning |
|-------------|-----------|-----------|
| E | { `)`, `$` } | Start symbol → `$`. Also appears in `( E )` → `)` |
| E' | { `)`, `$` } | E → T E' → FOLLOW(E') = FOLLOW(E) |
| T | { `+`, `)`, `$` } | From E' → + T E' → FIRST(E')−{ε} = {`+`}. Since ε ∈ FIRST(E'), also FOLLOW(E') = {`)`, `$`} |
| T' | { `+`, `)`, `$` } | T → F T' → FOLLOW(T') = FOLLOW(T) |
| F | { `*`, `+`, `)`, `$` } | From T' → * F T' → FIRST(T')−{ε} = {`*`}. Since ε ∈ FIRST(T'), also FOLLOW(T') |

## How the Code Works (`exp4.py`)

### `first(grammar)` — Fixed-point iteration

The algorithm runs in a loop and keeps adding terminals to FIRST sets until nothing changes:

```python
changed = True
while changed:
    changed = False
    for nt in grammar:
        for prod in grammar[nt]:
            for sym in prod:
                if sym == 'e':         # epsilon production → add ε
                    ans[nt].add('e')
                elif sym not in grammar:  # terminal → add it, stop
                    ans[nt].add(sym)
                    break
                else:                    # non-terminal → add its FIRST - {ε}
                    ans[nt] |= ans[sym] - {'e'}
                    if 'e' not in ans[sym]:  # if it can't produce ε, stop
                        break
```

**Key insight:** The `while changed` loop is needed because FIRST sets depend on each other. `FIRST(E)` depends on `FIRST(T)` which depends on `FIRST(F)`. Multiple passes propagate the information.

### `follow(grammar, first_sets)` — Also fixed-point

```python
ans[start].add('$')  # Rule 1: start symbol gets $

for nt in grammar:
    for prod in grammar[nt]:
        for i, sym in enumerate(prod):
            if sym not in grammar: continue  # skip terminals
            beta = prod[i + 1:]              # everything after sym

            # Add FIRST(beta) - {ε} to FOLLOW(sym)
            # If beta is nullable/empty, add FOLLOW(nt) to FOLLOW(sym)
```

### How to write from scratch
1. **Grammar representation:** `{'E': [['T', "E'"]], "E'": [['+', 'T', "E'"], ['e']], ...}`
2. **FIRST:** Initialize empty sets. Loop until stable. For each production, walk symbols left-to-right, adding terminals/FIRST-of-nonterminals.
3. **FOLLOW:** Initialize start symbol with `$`. Loop until stable. For each symbol in each production, look at what comes after it.

### Common Exam Questions
- **Why does FOLLOW of start symbol include `$`?** Because `$` marks end-of-input. The start symbol's derivation is always followed by EOF.
- **Why iterate until no changes?** Because FOLLOW sets have circular dependencies. `FOLLOW(T)` may depend on `FOLLOW(E')` which depends on `FOLLOW(E)`.

---
---

# Experiment 5: LL(1) Parser Construction

## Why does this exist?

Experiments 3 and 4 were **preparation** — cleaning the grammar and computing FIRST/FOLLOW. Now we build the actual **parser**: an LL(1) parsing table that tells the parser exactly which production to use for every (non-terminal, lookahead token) combination.

## Core Concepts

### What does LL(1) mean?

| Letter | Meaning |
|--------|---------|
| **L** | Scan input **L**eft to right |
| **L** | Produce a **L**eftmost derivation |
| **1** | Use **1** lookahead token |

An LL(1) parser is a **predictive parser** — no backtracking. It looks at the current non-terminal to expand + the next input token, and the parsing table tells it exactly which production to use.

### LL(1) Prerequisites
The grammar must:
1. Have **no left recursion** (fixed in Exp 3)
2. Have **no common prefixes** (fixed in Exp 3)
3. Have **disjoint FIRST sets** for alternative productions
4. If ε ∈ FIRST(α), then FIRST(α) ∩ FOLLOW(A) = ∅

### The Parsing Table

It's a 2D table: **rows** = non-terminals, **columns** = terminals + `$`.

**Construction algorithm:**

For each production `A → α`:
1. For every terminal `a` in FIRST(α) (except ε): put `A → α` in cell `M[A, a]`
2. If ε ∈ FIRST(α): for every terminal `b` in FOLLOW(A): put `A → α` in cell `M[A, b]`

**If any cell has two entries → grammar is NOT LL(1).**

### Worked Example

Grammar: `S → aA`, `A → b | ε`

FIRST(S) = {a}, FIRST(A) = {b, ε}
FOLLOW(S) = {$}, FOLLOW(A) = {$}

| | a | b | $ |
|---|---|---|---|
| **S** | S → aA | — | — |
| **A** | — | A → b | A → ε |

- `S → aA`: FIRST(aA) = {a} → M[S, a] = "S → aA"
- `A → b`: FIRST(b) = {b} → M[A, b] = "A → b"
- `A → ε`: ε ∈ FIRST(ε), so for each terminal in FOLLOW(A) = {$}: M[A, $] = "A → ε"

No conflicts → **grammar is LL(1)** ✓

## How the Code Works (`exp5.py`)

### Step 1: Parse input and extract terminals/non-terminals
```python
prods = [input().replace(" ", "").split("->") for _ in range(n)]
nt_list = list(dict.fromkeys([p[0] for p in prods]))         # non-terminals
t_list = [...extract lowercase/symbol chars...] + ['$']       # terminals + $
```

### Step 2: Compute FIRST (recursive `get_first`)
```python
def get_first(s):
    if not s.isupper(): return {s}    # terminal → FIRST = itself
    res = set()
    for head, body in [p for p in prods if p[0] == s]:
        if body == 'e': res.add('e')
        else:
            for char in body:
                f = get_first(char)
                res |= (f - {'e'})
                if 'e' not in f: break
            else: res.add('e')       # all symbols were nullable → add ε
    return res
```

### Step 3: Compute FOLLOW (iterative)
```python
follow[start_symbol].add('$')
# For each production A → ...B...:
#   If B is a non-terminal, look at what comes after B
#   Add FIRST(next) - {ε} to FOLLOW(B)
#   If next is nullable or empty, add FOLLOW(A) to FOLLOW(B)
```

### Step 4: Build the parsing table
```python
for head, body in prods:
    f_body = get_first(body[0])           # FIRST of the production's body

    for s in f_body:
        if s != 'e':
            table[head][s] = f"{head}->{body}"   # Rule 1: terminal in FIRST
        else:
            for f_s in follow[head]:
                table[head][f_s] = f"{head}->{body}"  # Rule 2: terminal in FOLLOW
```

### Step 5: Check for conflicts
```python
if table[head][s]:    # if cell already has a production → CONFLICT
    is_ll1 = False
```

### How to write from scratch
1. Take grammar as input (e.g., `S->aA`, `A->b`, `A->e`).
2. Compute FIRST sets (recursive function or iterative fixed-point).
3. Compute FOLLOW sets (iterative fixed-point).
4. Initialize a 2D dict `table[non_terminal][terminal] = ""`.
5. For each production, fill in table cells using FIRST/FOLLOW rules.
6. Check if any cell got filled twice → not LL(1).

### Sample Run
```
Input:
  S->aA
  A->b
  A->e

FIRST: S={a}, A={b, e}
FOLLOW: S={$}, A={$}

Table:
  S | S->aA | -   | -
  A | -     | A->b | A->e

Grammar is LL1
```

---
---

# Cheat Sheet: How Everything Connects

```
Exp 1: Lexical Analyzer          "Break code into tokens"
  ↓
Exp 2: Lex/Flex                  "Same thing, but using a tool that generates the scanner from regex"
  ↓
Exp 3: Left Recursion + Factoring "Clean the grammar so top-down parsing works"
  ↓
Exp 4: FIRST & FOLLOW             "Compute what tokens can start/follow each non-terminal"
  ↓
Exp 5: LL(1) Parser Table         "Build the decision table that tells the parser which rule to use"
```

## Quick Implementation Recap

| Exp | Input | Output | Core Data Structure |
|-----|-------|--------|---------------------|
| 1 | Source code string | List of `(type, value)` tokens | Lists for keywords/operators/separators |
| 2 | Text input to Flex `.l` file | Pattern-matched results | Regex rules in Lex format |
| 3 | Grammar as dict | Transformed grammar (no left recursion, no common prefixes) | Dict of non-terminal → list of productions |
| 4 | Grammar as dict | FIRST and FOLLOW sets (set of terminals per non-terminal) | Dict of non-terminal → set of terminals |
| 5 | Grammar + FIRST + FOLLOW | 2D parsing table + LL(1) verdict | Dict of dicts: `table[NT][terminal]` |

---

# Tips for the Practical Exam

1. **Start from the data structures.** Every program is just manipulating dicts and lists. Picture the data structure first, then the logic writes itself.
2. **Exp 1 is the easiest to freestyle.** Just the while-loop scanner with the 5-way `if-elif` chain.
3. **Exp 3-5 are connected.** If asked to build an LL(1) parser from scratch, you'd chain: input grammar → Exp 3 (clean it) → Exp 4 (FIRST/FOLLOW) → Exp 5 (table).
4. **Use `'e'` for epsilon** in your Python code. It's a convention in these programs.
5. **Non-terminals are UPPERCASE, terminals are lowercase** — that's how the code distinguishes them.
6. **The fixed-point loop pattern** (`while changed: changed = False; ... changed = True`) appears in Exp 4 and is a very common pattern in compilers. Understand it well.

Good luck tomorrow. 🚀
