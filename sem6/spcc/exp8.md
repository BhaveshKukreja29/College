# Experiment No. 08
## Implement Code Generation Algorithm

**Aim:**
To write a program to implement a code generation algorithm that converts intermediate representation (Three Address Code) into target machine code or assembly-like instructions.

**Prerequisite:**
- Programming Language (Python)

**Course Outcome:**
After successful completion of this experiment students will be able to identify and validate tokens for a given high level language and implement the synthesis phase of the compiler.

**Software used:**
- Operating System: Windows / Linux
- Python compiler

---

### Theory

Code Generation is the final phase of a compiler. It converts the intermediate code produced by earlier phases (lexical analysis, parsing, intermediate code generation) into target machine code.

The main objectives of code generation are:
- Produce correct target code
- Use efficient instructions
- Optimise register usage

Typically, the input to the code generator is Three Address Code (TAC) such as:
```
t1 = a + b
t2 = t1 * c
d = t2
```

The output is assembly-like instructions:
```
MOV R1, a
ADD R1, b
MOV R2, t1
MUL R2, c
MOV d, R2
```

---

### Algorithm

For each statement `x = y op z`:
1. Use `getreg()` to select a register L to store the result.
2. Find the current location of y from the address descriptor.
3. If y is not already in L, generate: `MOV y → L`
4. Find the current location of z from the address descriptor.
5. Generate the operation instruction: `OP z → L` (e.g., ADD, SUB, MUL, DIV)
6. Store the result x in location L and update the address descriptor of x.
7. Remove x from other locations except L.
8. Update register descriptors — free registers holding y or z if they have no next use and are not live after the block.

---

### Procedure

1. Write and save the Python program.
2. Run the program.
3. Enter TAC lines as input.
4. Observe the generated target code.

---

### Tasks

1. Accept a three-address statement of the form `x = y op z` as input.
2. Generate the corresponding target code instructions.
3. Display the generated assembly-like instructions such as MOV, ADD, SUB, MUL, DIV.
4. Verify the output for different operators.

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

**File: `exp8.py`**

```python
OP_MAP = {
    '+': 'ADD',
    '-': 'SUB',
    '*': 'MUL',
    '/': 'DIV',
}

reg_count = 0

def getreg():
    global reg_count
    reg_count += 1
    return f"R{reg_count}"


def generate(tac_lines):
    code = []

    for line in tac_lines:
        parts = line.split('=', 1)
        lhs = parts[0].strip()
        rhs = parts[1].strip().split()

        if len(rhs) == 1:
            # simple assignment: x = y
            r = getreg()
            code.append(f"MOV {r}, {rhs[0]}")
            code.append(f"MOV {lhs}, {r}")

        elif len(rhs) == 3:
            # x = y op z
            y, op, z = rhs
            r = getreg()
            code.append(f"MOV {r}, {y}")
            code.append(f"{OP_MAP[op]} {r}, {z}")
            code.append(f"MOV {lhs}, {r}")

    return code


n = int(input("Enter number of TAC lines: "))
tac = []
for i in range(n):
    tac.append(input(f"  Line {i + 1}: "))

print("\nInput TAC:")
for line in tac:
    print(f"  {line}")

result = generate(tac)

print("\nGenerated Target Code:")
for line in result:
    print(f"  {line}")
```

---

### Output Screenshot

*(Paste screenshot here)*

---

### Observations

- The program correctly maps arithmetic operators (+, -, *, /) to their corresponding assembly mnemonics (ADD, SUB, MUL, DIV).
- For each TAC instruction x = y op z, three assembly instructions are generated: MOV to load the first operand into a register, the operation instruction, and MOV to store the result.
- Simple assignments of the form x = y generate two instructions: a MOV into a register and a MOV to the target variable.
- Registers are allocated sequentially using getreg(), assigning R1, R2, R3, etc. in order.
- The generated code correctly preserves the evaluation order of the original TAC.

---

### Conclusions

This experiment demonstrates the final phase of compilation — code generation — where Three Address Code is translated into assembly-like target instructions. The getreg() function provides a simple sequential register allocation strategy, and the operator-to-mnemonic mapping (OP_MAP) converts high-level operators into machine instruction names. While this implementation uses a naive register allocation scheme (new register per instruction), it validates the core code generation pipeline: parsing TAC, selecting registers, emitting load/operate/store sequences, and producing correct target code.

---

### Questions of Curiosity

1. What is the purpose of a code generator?
The code generator translates intermediate representation (such as TAC) into target machine code or assembly language. It is the final phase of the compiler and must produce correct, efficient code that faithfully implements the semantics of the source program.

2. What is a register descriptor?
A register descriptor tracks the current contents of each machine register at any point during code generation. It records which variables or temporaries are currently stored in each register, enabling the code generator to avoid unnecessary loads.

3. What is an address descriptor?
An address descriptor tracks where the current value of each variable or temporary is stored — it could be in a register, a memory location, or both. This information helps the code generator decide whether a MOV instruction is needed before an operation.

4. What is the function of getreg() in code generation?
getreg() is a register allocation function that selects an available register to hold the result of a computation. In a simple implementation it returns the next available register; in optimised compilers it considers register availability, variable liveness, and spilling strategies.

5. Why are registers used in code generation?
Registers are the fastest storage locations in a CPU — significantly faster than main memory. Using registers for intermediate computations minimises memory accesses and improves execution speed. Effective register allocation is one of the most impactful optimisations a compiler can perform.

6. What are the common target instructions used in code generation?
MOV (data transfer), ADD (addition), SUB (subtraction), MUL (multiplication), DIV (division), CMP (comparison), JMP (unconditional jump), JZ/JNZ (conditional jumps), PUSH/POP (stack operations), and CALL/RET (function call/return).

7. What is the output of the code generation phase?
The output is target machine code — either assembly language instructions or actual binary machine code. This is the final output of the compiler, ready to be assembled/linked and executed on the target hardware.

---

### References
1. Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D., *Compilers: Principles, Techniques, and Tools*, 2nd Edition, Pearson Education.
2. Alfred V. Aho and Jeffrey D. Ullman, *Principles of Compiler Design*, Addison-Wesley.
