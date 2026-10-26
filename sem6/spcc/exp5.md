# Experiment No. 05
## Construction of an LL(1) Parser

**Aim:**
To design and implement an LL(1) parser for a given context-free grammar and verify whether the grammar satisfies LL(1) conditions using FIRST and FOLLOW sets.

**Prerequisite:**
- Programming Language (Python)

**Course Outcome:**
After successful completion of this experiment students will be able to parse the given input string by constructing top-down / bottom-up parser.

**Software used:**
- Operating System: Windows / Linux
- Python compiler

---

### Theory

An LL(1) parser is a top-down, predictive parser that:
- **L** → Scans input from Left to right
- **L** → Produces a Leftmost derivation
- **1** → Uses 1 lookahead symbol

LL(1) parsing requires:
- No left recursion
- No left factoring ambiguity
- Disjoint FIRST sets for productions
- If ε is present, FIRST and FOLLOW must be disjoint

#### LL(1) Parsing Table Construction

For each production `A → α`:
1. For every terminal `a` ∈ FIRST(α) (except ε), put `A → α` in M[A, a].
2. If ε ∈ FIRST(α), for every terminal `b` ∈ FOLLOW(A), put `A → α` in M[A, b].

If any table entry contains more than one production → grammar is **not** LL(1).

#### Example

Grammar: `S → aA`, `A → b`

| Non-Terminal | a      | b     | $   |
|-------------|--------|-------|-----|
| S           | S → aA |       |     |
| A           |        | A → b |     |

---

### Algorithm

1. Input the grammar G = (V, T, P, S).
2. Compute FIRST sets for all non-terminals.
3. Compute FOLLOW sets for all non-terminals.
4. Initialise parsing table M[A, a] = empty for all A ∈ V, a ∈ T ∪ {$}.
5. For each production A → α:
   - For every terminal a ∈ FIRST(α) (except ε), put A → α in M[A, a].
   - If ε ∈ FIRST(α), for every terminal b ∈ FOLLOW(A), put A → α in M[A, b].
6. If any table entry has more than one production → grammar is not LL(1).

---

### Procedure

1. Write and save the Python program.
2. Run the program.
3. Observe output.

---

### Tasks

1. Write the given context-free grammar.
2. Check for and eliminate left recursion and left factoring if present.
3. Compute FIRST and FOLLOW sets.
4. Construct the LL(1) parsing table.
5. Check for conflicts — if any table entry has two productions, the grammar is not LL(1).
6. Test by parsing a sample input string.

---

> **Roll No.:** 2303080
> **Name:** Bhavesh Kailash Kukreja
> **Program:** SPCC Lab
> **Division:** C2
> **Semester:** 6
> **Batch:** C21
> **Date of Experiment:**
> **Date of Submission:** 07/03/2026
> **Grade:**

---

### Program

**File: `exp5.py`**

```python
# Input Grammar: S->aA, A->b|e
n = int(input("Enter number of productions: "))
prods = [input().replace(" ", "").split("->") for _ in range(n)]
nt_list = list(dict.fromkeys([p[0] for p in prods]))
t_list = list(dict.fromkeys([c for p in prods for c in p[1] if not c.isupper() and c != 'e'])) + ['$']

first = {nt: set() for nt in nt_list}
def get_first(s):
    if not s.isupper(): return {s}
    res = set()
    for head, body in [p for p in prods if p[0] == s]:
        if body == 'e': res.add('e')
        else:
            for char in body:
                f = get_first(char)
                res |= (f - {'e'})
                if 'e' not in f: break
            else: res.add('e')
    return res

for nt in nt_list: first[nt] = get_first(nt)

follow = {nt: set() for nt in nt_list}; follow[nt_list[0]].add('$')
for _ in range(len(nt_list)):
    for head, body in prods:
        for i, char in enumerate(body):
            if char.isupper():
                rest = body[i+1:]
                if not rest: follow[char] |= follow[head]
                else:
                    f_next = get_first(rest[0])
                    follow[char] |= (f_next - {'e'})
                    if 'e' in f_next: follow[char] |= follow[head]

table = {nt: {t: "" for t in t_list} for nt in nt_list}
is_ll1 = True

for head, body in prods:
    f_body = get_first(body[0] if body != 'e' else {'e'})

    for s in f_body:
        if s != 'e':
            if table[head][s]: is_ll1 = False
            table[head][s] = f"{head}->{body}"
        else:
            for f_s in follow[head]:
                if table[head][f_s]: is_ll1 = False
                table[head][s] = f"{head}->{body}"


print("\nFIRST:", first, "\nFOLLOW:", follow)
print("\nTable")
print()
for nt in nt_list:
    print(f"{nt} | " + " | ".join([table[nt][t] or "-" for t in t_list]))

if is_ll1:
    print("Grammar is LL1")
else:
    print("Not LL1")
```

---

### Output Screenshot

*(Paste screenshot here)*

---

### Observations

- The FIRST and FOLLOW sets are correctly computed for all non-terminals using recursive analysis of the grammar productions.
- The parsing table is populated by mapping each production to the appropriate (non-terminal, terminal) cell based on FIRST sets, with epsilon productions handled via FOLLOW sets.
- When no table entry contains more than one production, the grammar is confirmed to be LL(1).
- The program correctly detects conflicts — if two productions map to the same cell, the is_ll1 flag is set to False.
- Terminals are extracted automatically from the production bodies, and $ is appended as the end-of-input marker.

---

### Conclusions

This experiment demonstrates the construction of an LL(1) parsing table from a context-free grammar using FIRST and FOLLOW sets. The LL(1) condition — that each (non-terminal, lookahead) pair maps to at most one production — is verified programmatically. The parsing table enables deterministic, predictive top-down parsing where the parser can decide which production to apply by examining a single lookahead token. Grammars that fail this condition require transformation (left recursion elimination, left factoring) or a more powerful parsing strategy.

---

### Questions of Curiosity

**1. What is a conflict in LL(1) parsing table?**
A conflict occurs when a single cell M[A, a] in the parsing table contains more than one production rule. This means the parser cannot deterministically decide which production to apply for non-terminal A with lookahead terminal a, making the grammar ambiguous for LL(1) parsing.

**2. What happens if a table entry has two productions?**
The parser becomes non-deterministic — it cannot decide which production to use for the given (non-terminal, terminal) pair. This means the grammar is not LL(1) and cannot be parsed by a predictive parser without backtracking or grammar transformation.

**3. How do you check whether a grammar is LL(1)?**
A grammar is LL(1) if and only if for every pair of productions A → α | β:
- FIRST(α) ∩ FIRST(β) = ∅
- If ε ∈ FIRST(α), then FIRST(β) ∩ FOLLOW(A) = ∅
- At most one of α or β can derive ε

Equivalently, the grammar is LL(1) if its parsing table has no multiply-defined entries.

---

### References
1. Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D., *Compilers: Principles, Techniques, and Tools*, 2nd Edition, Pearson Education.
2. Alfred V. Aho and Jeffrey D. Ullman, *Principles of Compiler Design*, Addison-Wesley.
