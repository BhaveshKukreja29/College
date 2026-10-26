# Experiment No. 09
## Implementation of Two Pass Macroprocessor

**Aim:**
To study and implement the working of a Two Pass Macroprocessor using a sample assembly program and understand the generation of MDT, MNT, and ALA tables.

**Prerequisite:**
- Programming Language (C)

**Course Outcome:**
After successful completion of this experiment students will be able to implement a Two Pass Macro Processor.

**Software used:**
- Operating System: Windows / Linux
- Compiler: GCC
- Text editor (gedit / VS Code)

---

### Theory

A macroprocessor is a system software component that allows programmers to define macros (a sequence of instructions) and reuse them multiple times in a program. When a macro is called, the macroprocessor replaces the macro call with the macro body.

A Two Pass Macroprocessor processes the source program in two passes:

**Pass 1** — Processes macro definitions and stores them in tables:
- **MNT (Macro Name Table)** — Stores macro name and pointer to MDT
- **MDT (Macro Definition Table)** — Stores macro body with formal parameters replaced by positional indices
- **ALA (Argument List Array)** — Stores formal/actual arguments used in macro

**Pass 2** — Expands macro calls:
- Detects macro calls in the intermediate code
- Looks up the macro in MNT
- Fetches the macro body from MDT
- Replaces positional indices with actual parameters using ALA
- Produces the final expanded assembly code

#### Sample Input (input9.txt)

```
PRG  START  0
MACRO
&LAB  INCR   &ARG1, &ARG2, &ARG3
&LAB  A  1, &ARG1
      A  2, &ARG2
      A  3, &ARG3
MEND
LOOP1 INCR   DATA1, DATA2, DATA3
DATA1  DC  F'5'
DATA2  DC  F'10'
DATA3  DC  F'15'
```

---

### Algorithm

**Pass 1 Algorithm:**
1. Read the source program line by line.
2. If MACRO statement is encountered: read prototype, enter name in MNT, store body in MDT until MEND.
3. Store non-macro statements in intermediate file.

**Pass 2 Algorithm:**
1. Read intermediate code line by line.
2. If macro call found: look up MNT, fetch body from MDT, substitute actual params.
3. Write expanded statements to output.

---

### Procedure

1. Save the input assembly program in `input9.txt`.
2. Compile: `gcc exp9.c -o exp9`
3. Run: `./exp9`
4. Observe output files: `mnt.txt`, `mdt.txt`, `intermediate9.txt`, `expanded.txt`

---

### Tasks

1. Read an assembly language source program containing macro definitions and macro calls from a file.
2. In Pass 1, identify macro definitions and store them in MNT and MDT while generating intermediate code.
3. In Pass 2, expand macro calls by replacing them with the corresponding macro body from MDT.
4. Write generated tables and expanded program to output files.

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

**File: `exp9.c`**

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_LINES 100
#define MAX_LEN 200
#define MAX_PARAMS 10

typedef struct {
    char name[30];
    int mdt_index;
} MNTEntry;

typedef struct {
    char line[MAX_LEN];
} MDTEntry;

typedef struct {
    char formal[MAX_PARAMS][30];
    int count;
} ALAEntry;

MNTEntry mnt[20];
int mnt_count = 0;
MDTEntry mdt[MAX_LINES];
int mdt_count = 0;
ALAEntry ala[20];
char intermediate[MAX_LINES][MAX_LEN];
int inter_count = 0;

void replace_params(char *line, ALAEntry *a) {
    char result[MAX_LEN] = "";
    char temp[MAX_LEN];
    strcpy(temp, line);

    for (int i = 0; i < a->count; i++) {
        char idx[10];
        sprintf(idx, "#%d", i);
        char *pos;
        result[0] = '\0';
        char *start = temp;
        while ((pos = strstr(start, a->formal[i])) != NULL) {
            strncat(result, start, pos - start);
            strcat(result, idx);
            start = pos + strlen(a->formal[i]);
        }
        strcat(result, start);
        strcpy(temp, result);
        result[0] = '\0';
    }
    strcpy(line, temp);
}

void pass1(char source[][MAX_LEN], int src_count) {
    int i = 0;
    while (i < src_count) {
        char line[MAX_LEN];
        strcpy(line, source[i]);

        char *p = line;
        while (*p == ' ' || *p == '\t') p++;
        char trimmed[MAX_LEN];
        strcpy(trimmed, p);

        if (strcmp(trimmed, "MACRO") == 0) {
            i++;
            char proto[MAX_LEN];
            strcpy(proto, source[i]);

            char *tokens[20];
            int tok_count = 0;
            char proto_copy[MAX_LEN];
            strcpy(proto_copy, proto);
            char *tok = strtok(proto_copy, " ,\t\n");
            while (tok) {
                tokens[tok_count++] = tok;
                tok = strtok(NULL, " ,\t\n");
            }

            char macro_name[30] = "";
            ala[mnt_count].count = 0;

            for (int j = 0; j < tok_count; j++) {
                if (tokens[j][0] == '&') {
                    strcpy(ala[mnt_count].formal[ala[mnt_count].count], tokens[j]);
                    ala[mnt_count].count++;
                } else if (macro_name[0] == '\0') {
                    strcpy(macro_name, tokens[j]);
                }
            }

            strcpy(mnt[mnt_count].name, macro_name);
            mnt[mnt_count].mdt_index = mdt_count + 1;

            char mdt_line[MAX_LEN];
            strcpy(mdt_line, proto);
            replace_params(mdt_line, &ala[mnt_count]);
            strcpy(mdt[mdt_count++].line, mdt_line);

            i++;
            while (i < src_count) {
                strcpy(line, source[i]);
                p = line;
                while (*p == ' ' || *p == '\t') p++;
                strcpy(trimmed, p);

                if (strcmp(trimmed, "MEND") == 0) {
                    strcpy(mdt[mdt_count++].line, "MEND");
                    break;
                }
                char body[MAX_LEN];
                strcpy(body, source[i]);
                replace_params(body, &ala[mnt_count]);
                strcpy(mdt[mdt_count++].line, body);
                i++;
            }
            mnt_count++;
            i++;
        } else {
            strcpy(intermediate[inter_count++], source[i]);
            i++;
        }
    }
}

void pass2(FILE *fout) {
    for (int i = 0; i < inter_count; i++) {
        char parts[20][30];
        int part_count = 0;
        char copy[MAX_LEN];
        strcpy(copy, intermediate[i]);
        char *tok = strtok(copy, " ,\t\n");
        while (tok) {
            strcpy(parts[part_count++], tok);
            tok = strtok(NULL, " ,\t\n");
        }

        int found = -1;
        int name_idx = -1;
        for (int m = 0; m < mnt_count; m++) {
            for (int j = 0; j < part_count; j++) {
                if (strcmp(parts[j], mnt[m].name) == 0) {
                    found = m;
                    name_idx = j;
                    break;
                }
            }
            if (found >= 0) break;
        }

        if (found < 0) {
            fprintf(fout, "%s\n", intermediate[i]);
        } else {
            char actual[MAX_PARAMS][30];
            int actual_count = 0;
            if (name_idx > 0)
                strcpy(actual[actual_count++], parts[name_idx - 1]);
            else
                strcpy(actual[actual_count++], "");
            for (int j = name_idx + 1; j < part_count; j++)
                strcpy(actual[actual_count++], parts[j]);

            int idx = mnt[found].mdt_index;
            while (idx < mdt_count && strcmp(mdt[idx].line, "MEND") != 0) {
                char expanded[MAX_LEN];
                strcpy(expanded, mdt[idx].line);
                for (int j = 0; j < actual_count; j++) {
                    char placeholder[10];
                    sprintf(placeholder, "#%d", j);
                    char result[MAX_LEN] = "";
                    char *start = expanded;
                    char *pos;
                    while ((pos = strstr(start, placeholder)) != NULL) {
                        strncat(result, start, pos - start);
                        strcat(result, actual[j]);
                        start = pos + strlen(placeholder);
                    }
                    strcat(result, start);
                    strcpy(expanded, result);
                }
                fprintf(fout, "%s\n", expanded);
                idx++;
            }
        }
    }
}

int main() {
    FILE *fin = fopen("input9.txt", "r");
    if (!fin) {
        printf("Error: cannot open input9.txt\n");
        return 1;
    }

    char source[MAX_LINES][MAX_LEN];
    int src_count = 0;
    while (fgets(source[src_count], MAX_LEN, fin)) {
        source[src_count][strcspn(source[src_count], "\n")] = '\0';
        src_count++;
    }
    fclose(fin);

    pass1(source, src_count);

    FILE *fmnt = fopen("mnt.txt", "w");
    fprintf(fmnt, "%-8s%-15s%s\n", "Index", "Name", "MDT Index");
    for (int i = 0; i < mnt_count; i++)
        fprintf(fmnt, "%-8d%-15s%d\n", i + 1, mnt[i].name, mnt[i].mdt_index);
    fclose(fmnt);

    FILE *fmdt = fopen("mdt.txt", "w");
    fprintf(fmdt, "%-8s%s\n", "Index", "Definition");
    for (int i = 0; i < mdt_count; i++)
        fprintf(fmdt, "%-8d%s\n", i + 1, mdt[i].line);
    fclose(fmdt);

    FILE *finter = fopen("intermediate9.txt", "w");
    for (int i = 0; i < inter_count; i++)
        fprintf(finter, "%s\n", intermediate[i]);
    fclose(finter);

    FILE *fout = fopen("expanded.txt", "w");
    pass2(fout);
    fclose(fout);

    printf("===== PASS 1 OUTPUT =====\n");
    printf("\nMacro Name Table (MNT):\n");
    printf("  %-8s%-15s%s\n", "Index", "Name", "MDT Index");
    for (int i = 0; i < mnt_count; i++)
        printf("  %-8d%-15s%d\n", i + 1, mnt[i].name, mnt[i].mdt_index);

    printf("\nMacro Definition Table (MDT):\n");
    printf("  %-8s%s\n", "Index", "Definition");
    for (int i = 0; i < mdt_count; i++)
        printf("  %-8d%s\n", i + 1, mdt[i].line);

    printf("\nIntermediate Code:\n");
    for (int i = 0; i < inter_count; i++)
        printf("  %s\n", intermediate[i]);

    printf("\n===== PASS 2 OUTPUT =====\n");
    printf("\nExpanded Source Program:\n");
    FILE *fread = fopen("expanded.txt", "r");
    char buf[MAX_LEN];
    while (fgets(buf, MAX_LEN, fread))
        printf("  %s", buf);
    fclose(fread);

    printf("\n\nOutput files: mnt.txt, mdt.txt, intermediate9.txt, expanded.txt\n");
    return 0;
}
```

**How to run:**
```
gcc exp9.c -o exp9
./exp9
```

---

### Output Screenshot

*(Paste screenshot here)*

---

### Observations

- Pass 1 correctly identifies MACRO and MEND delimiters and extracts the macro prototype and body from the input file.
- The Macro Name Table (MNT) stores the macro name with a pointer to the corresponding entry in the MDT, enabling quick lookup during Pass 2.
- The Macro Definition Table (MDT) stores the macro body with formal parameters replaced by positional indices (#0, #1, #2, #3), making parameter substitution straightforward during expansion.
- The intermediate code produced after Pass 1 contains no macro definitions — only regular statements and macro calls remain.
- Pass 2 correctly expands macro calls by substituting actual parameters for the positional indices in the MDT, producing the final expanded assembly program written to `expanded.txt`.

---

### Conclusions

This experiment demonstrates the working of a Two Pass Macroprocessor implemented in C with file I/O. Pass 1 processes macro definitions — building the MNT, MDT, and ALA tables while stripping macro definitions from the source to produce intermediate code. Pass 2 scans this intermediate code for macro calls, looks up the macro body in the MDT via the MNT, and performs parameter substitution using the ALA to produce the final expanded program. All tables and results are written to separate output files for verification.

---

### Questions of Curiosity

**1. What is a macroprocessor?**
A macroprocessor is system software that processes macro definitions and macro calls in a source program. It replaces each macro call with the corresponding macro body (expansion), performing text substitution before the assembler or compiler processes the program.

**2. What is the difference between single pass and multi pass macroprocessor?**
A single pass macroprocessor processes the source in one scan — it requires macros to be defined before they are called. A multi pass (two pass) macroprocessor uses the first pass to collect all macro definitions into tables, and the second pass to expand macro calls. This allows macros to be defined anywhere in the source.

**3. What is Macro Name Table (MNT)?**
The MNT stores the name of each macro along with a pointer (index) to its definition in the MDT. During Pass 2, when a macro call is encountered, the MNT is searched to locate the corresponding macro body.

**4. What is Macro Definition Table (MDT)?**
The MDT stores the body of each macro definition. Formal parameters in the body are replaced by positional indices (#0, #1, etc.) during Pass 1. During expansion in Pass 2, these indices are substituted with actual argument values.

**5. What is the purpose of MEND in macro definition?**
MEND marks the end of a macro definition body. It tells the macroprocessor where the macro body terminates, similar to how END marks the end of a program.

**6. What happens during Pass 1 of a macroprocessor?**
Pass 1 reads the source program, identifies macro definitions (between MACRO and MEND), extracts formal parameters, and stores the macro name in MNT and the macro body in MDT. It also generates an intermediate file containing only non-macro statements and macro calls.

**7. What happens during Pass 2 of a macroprocessor?**
Pass 2 reads the intermediate code, detects macro calls, looks up the macro in MNT, fetches its body from MDT, substitutes actual parameters for positional indices using ALA, and writes the expanded assembly code to the output file.

**8. What are the advantages of macros?**
Macros reduce code repetition — frequently used instruction sequences can be defined once and reused multiple times. They improve readability, reduce program size at the source level, and simplify maintenance since changes to a macro definition automatically apply to all its call sites.

---

### References
1. Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D., *Compilers: Principles, Techniques, and Tools*, 2nd Edition, Pearson Education.
2. Alfred V. Aho and Jeffrey D. Ullman, *Principles of Compiler Design*, Addison-Wesley.
