# Experiment No. 06
## Three Address Code Generation

**Aim:**
To write a program for generating Three Address Code (TAC) from a given arithmetic expression.

**Prerequisite:**
- Programming Language (Python)

**Course Outcome:**
After successful completion of this experiment students will be able to parse the given input string by constructing top-down / bottom-up parser.

**Software used:**
- Operating System: Windows / Linux
- Python compiler

---

### Theory

Three Address Code (TAC) is an intermediate representation used in compilers during program translation. It breaks complex expressions into a sequence of simple instructions containing at most three operands.

Each TAC instruction has the form:

```
result = operand1 operator operand2
```

or

```
result = operator operand
```

TAC helps in:
- Simplifying expressions
- Code optimisation
- Easy machine code generation

#### Example

Expression: `a = b + c * d`

TAC:
```
t1 = c * d
t2 = b + t1
a = t2
```

Temporary variables (`t1`, `t2`, etc.) are used to store intermediate results.

---

### Algorithm

1. Accept an arithmetic expression.
2. Tokenise the expression into operands and operators.
3. Parse using recursive descent with operator precedence (`*`, `/` before `+`, `-`).
4. Generate temporary variables for each sub-expression.
5. Convert each operation into TAC format.
6. Print generated Three Address Code.

---

### Procedure

1. Write and save the Python program.
2. Run the program.
3. Enter an arithmetic expression.
4. Observe the generated TAC.

---

### Tasks

Implement a program that reads an arithmetic expression as input and generates its corresponding Three Address Code by identifying operators based on precedence. The program should create temporary variables to store intermediate results and print each operation in `result = operand1 operator operand2` form.

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

**File: `exp6.py`**

```python
def generate_tac(expr):
    # split assignment if present
    target = None
    if '=' in expr:
        parts = expr.split('=', 1)
        target = parts[0].strip()
        expr = parts[1].strip()

    tokens = tokenize(expr)
    result, tac = parse_expression(tokens, 0)
    
    if target:
        tac.append(f"{target} = {result}")
    
    return tac


def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isspace():
            i += 1
            continue
        if expr[i] in '+-*/()':
            tokens.append(expr[i])
            i += 1
        else:
            word = ''
            while i < len(expr) and (expr[i].isalnum() or expr[i] == '_'):
                word += expr[i]
                i += 1
            tokens.append(word)
    return tokens


temp_count = 0

def new_temp():
    global temp_count
    temp_count += 1
    return f"t{temp_count}"


def parse_expression(tokens, pos):
    left, tac, pos = parse_term(tokens, pos)
    while pos < len(tokens) and tokens[pos] in ('+', '-'):
        op = tokens[pos]
        pos += 1
        right, tac2, pos = parse_term(tokens, pos)
        tac.extend(tac2)
        t = new_temp()
        tac.append(f"{t} = {left} {op} {right}")
        left = t
    return left, tac, pos


def parse_term(tokens, pos):
    left, tac, pos = parse_factor(tokens, pos)
    while pos < len(tokens) and tokens[pos] in ('*', '/'):
        op = tokens[pos]
        pos += 1
        right, tac2, pos = parse_factor(tokens, pos)
        tac.extend(tac2)
        t = new_temp()
        tac.append(f"{t} = {left} {op} {right}")
        left = t
    return left, tac, pos


def parse_factor(tokens, pos):
    if tokens[pos] == '(':
        pos += 1  # skip (
        result, tac, pos = parse_expression(tokens, pos)
        pos += 1  # skip )
        return result, tac, pos
    else:
        return tokens[pos], [], pos + 1


expr = input("Enter expression (e.g. a = b + c * d): ")
tac = generate_tac(expr)

print("\nThree Address Code:")
for line in tac:
    print(f"  {line}")
```

---

### Output Screenshot

*(Paste screenshot here)*

---

### Observations

- The program correctly respects operator precedence — multiplication and division are evaluated before addition and subtraction, generating temporaries in the correct order.
- For the expression `a = b + c * d`, the TAC correctly produces `t1 = c * d`, `t2 = b + t1`, `a = t2`.
- Parenthesised sub-expressions are handled by the recursive descent parser, ensuring correct grouping regardless of default precedence.
- Each TAC instruction contains at most three operands (one result, two source operands), conforming to the three-address format.
- Temporary variables are numbered sequentially (`t1`, `t2`, `t3`, …), providing a clear trace of the evaluation order.

---

### Conclusions

This experiment demonstrates intermediate code generation in the form of Three Address Code using a recursive descent parser with operator precedence. TAC serves as a bridge between the high-level source expression and the final machine code — it decomposes complex expressions into atomic operations that map directly to machine instructions. The recursive descent approach naturally handles precedence and associativity, producing correct TAC without requiring explicit precedence tables.

---

### Questions of Curiosity

**1. What is Three Address Code?**
Three Address Code is an intermediate representation where each instruction has at most three operands — typically one result and two source operands. It takes the form `x = y op z`, where `x`, `y`, `z` are variables or temporaries and `op` is an operator.

**2. Why is TAC used in compilers?**
TAC simplifies complex source expressions into atomic operations that are easy to optimise and translate to machine code. It provides a platform-independent intermediate form, allowing the compiler to apply optimisations (constant folding, dead code elimination, CSE) before generating target-specific code.

**3. What are temporary variables?**
Temporary variables (`t1`, `t2`, …) are compiler-generated variables that hold intermediate results during expression evaluation. They do not appear in the original source code and exist only in the intermediate representation.

**4. Give the general form of TAC.**
The general forms are:
- `x = y op z` — binary operation
- `x = op y` — unary operation
- `x = y` — copy/assignment

**5. What is intermediate code generation?**
Intermediate code generation is the compiler phase that translates the syntax tree (or parse tree) into an intermediate representation like TAC. It sits between the front end (parsing) and the back end (code generation), enabling machine-independent optimisation.

**6. Name types of intermediate representations.**
Three Address Code (TAC / quadruples / triples)
Abstract Syntax Trees (AST)
Directed Acyclic Graphs (DAG)
Static Single Assignment (SSA) form
Postfix notation (reverse Polish)

---

### References
1. Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D., *Compilers: Principles, Techniques, and Tools*, 2nd Edition, Pearson Education.
2. Alfred V. Aho and Jeffrey D. Ullman, *Principles of Compiler Design*, Addison-Wesley.
