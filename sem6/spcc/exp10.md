# Experiment No. 10
## Implementation of Two Pass Assembler

**Aim:**
To implement a Two Pass Assembler and generate Intermediate Code (Pass I), Symbol Table (SYMTAB), and Final Machine Code (Pass II).

**Prerequisite:**
- Programming Language (C)

**Course Outcome:**
After successful completion of this experiment students will be able to generate machine code by implementing two pass assemblers.

**Software used:**
- Operating System: Windows / Linux
- Compiler: GCC
- Text editor (gedit / VS Code)

---

### Theory

An Assembler is system software that translates an assembly language program into machine language.

**Pass I:**
- Scans the program
- Assigns addresses to symbols
- Generates Symbol Table (SYMTAB) and Intermediate Code (IC)

**Pass II:**
- Uses intermediate code and symbol table
- Replaces symbolic addresses with actual addresses
- Generates final machine code

#### Input Program (input10.txt)

```
START 501
READ A
READ B
MOVER AREG A
ADD AREG B
MOVEM AREG C
PRINT C
A DS 1
B DS 1
C DS 1
END
```

#### OPTAB (Mnemonic Table)

| Mnemonic | Class | Opcode |
|----------|-------|--------|
| READ     | IS    | 09     |
| MOVER    | IS    | 04     |
| ADD      | IS    | 01     |
| MOVEM    | IS    | 05     |
| PRINT    | IS    | 10     |
| START    | AD    | 01     |
| END      | AD    | 02     |
| DS       | DL    | 02     |
| DC       | DL    | 01     |

---

### Algorithm

**Pass I Algorithm:**
1. Initialize Location Counter (LC).
2. If START, initialize LC to the given value.
3. For each instruction: if label present, add to SYMTAB; generate intermediate code; update LC.
4. Stop at END.

**Pass II Algorithm:**
1. Read intermediate code.
2. Replace symbolic addresses using SYMTAB.
3. Generate machine code.
4. Output final object code.

---

### Procedure

1. Save the input assembly program in `input10.txt`.
2. Compile: `gcc exp10.c -o exp10`
3. Run: `./exp10`
4. Observe output files: `symtab.txt`, `ic.txt`, `output10.txt`

---

### Tasks

1. In Pass I: read the assembly program, maintain LC, generate IC, construct SYMTAB.
2. In Pass II: read IC, replace symbolic operands using SYMTAB, generate final machine code.
3. Display IC, SYMTAB, and machine code.

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

**File: `exp10.c`**

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 50
#define LEN 100

typedef struct {
    char mnemonic[10];
    char cls[5];      // IS, DL, AD
    int opcode;
} OPTABEntry;

typedef struct {
    char symbol[20];
    int address;
} SYMTABEntry;

typedef struct {
    char ic[LEN];
} ICEntry;

OPTABEntry optab[] = {
    {"READ",  "IS", 9},
    {"MOVER", "IS", 4},
    {"MOVEM", "IS", 5},
    {"ADD",   "IS", 1},
    {"SUB",   "IS", 2},
    {"MULT",  "IS", 3},
    {"PRINT", "IS", 10},
    {"COMP",  "IS", 6},
    {"BC",    "IS", 7},
    {"DIV",   "IS", 8},
    {"START", "AD", 1},
    {"END",   "AD", 2},
    {"DS",    "DL", 2},
    {"DC",    "DL", 1},
};
int optab_size = sizeof(optab) / sizeof(optab[0]);

SYMTABEntry symtab[MAX];
int sym_count = 0;
ICEntry ic[MAX];
int ic_count = 0;

int find_optab(char *mnemonic) {
    for (int i = 0; i < optab_size; i++)
        if (strcmp(optab[i].mnemonic, mnemonic) == 0)
            return i;
    return -1;
}

int find_symbol(char *name) {
    for (int i = 0; i < sym_count; i++)
        if (strcmp(symtab[i].symbol, name) == 0)
            return i;
    return -1;
}

int add_symbol(char *name, int addr) {
    int idx = find_symbol(name);
    if (idx >= 0) {
        symtab[idx].address = addr;
        return idx;
    }
    strcpy(symtab[sym_count].symbol, name);
    symtab[sym_count].address = addr;
    return sym_count++;
}

int get_reg_code(char *reg) {
    if (strcmp(reg, "AREG") == 0) return 1;
    if (strcmp(reg, "BREG") == 0) return 2;
    if (strcmp(reg, "CREG") == 0) return 3;
    if (strcmp(reg, "DREG") == 0) return 4;
    return 0;
}

void pass1(char lines[][LEN], int line_count) {
    int lc = 0;

    for (int i = 0; i < line_count; i++) {
        char copy[LEN];
        strcpy(copy, lines[i]);
        char *tokens[10];
        int tok_count = 0;
        char *tok = strtok(copy, " \t\n");
        while (tok && tok_count < 10) {
            tokens[tok_count++] = tok;
            tok = strtok(NULL, " \t\n");
        }
        if (tok_count == 0) continue;

        int opidx = -1;
        int label_present = 0;
        char label[20] = "";

        opidx = find_optab(tokens[0]);
        if (opidx < 0 && tok_count > 1) {
            strcpy(label, tokens[0]);
            label_present = 1;
            opidx = find_optab(tokens[1]);
        }

        if (opidx < 0) continue;

        OPTABEntry *op = &optab[opidx];
        int mnemonic_idx = label_present ? 1 : 0;

        if (strcmp(op->cls, "AD") == 0) {
            if (strcmp(op->mnemonic, "START") == 0) {
                lc = atoi(tokens[mnemonic_idx + 1]);
                sprintf(ic[ic_count++].ic, "(AD, %02d) (C, %d)", op->opcode, lc);
            } else if (strcmp(op->mnemonic, "END") == 0) {
                sprintf(ic[ic_count++].ic, "(AD, %02d)", op->opcode);
            }
        } else if (strcmp(op->cls, "IS") == 0) {
            if (label_present)
                add_symbol(label, lc);

            if (tok_count > mnemonic_idx + 2) {
                int reg = get_reg_code(tokens[mnemonic_idx + 1]);
                char *operand = tokens[mnemonic_idx + 2];
                int sym_idx = find_symbol(operand);
                if (sym_idx < 0) sym_idx = add_symbol(operand, -1);
                sprintf(ic[ic_count++].ic, "(IS, %02d) (%d) (S, %02d)",
                        op->opcode, reg, sym_idx + 1);
            } else {
                char *operand = tokens[mnemonic_idx + 1];
                int sym_idx = find_symbol(operand);
                if (sym_idx < 0) sym_idx = add_symbol(operand, -1);
                sprintf(ic[ic_count++].ic, "(IS, %02d) (S, %02d)",
                        op->opcode, sym_idx + 1);
            }
            lc++;
        } else if (strcmp(op->cls, "DL") == 0) {
            if (label_present)
                add_symbol(label, lc);
            int val = atoi(tokens[mnemonic_idx + 1]);
            sprintf(ic[ic_count++].ic, "(DL, %02d) (C, %d)", op->opcode, val);
            lc++;
        }
    }
}

void pass2(FILE *fout) {
    int lc = -1;
    for (int i = 0; i < ic_count; i++) {
        char copy[LEN];
        strcpy(copy, ic[i].ic);

        char cls[5];
        int opcode;
        sscanf(copy, "(%[^,], %d)", cls, &opcode);

        if (strcmp(cls, "AD") == 0) {
            if (opcode == 1) {
                char *cpos = strstr(copy, "(C,");
                if (cpos) sscanf(cpos, "(C, %d)", &lc);
            }
            continue;
        }

        if (strcmp(cls, "DL") == 0) {
            fprintf(fout, "%d\n", lc);
            printf("  %d\n", lc);
            lc++;
            continue;
        }

        int reg = 0, sym_idx = 0;
        char *s_pos = strstr(copy, "(S,");
        if (s_pos) sscanf(s_pos, "(S, %d)", &sym_idx);

        int groups = 0;
        for (char *p = copy; *p; p++)
            if (*p == '(') groups++;

        if (groups == 3) {
            char *second = strchr(copy, ')');
            if (second) {
                second++;
                while (*second == ' ') second++;
                sscanf(second, "(%d)", &reg);
            }
        }

        int addr = (sym_idx > 0 && sym_idx <= sym_count)
                   ? symtab[sym_idx - 1].address : 0;
        fprintf(fout, "%d +%02d %d %d\n", lc, opcode, reg, addr);
        printf("  %d +%02d %d %d\n", lc, opcode, reg, addr);
        lc++;
    }
}

int main() {
    FILE *fin = fopen("input10.txt", "r");
    if (!fin) {
        printf("Error: cannot open input10.txt\n");
        return 1;
    }

    char lines[MAX][LEN];
    int line_count = 0;
    while (fgets(lines[line_count], LEN, fin)) {
        lines[line_count][strcspn(lines[line_count], "\n")] = '\0';
        line_count++;
    }
    fclose(fin);

    pass1(lines, line_count);

    FILE *fsym = fopen("symtab.txt", "w");
    fprintf(fsym, "%-8s%-15s%s\n", "Index", "Symbol", "Address");
    printf("===== PASS 1 OUTPUT =====\n");
    printf("\nSymbol Table (SYMTAB):\n");
    printf("  %-8s%-15s%s\n", "Index", "Symbol", "Address");
    for (int i = 0; i < sym_count; i++) {
        fprintf(fsym, "%-8d%-15s%d\n", i + 1, symtab[i].symbol, symtab[i].address);
        printf("  %-8d%-15s%d\n", i + 1, symtab[i].symbol, symtab[i].address);
    }
    fclose(fsym);

    FILE *fic = fopen("ic.txt", "w");
    printf("\nIntermediate Code (IC):\n");
    for (int i = 0; i < ic_count; i++) {
        fprintf(fic, "%s\n", ic[i].ic);
        printf("  %s\n", ic[i].ic);
    }
    fclose(fic);

    printf("\n===== PASS 2 OUTPUT =====\n");
    printf("\nMachine Code:\n");
    FILE *fout = fopen("output10.txt", "w");
    pass2(fout);
    fclose(fout);

    printf("\nOutput files: symtab.txt, ic.txt, output10.txt\n");
    return 0;
}
```

**How to run:**
```
gcc exp10.c -o exp10
./exp10
```

---

### Output Screenshot

*(Paste screenshot here)*

---

### Observations

- The Location Counter (LC) starts from the value specified in the START directive (501 in this case) and increments by 1 for each instruction or declarative statement.
- All symbols (A, B, C) are assigned sequential memory addresses (507, 508, 509) after the executable instructions.
- Declarative statements (DS) reserve memory but do not generate machine instructions — only the address is recorded in the machine code output.
- The intermediate code uses a tuple format: (class, opcode) (register) (symbol_index), which simplifies address resolution in Pass II.
- The Symbol Table is used in Pass II to resolve symbolic references — each symbol index in the IC is replaced with the actual memory address from SYMTAB.
- Output files (symtab.txt, ic.txt, output10.txt) are generated for verification.

---

### Conclusions

This experiment demonstrates the implementation of a Two Pass Assembler in C. Pass I scans the assembly source, maintains a Location Counter, builds the Symbol Table, and generates Intermediate Code using an OPTAB-based classification (IS, DL, AD). Pass II reads the IC, resolves symbolic addresses using the SYMTAB, and produces the final machine code. The two-pass approach allows forward references — symbols can be used before they are defined, since Pass I collects all symbol addresses before Pass II generates the final code.

---

### Questions of Curiosity

**1. What is an assembler?**
An assembler is system software that translates assembly language programs (mnemonics like ADD, MOV) into machine language (binary opcodes and addresses). It maps symbolic instructions to their numeric equivalents using an opcode table.

**2. What is the difference between a one pass and two pass assembler?**
A one pass assembler processes the source in a single scan — it must handle forward references by backpatching. A two pass assembler uses the first pass to build the symbol table and the second pass to generate machine code, naturally resolving all forward references.

**3. What is SYMTAB?**
SYMTAB (Symbol Table) is a data structure that stores each symbol (label) encountered in the source program along with its assigned memory address. It is built during Pass I and used during Pass II for address resolution.

**4. What is intermediate code?**
Intermediate code is the output of Pass I — a representation of the source program where mnemonics are replaced by (class, opcode) tuples and operands are represented as symbol table indices or constants. It simplifies Pass II processing.

**5. Why is Pass II required?**
Pass II is required to generate the actual machine code. Pass I only builds tables and generates intermediate code with symbolic references. Pass II resolves these references using the completed SYMTAB and produces the final binary-equivalent output.

**6. What is the role of a location counter?**
The Location Counter (LC) tracks the memory address assigned to each instruction or data item. It is initialised by the START directive and incremented after each instruction, ensuring sequential address assignment.

**7. What are IS, DL, and AD?**
These are instruction classes used in the OPTAB:
- IS (Imperative Statement) — executable instructions like ADD, MOVER, READ
- DL (Declarative Statement) — data declaration directives like DS (Define Storage), DC (Define Constant)
- AD (Assembler Directive) — directives that control the assembler like START, END

---

### References
1. L. L. Dhamdhere, *Systems Programming and Operating Systems*, 2nd ed., McGraw-Hill Education, 2011.
2. S. Pal, *Systems Programming*, Oxford University Press, 2011.
