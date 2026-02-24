def first(grammar):
    ans = {nt: set() for nt in grammar}

    changed = True
    while changed:
        changed = False
        for nt in grammar:
            for prod in grammar[nt]:
                all_nullable = True
                for sym in prod:
                    if sym == 'e':
                        if 'e' not in ans[nt]:
                            ans[nt].add('e')
                            changed = True
                        all_nullable = True
                        break

                    if sym not in grammar:
                        if sym not in ans[nt]:
                            ans[nt].add(sym)
                            changed = True
                        all_nullable = False
                        break
                    else:
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

                    beta = prod[i + 1:]

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

                    if all_nullable:
                        ans[sym] |= ans[nt]

                    if len(ans[sym]) > before:
                        changed = True
    return ans


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
