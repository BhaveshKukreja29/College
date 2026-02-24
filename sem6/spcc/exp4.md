# Experiment No. 04
## FIRST and FOLLOW of a Given Grammar

**Aim:**
To implement the algorithm for FIRST and FOLLOW sets for a given context-free grammar (CFG) and understand their role in syntax analysis.

**Prerequisite:**
- Programming Language (Python)

**Course Outcome:**
After successful completion of this experiment students will be able to parse the given input string by constructing top-down / bottom-up parser.

**Software used:**
- Operating System: Windows / Linux
- Python compiler

---

### Theory

#### Context-Free Grammar (CFG)

A grammar G = (V, T, P, S) where:
- **V** = Set of non-terminals
- **T** = Set of terminals
- **P** = Set of production rules
- **S** = Start symbol

#### FIRST Set

FIRST(X) is the set of terminals that appear as the first symbol in strings derived from X.

**Rules to compute FIRST:**
1. If X is a terminal, FIRST(X) = {X}
2. If X → ε, add ε to FIRST(X)
3. If X → Y₁Y₂…Yₙ, add FIRST(Y₁) to FIRST(X)
4. If FIRST(Y₁) contains ε, consider FIRST(Y₂), and so on

#### FOLLOW Set

FOLLOW(X) is the set of terminals that can appear immediately to the right of X in some sentential form.

**Rules to compute FOLLOW:**
1. Add `$` to FOLLOW(S), where S is the start symbol
2. For `A → αBβ`, add FIRST(β) − {ε} to FOLLOW(B)
3. If β → ε or β is empty, add FOLLOW(A) to FOLLOW(B)

#### Example

| Non-Terminal | FIRST       | FOLLOW |
|-------------|-------------|--------|
| S           | { a, b }    | { $ }  |
| A           | { a, ε }    | { b }  |
| B           | { b }       | { $ }  |

---

### Algorithm

**Algorithm for FIRST:**
1. Initialise FIRST(X) = ∅ for all symbols X
2. Repeat until no changes occur:
   - For each production X → Y₁Y₂…Yₖ:
     - Add FIRST(Y₁) − {ε} to FIRST(X)
     - For i = 2 to k: if ε ∈ FIRST(Yᵢ₋₁), add FIRST(Yᵢ) − {ε} to FIRST(X)
     - If ε ∈ FIRST(Yᵢ) for all i = 1 to k, add ε to FIRST(X)
3. Stop when FIRST sets no longer change.

**Algorithm for FOLLOW:**
1. Initialise FOLLOW(A) = ∅ for all non-terminals A
2. Add `$` to FOLLOW(S)
3. Repeat until no changes occur:
   - For each production A → αBβ:
     - Add FIRST(β) − {ε} to FOLLOW(B)
     - If β is empty or ε ∈ FIRST(β), add FOLLOW(A) to FOLLOW(B)
4. Stop when FOLLOW sets no longer change.

---

### Procedure

1. Write and save the Python program.
2. Run the program.
3. Observe output.

---

### Tasks

Given a context-free grammar, write and execute an algorithm to compute the FIRST and FOLLOW sets for all non-terminals in the grammar.

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

**File: `exp4.py`**

```python
"""
Experiment 4: FIRST and FOLLOW sets

Grammar format:
  - dict of non-terminal -> list of productions
  - each production is a list of symbols
  - lowercase / special chars = terminals, uppercase = non-terminals
  - 'e' stands for epsilon

Example:
  E  -> T E'
  E' -> + T E' | e
  T  -> F T'
  T' -> * F T' | e
  F  -> ( E ) | id
"""

def first(grammar):
    ans = {nt: set() for nt in grammar}

    changed = True
    while changed:
        changed = False
        for nt in grammar:
            for prod in grammar[nt]:
                # walk through each symbol in the production
                all_nullable = True
                for sym in prod:
                    if sym == 'e':
                        # epsilon production
                        if 'e' not in ans[nt]:
                            ans[nt].add('e')
                            changed = True
                        all_nullable = True
                        break

                    if sym not in grammar:
                        # terminal
                        if sym not in ans[nt]:
                            ans[nt].add(sym)
                            changed = True
                        all_nullable = False
                        break
                    else:
                        # non-terminal: add its FIRST minus epsilon
                        before = len(ans[nt])
                        ans[nt] |= ans[sym] - {'e'}
                        if len(ans[nt]) > before:
                            changed = True

                        if 'e' not in ans[sym]:
                            all_nullable = False
                            break

                if all_nullable and 'e' not in ans[nt]:
                    ans[nt].add('e')
                    changed = True

    return ans


def follow(grammar, first_sets):
    ans = {nt: set() for nt in grammar}

    start = list(grammar.keys())[0]
    ans[start].add('$')

    changed = True
    while changed:
        changed = False
        for nt in grammar:
            for prod in grammar[nt]:
                for i, sym in enumerate(prod):
                    if sym not in grammar:
                        continue

                    # look at everything after sym (the beta part)
                    beta = prod[i + 1:]

                    # add FIRST(beta) - {e} to FOLLOW(sym)
                    first_beta = set()
                    all_nullable = True
                    for b in beta:
                        if b not in grammar:
                            first_beta.add(b)
                            all_nullable = False
                            break
                        else:
                            first_beta |= first_sets[b] - {'e'}
                            if 'e' not in first_sets[b]:
                                all_nullable = False
                                break

                    before = len(ans[sym])
                    ans[sym] |= first_beta

                    # if beta is empty or nullable, add FOLLOW(nt) to FOLLOW(sym)
                    if all_nullable:
                        ans[sym] |= ans[nt]

                    if len(ans[sym]) > before:
                        changed = True

    return ans


# --- take input ---
n = int(input("Enter number of non-terminals: "))
grammar = {}

for _ in range(n):
    nt = input("Enter non-terminal: ").strip()
    m = int(input(f"Enter number of productions for {nt}: "))
    prods = []
    for j in range(m):
        raw = input(f"  Production {j + 1} (space-separated, use 'e' for epsilon): ").strip()
        prods.append(raw.split())
    grammar[nt] = prods

print()

f = first(grammar)
print("FIRST sets:")
for nt in grammar:
    print(f"  FIRST({nt}) = {{ {', '.join(sorted(f[nt]))} }}")

fl = follow(grammar, f)
print("\nFOLLOW sets:")
for nt in grammar:
    print(f"  FOLLOW({nt}) = {{ {', '.join(sorted(fl[nt]))} }}")
```

---

### Output Screenshot

*(Paste screenshot here)*

---

### Observations

- The FIRST set computation correctly identifies terminal symbols that can begin a derivation from each non-terminal, including epsilon for nullable productions.
- The fixed-point iteration terminates once no new terminals are added to any FIRST set, confirming convergence.
- The FOLLOW set for the start symbol always includes `$` (end-of-input marker) as initialised by the algorithm.
- For productions of the form `A → αBβ`, the FIRST of β (excluding ε) is correctly added to FOLLOW(B). When β is nullable or empty, FOLLOW(A) propagates to FOLLOW(B).
- The computed FIRST and FOLLOW sets for the given grammar satisfy all the standard rules of compiler design.

---

### Conclusions

This experiment demonstrates the computation of FIRST and FOLLOW sets — two fundamental constructs required for building LL(1) parse tables. The FIRST set determines which terminal can start a derivation from a non-terminal, while the FOLLOW set determines which terminals can appear after a non-terminal in any sentential form. Both computations use a fixed-point iterative approach that terminates when no further changes occur. The resulting sets enable the construction of a predictive parsing table by resolving which production to apply for a given (non-terminal, lookahead) pair.

---

### Questions of Curiosity

**1. What is context-free grammar?**
A context-free grammar (CFG) is a formal grammar where every production rule has a single non-terminal on the left-hand side. It is defined as G = (V, T, P, S), where V is the set of non-terminals, T is the set of terminals, P is the set of production rules, and S is the start symbol. CFGs are powerful enough to describe the syntax of most programming languages.

**2. What is the FIRST set?**
FIRST(X) is the set of terminal symbols that can appear as the first symbol of any string derivable from X. If X can derive ε (the empty string), then ε is also included in FIRST(X).

**3. What is the FOLLOW set?**
FOLLOW(A) is the set of terminal symbols that can appear immediately to the right of non-terminal A in any sentential form derived from the start symbol. The end-of-input marker `$` is always included in FOLLOW of the start symbol.

**4. Why are FIRST sets required in compiler design?**
FIRST sets are used by predictive parsers (LL(1)) to decide which production to apply. Given a non-terminal and a lookahead token, the parser checks which production's FIRST set contains that token. Without FIRST sets, the parser cannot make a deterministic choice.

**5. Why are FOLLOW sets required?**
FOLLOW sets are needed to handle epsilon productions. When a non-terminal can derive ε, the parser must check whether the lookahead token belongs to the non-terminal's FOLLOW set to decide whether to apply the epsilon production.

---

### References
1. Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D., *Compilers: Principles, Techniques, and Tools*, 2nd Edition, Pearson Education.
2. Alfred V. Aho and Jeffrey D. Ullman, *Principles of Compiler Design*, Addison-Wesley.
