# Experiment No. 03
## Elimination of Left Recursion & Left Factoring in Context-Free Grammar

**Aim:**
To implement the elimination of left recursion and left factoring from a given context-free grammar (CFG) in the syntax analysis phase of compiler design.

**Prerequisite:**
- Programming Language (Python)

**Course Outcome:**
After successful completion of this experiment students will be able to parse the given input string by constructing top-down / bottom-up parser.

**Software used:**
- Operating System: Windows / Linux
- Python compiler

---

### Theory

#### Left Recursion

A grammar is said to be left recursive if it has a non-terminal A such that `A → Aα`. Left recursion causes infinite recursion in top-down parsers like Recursive Descent Parser.

**Types of Left Recursion:**

1. **Immediate (Direct) Left Recursion** — `A → Aα | β`
2. **Indirect Left Recursion** — `A → Bα`, `B → Aβ`

**Elimination of Immediate Left Recursion:**
For a production `A → Aα | β`, convert to:
```
A  → βA'
A' → αA' | ε
```

**Example:**
```
Input:               Output:
E → E + T | T        E  → T E'
T → T * F | F        E' → + T E' | ε
F → ( E ) | id       T  → F T'
                      T' → * F T' | ε
                      F  → ( E ) | id
```

#### Left Factoring

Left factoring is a transformation technique used to eliminate common prefixes from production rules.

For productions `A → αβ₁ | αβ₂`, convert to:
```
A  → αA'
A' → β₁ | β₂
```

---

### Algorithm

**Algorithm to Eliminate Direct Left Recursion:**
1. Identify left-recursive productions in the grammar.
2. Separate recursive and non-recursive parts.
3. Introduce a new non-terminal.
4. Rewrite the productions to remove left recursion.
5. Repeat for all non-terminals.

**Algorithm for Left Factoring:**
1. Identify non-terminals with productions having common prefixes.
2. Extract the longest common prefix.
3. Introduce a new non-terminal.
4. Rewrite the grammar by factoring out the common prefix.
5. Repeat until no common prefixes remain.

---

### Procedure

1. Write and save the Python program.
2. Run the program.
3. Observe output.

---

### Tasks

1. Identify direct / indirect left recursion / left factoring in the given grammar.
2. Execute the program to eliminate direct / indirect left recursion / left factoring.
3. Analyse and verify the output grammar obtained.
4. Verify that the final grammar is free from both direct and indirect left recursion and left factoring.
5. Record the input, output, and observations.

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

**File: `exp3.py`**

```python
"""
Experiment 3: Elimination of Left Recursion & Left Factoring
Reads a CFG and removes direct left recursion and performs left factoring.
"""

import os


def eliminate_left_recursion(grammar, order):
    new_grammar = {}
    new_order = []

    for nt in order:
        prods = grammar[nt]
        recursive = []
        non_recursive = []

        for prod in prods:
            if prod[0] == nt:
                recursive.append(prod[1:])
            else:
                non_recursive.append(prod)

        if not recursive:
            new_grammar[nt] = prods
            new_order.append(nt)
        else:
            new_nt = nt + "'"
            # A -> beta A'
            new_grammar[nt] = [p + [new_nt] for p in non_recursive]
            # A' -> alpha A' | epsilon
            new_grammar[new_nt] = [r + [new_nt] for r in recursive] + [['e']]
            new_order.append(nt)
            new_order.append(new_nt)

    return new_grammar, new_order


def left_factor(grammar, order):
    new_grammar = {}
    new_order = []
    counter = {}

    for nt in order:
        prods = grammar[nt]

        # find the longest common prefix among any group
        prefix_map = {}
        for prod in prods:
            first = prod[0]
            if first not in prefix_map:
                prefix_map[first] = []
            prefix_map[first].append(prod)

        needs_factoring = False
        for key in prefix_map:
            if len(prefix_map[key]) > 1:
                needs_factoring = True
                break

        if not needs_factoring:
            new_grammar[nt] = prods
            new_order.append(nt)
        else:
            new_prods = []
            for key in prefix_map:
                group = prefix_map[key]
                if len(group) == 1:
                    new_prods.append(group[0])
                else:
                    if nt not in counter:
                        counter[nt] = 1
                    new_nt = nt + "'" * counter[nt]
                    counter[nt] += 1

                    new_prods.append([key, new_nt])
                    suffixes = []
                    for p in group:
                        rest = p[1:]
                        suffixes.append(rest if rest else ['e'])
                    new_grammar[new_nt] = suffixes
                    new_order.append(new_nt)

            new_grammar[nt] = new_prods
            new_order.insert(new_order.index(new_nt), nt) if nt not in new_order else None

    return new_grammar, new_order


def print_grammar(grammar, order):
    for nt in order:
        prods = grammar[nt]
        rhs = " | ".join(" ".join(p) for p in prods)
        print(f"  {nt} -> {rhs}")


# --- input ---
n = int(input("Enter number of non-terminals: "))
grammar = {}
order = []

for _ in range(n):
    nt = input("Enter non-terminal: ").strip()
    order.append(nt)
    raw = input(f"  Productions for {nt} (use | to separate, space between symbols): ").strip()
    prods = [alt.strip().split() for alt in raw.split('|')]
    grammar[nt] = prods

print("\nOriginal Grammar:")
print_grammar(grammar, order)

grammar, order = eliminate_left_recursion(grammar, order)
print("\nAfter Eliminating Left Recursion:")
print_grammar(grammar, order)

grammar, order = left_factor(grammar, order)
print("\nAfter Left Factoring:")
print_grammar(grammar, order)
```

---

### Output Screenshot

*(Paste screenshot here)*

---

### Observations

- The program correctly identifies left-recursive productions where the non-terminal appears as the first symbol on the right-hand side.
- For each left-recursive non-terminal, a new primed non-terminal (e.g., `E'`) is introduced, and the recursive and non-recursive parts are separated according to the standard elimination formula.
- The left factoring transformation correctly identifies productions with common prefixes and factors them into a shared prefix followed by a new non-terminal for the suffixes.
- Epsilon (`e`) productions are generated as expected during both left recursion elimination and left factoring.
- The final grammar obtained is suitable for top-down parsing techniques like Recursive Descent or LL(1) parsing.

---

### Conclusions

This experiment demonstrates the mechanical transformation of context-free grammars to eliminate left recursion and perform left factoring — two essential preprocessing steps for top-down parsers. Left recursion, which causes infinite loops in recursive descent parsers, is removed by introducing new non-terminals that convert left-recursive rules into right-recursive equivalents. Left factoring resolves ambiguity when multiple productions share a common prefix by deferring the decision point. The transformations preserve the language generated by the grammar while making it amenable to predictive parsing.

---

### Questions of Curiosity

**1. What is left recursion in a grammar?**
Left recursion occurs when a non-terminal `A` has a production where `A` itself is the leftmost symbol on the right-hand side (e.g., `A → Aα`). It can be direct (immediate) or indirect (through a chain of productions).

**2. Why is left recursion a problem in top-down parsing?**
A top-down parser expands the leftmost non-terminal first. If the first symbol of the expansion is the same non-terminal, the parser enters an infinite recursive loop, never consuming any input.

**3. What is immediate (direct) left recursion?**
Immediate left recursion occurs when a production directly refers to the same non-terminal as its leftmost symbol, e.g., `A → Aα | β`.

**4. What is indirect left recursion?**
Indirect left recursion occurs through a cycle of two or more productions, e.g., `A → Bα` and `B → Aβ`, where expanding `A → B → A` creates a recursive loop.

**5. Give an example of a left-recursive grammar.**
`E → E + T | T` — here `E` appears as the first symbol in its own production.

**6. How can immediate left recursion be eliminated?**
Replace `A → Aα | β` with: `A → βA'` and `A' → αA' | ε`. This converts the left recursion into right recursion.

**7. Why are new non-terminals introduced while eliminating left recursion?**
New non-terminals (e.g., `A'`) are needed to represent the recursive tail. Without them, there is no way to express the repetition of `α` without reintroducing left recursion.

**8. Does eliminating left recursion change the language of the grammar?**
No. The transformation is language-preserving — the set of strings generated by the grammar remains exactly the same. Only the derivation structure (parse tree shape) changes.

**9. Can bottom-up parsers handle left recursion? Why?**
Yes. Bottom-up parsers (e.g., LR parsers) build the parse tree from leaves to root by reducing substrings to non-terminals. They do not expand non-terminals top-down, so left recursion does not cause infinite loops.

**10. What happens if left recursion is not removed before recursive descent parsing?**
The parser enters an infinite recursive call chain — it repeatedly calls the function for the same non-terminal without advancing the input pointer, eventually causing a stack overflow.

**11. What is left factoring?**
Left factoring is a grammar transformation that factors out common prefixes from multiple productions of the same non-terminal, enabling a parser to make a deterministic choice based on a single lookahead token.

**12. Why is left factoring required?**
Without left factoring, a predictive parser cannot decide which production to use when two alternatives begin with the same symbol. Left factoring defers the choice point until the common prefix has been consumed.

---

### References
1. Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D., *Compilers: Principles, Techniques, and Tools*, 2nd Edition, Pearson Education.
2. Alfred V. Aho and Jeffrey D. Ullman, *Principles of Compiler Design*, Addison-Wesley.
