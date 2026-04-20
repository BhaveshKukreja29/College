# --- Left Recursion Elimination ---
# A -> Aα | β  becomes  A -> βA', A' -> αA' | ε

def eliminate_left_recursion(grammar, order):
    new_grammar = {}
    new_order = []

    for nt in order:
        recursive = []
        non_recursive = []

        for prod in grammar[nt]:
            if prod[0] == nt:
                recursive.append(prod[1:])   # save α (drop the leading A)
            else:
                non_recursive.append(prod)   # save β

        if not recursive:
            new_grammar[nt] = grammar[nt]
            new_order.append(nt)
        else:
            new_nt = nt + "'"
            # A -> β A'
            new_grammar[nt] = []
            for p in non_recursive:
                new_grammar[nt].append(p + [new_nt])
            # A' -> α A' | ε
            new_grammar[new_nt] = []
            for r in recursive:
                new_grammar[new_nt].append(r + [new_nt])
            new_grammar[new_nt].append(['e'])

            new_order.append(nt)
            new_order.append(new_nt)

    return new_grammar, new_order


# --- Left Factoring ---
# A -> αβ1 | αβ2  becomes  A -> αA', A' -> β1 | β2

def left_factor(grammar, order):
    new_grammar = {}
    new_order = []

    for nt in order:
        # group productions by their first symbol
        groups = {}
        for prod in grammar[nt]:
            first = prod[0]
            if first not in groups:
                groups[first] = []
            groups[first].append(prod)

        # check if any group has more than 1 production (= common prefix)
        has_common_prefix = False
        for key in groups:
            if len(groups[key]) > 1:
                has_common_prefix = True

        if not has_common_prefix:
            new_grammar[nt] = grammar[nt]
            new_order.append(nt)
        else:
            new_prods = []
            for key in groups:
                if len(groups[key]) == 1:
                    new_prods.append(groups[key][0])
                else:
                    new_nt = nt + "'"
                    new_prods.append([key, new_nt])   # A -> prefix A'
                    # A' -> suffix1 | suffix2 | ...
                    new_grammar[new_nt] = []
                    for p in groups[key]:
                        rest = p[1:]
                        if rest:
                            new_grammar[new_nt].append(rest)
                        else:
                            new_grammar[new_nt].append(['e'])
                    new_order.append(new_nt)

            new_grammar[nt] = new_prods
            new_order.insert(0, nt)

    return new_grammar, new_order


# --- Print ---

def print_grammar(grammar, order):
    for nt in order:
        parts = []
        for p in grammar[nt]:
            parts.append(" ".join(p))
        print(f"  {nt} -> {' | '.join(parts)}")


# --- Main ---

n = int(input("Enter number of non-terminals: "))
grammar = {}
order = []

for _ in range(n):
    nt = input("Enter non-terminal: ").strip()
    order.append(nt)
    raw = input(f"  Productions for {nt} (| separated, space between symbols): ")
    prods = []
    for alt in raw.split('|'):
        print(alt)
        prods.append(alt.strip().split())
    grammar[nt] = prods

print("\nOriginal Grammar:")
print(grammar)
print_grammar(grammar, order)

grammar, order = eliminate_left_recursion(grammar, order)
print("\nAfter Left Recursion Elimination:")
print_grammar(grammar, order)

grammar, order = left_factor(grammar, order)
print("\nAfter Left Factoring:")
print_grammar(grammar, order)

