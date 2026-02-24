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
            new_grammar[nt] = [p + [new_nt] for p in non_recursive]
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
            if nt not in new_order:
                new_order.insert(new_order.index(new_nt), nt)

    return new_grammar, new_order


def print_grammar(grammar, order):
    for nt in order:
        prods = grammar[nt]
        rhs = " | ".join(" ".join(p) for p in prods)
        print(f"  {nt} -> {rhs}")


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
