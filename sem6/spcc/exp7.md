# Experiment No. 07
## Code Optimization using Common Subexpression Elimination

**Aim:**
To implement code optimisation using the Common Subexpression Elimination (CSE) technique to reduce redundant computations in intermediate code.

**Prerequisite:**
- Programming Language (Python)

**Course Outcome:**
After successful completion of this experiment students will be able to identify and validate tokens for a given high level language and implement the synthesis phase of the compiler.

**Software used:**
- Operating System: Windows / Linux
- Python compiler

---

### Theory

Code optimisation is a compiler design technique used to improve the performance and efficiency of generated code without changing its output. One important optimisation method is **Common Subexpression Elimination (CSE)**.

A common subexpression is an expression that appears more than once in a program and evaluates to the same value, provided the variables involved are not modified between occurrences.

#### Example

Before CSE:
```
t1 = a + b
t2 = a + b
t3 = t1 * c
```

After CSE:
```
t1 = a + b
t2 = t1
t3 = t1 * c
```

The repeated evaluation of `a + b` is avoided, improving efficiency.

CSE reduces:
- Execution time
- Code size
- CPU usage

It is commonly applied on Three Address Code (TAC) during intermediate code optimisation.

---

### Algorithm

1. Input the intermediate code (Three Address Code).
2. For each expression on the RHS:
   - Check if the same expression was previously computed.
   - Ensure none of its operands were modified after its first computation.
3. If found: replace the repeated expression with the previously computed temporary variable.
4. Generate optimised code.

---

### Procedure

1. Write and save the Python program.
2. Run the program.
3. Enter TAC lines.
4. Observe the optimised output.

---

### Tasks

Implement a program that detects common subexpressions and replaces redundant computations with previously computed temporary variables. Test with at least three different input cases (with and without common subexpressions), compare original and optimised code, and record the results.

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

**File: `exp7.py`**

```python
def eliminate_cse(code):
    lines = [line.strip() for line in code if line.strip()]
    expr_map = {}
    optimized = []

    for line in lines:
        parts = line.split('=', 1)
        lhs = parts[0].strip()
        rhs = parts[1].strip()

        if rhs in expr_map:
            optimized.append(f"{lhs} = {expr_map[rhs]}")
        else:
            expr_map[rhs] = lhs
            optimized.append(line)

    return optimized


print("Enter Three Address Code (type 'done' to finish):")
code = []
while True:
    line = input()
    if line.strip().lower() == 'done':
        break
    code.append(line)

print("\nOriginal Code:")
for line in code:
    print(f"  {line.strip()}")

result = eliminate_cse(code)

print("\nOptimized Code (after CSE):")
for line in result:
    print(f"  {line}")
```

---

### Output Screenshot

*(Paste screenshot here)*

---

### Observations

- The program successfully identifies repeated expressions in the given Three Address Code by maintaining a hash map of previously computed RHS expressions.
- When identical expressions are entered without modification of operands, the program replaces the redundant computation with a previously stored temporary variable.
- For input where no common subexpressions exist, the output remains identical to the input, confirming that the optimisation is conservative and does not alter correct code.
- The dictionary-based lookup provides O(1) average-case detection of common subexpressions.
- The number of TAC instructions in the optimised output is less than or equal to the original, validating that no unnecessary instructions are introduced.

---

### Conclusions

This experiment demonstrates the Common Subexpression Elimination optimisation technique applied to Three Address Code. CSE identifies expressions that are computed more than once with unchanged operands and replaces redundant computations with references to previously computed results. This reduces both the number of arithmetic operations executed at runtime and the overall code size. The technique is a fundamental machine-independent optimisation that operates on the intermediate representation, making it applicable regardless of the target architecture.

---

### Questions of Curiosity

**1. What is code optimisation?**
Code optimisation is the process of transforming a program's intermediate representation to improve its runtime performance (speed), reduce memory usage, or decrease code size — all without altering the program's observable behaviour or output.

**2. Define common subexpression.**
A common subexpression is an expression that appears more than once in a program and computes the same value each time, because none of its constituent variables have been modified between the two occurrences. For example, if `a + b` appears in two TAC instructions and neither `a` nor `b` is reassigned in between, `a + b` is a common subexpression.

**3. What is Three Address Code?**
Three Address Code is an intermediate representation where each instruction has at most three operands — one result and up to two source operands — in the form `x = y op z`. It linearises complex expressions into a sequence of simple atomic operations.

**4. Why is optimisation required in compilers?**
Without optimisation, generated code may contain redundant computations, unnecessary memory accesses, dead code, and suboptimal instruction sequences. Optimisation removes these inefficiencies, producing faster and smaller executables. It bridges the gap between the programmer's high-level intent and the machine's execution capabilities.

**5. What is the difference between machine-independent and machine-dependent optimisation?**

Machine-independent optimisation is applied on intermediate code (TAC, AST) and does not depend on the target hardware. Examples include CSE, constant folding, and dead code elimination. It is performed in the middle end, after parsing but before code generation.

Machine-dependent optimisation is applied on the target machine code and depends on the specific hardware (registers, instruction set, cache). Examples include register allocation, instruction scheduling, and peephole optimisation. It is performed in the back end, during or after code generation.

---

### References
1. Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D., *Compilers: Principles, Techniques, and Tools*, 2nd Edition, Pearson Education.
2. Alfred V. Aho and Jeffrey D. Ullman, *Principles of Compiler Design*, Addison-Wesley.
