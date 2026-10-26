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

        // trim
        char *p = line;
        while (*p == ' ' || *p == '\t') p++;
        char trimmed[MAX_LEN];
        strcpy(trimmed, p);

        if (strcmp(trimmed, "MACRO") == 0) {
            i++;
            char proto[MAX_LEN];
            strcpy(proto, source[i]);

            // parse prototype: extract params (&...) and macro name
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

            // store prototype in MDT with params replaced
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

        // check if any token is a macro name
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
            // build actual params
            char actual[MAX_PARAMS][30];
            int actual_count = 0;
            if (name_idx > 0)
                strcpy(actual[actual_count++], parts[name_idx - 1]); // label
            else
                strcpy(actual[actual_count++], "");
            for (int j = name_idx + 1; j < part_count; j++)
                strcpy(actual[actual_count++], parts[j]);

            // expand from MDT (skip prototype)
            int idx = mnt[found].mdt_index; // skip prototype (0-indexed: mdt_index is 1-based)
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

    // write MNT
    FILE *fmnt = fopen("mnt.txt", "w");
    fprintf(fmnt, "%-8s%-15s%s\n", "Index", "Name", "MDT Index");
    for (int i = 0; i < mnt_count; i++)
        fprintf(fmnt, "%-8d%-15s%d\n", i + 1, mnt[i].name, mnt[i].mdt_index);
    fclose(fmnt);

    // write MDT
    FILE *fmdt = fopen("mdt.txt", "w");
    fprintf(fmdt, "%-8s%s\n", "Index", "Definition");
    for (int i = 0; i < mdt_count; i++)
        fprintf(fmdt, "%-8d%s\n", i + 1, mdt[i].line);
    fclose(fmdt);

    // write intermediate
    FILE *finter = fopen("intermediate9.txt", "w");
    for (int i = 0; i < inter_count; i++)
        fprintf(finter, "%s\n", intermediate[i]);
    fclose(finter);

    // Pass 2 - expanded output
    FILE *fout = fopen("expanded.txt", "w");
    pass2(fout);
    fclose(fout);

    // print everything to console too
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
