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

        // check if first token is a mnemonic
        opidx = find_optab(tokens[0]);
        if (opidx < 0 && tok_count > 1) {
            // first token is a label
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
                // has register and operand: MOVER AREG A
                int reg = get_reg_code(tokens[mnemonic_idx + 1]);
                char *operand = tokens[mnemonic_idx + 2];
                int sym_idx = find_symbol(operand);
                if (sym_idx < 0) sym_idx = add_symbol(operand, -1);
                sprintf(ic[ic_count++].ic, "(IS, %02d) (%d) (S, %02d)", op->opcode, reg, sym_idx + 1);
            } else {
                // no register: READ A, PRINT C
                char *operand = tokens[mnemonic_idx + 1];
                int sym_idx = find_symbol(operand);
                if (sym_idx < 0) sym_idx = add_symbol(operand, -1);
                sprintf(ic[ic_count++].ic, "(IS, %02d) (S, %02d)", op->opcode, sym_idx + 1);
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

        // parse class and opcode
        char cls[5];
        int opcode;
        sscanf(copy, "(%[^,], %d)", cls, &opcode);

        if (strcmp(cls, "AD") == 0) {
            if (opcode == 1) {
                // START: extract LC
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

        // IS instruction
        // check if it has register
        int reg = 0, sym_idx = 0;
        char *s_pos = strstr(copy, "(S,");
        if (s_pos) sscanf(s_pos, "(S, %d)", &sym_idx);

        // count parentheses groups to see if reg is present
        int groups = 0;
        for (char *p = copy; *p; p++)
            if (*p == '(') groups++;

        if (groups == 3) {
            // has register: (IS, op) (reg) (S, idx)
            char *second = strchr(copy, ')');
            if (second) {
                second++;
                while (*second == ' ') second++;
                sscanf(second, "(%d)", &reg);
            }
        }

        int addr = (sym_idx > 0 && sym_idx <= sym_count) ? symtab[sym_idx - 1].address : 0;
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

    // write SYMTAB
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

    // write IC
    FILE *fic = fopen("ic.txt", "w");
    printf("\nIntermediate Code (IC):\n");
    for (int i = 0; i < ic_count; i++) {
        fprintf(fic, "%s\n", ic[i].ic);
        printf("  %s\n", ic[i].ic);
    }
    fclose(fic);

    // Pass 2
    printf("\n===== PASS 2 OUTPUT =====\n");
    printf("\nMachine Code:\n");
    FILE *fout = fopen("output10.txt", "w");
    pass2(fout);
    fclose(fout);

    printf("\nOutput files: symtab.txt, ic.txt, output10.txt\n");
    return 0;
}
