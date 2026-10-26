# FIRST: what terminals can a symbol start with?
# FOLLOW: what terminals can appear after a non-terminal?

grammar = {}

def get_first(sym):
    if sym == 'e':
        return {'e'}
    if sym not in grammar:       # terminal
        return {sym}
    result = set()
    for prod in grammar[sym]:
        for s in prod:
            f = get_first(s)
            result |= f - {'e'}
            if 'e' not in f:
                break
        else:
            result.add('e')      # all symbols nullable
    return result


def get_follow():
    follow = {nt: set() for nt in grammar}
    start = list(grammar.keys())[0]
    follow[start].add('$')

    for _ in range(len(grammar)):          # repeat to propagate
        for nt in grammar:
            for prod in grammar[nt]:
                for i, sym in enumerate(prod):
                    if sym not in grammar:
                        continue
                    beta = prod[i+1:]
                    # FIRST of everything after sym
                    first_beta = set()
                    nullable = True
                    for b in beta:
                        fb = get_first(b)
                        first_beta |= fb - {'e'}
                        if 'e' not in fb:
                            nullable = False
                            break
                    follow[sym] |= first_beta
                    if nullable:
                        follow[sym] |= follow[nt]
    return follow


# --- input ---
n = int(input("Enter number of non-terminals: "))
for _ in range(n):
    nt = input("Non-terminal: ").strip()
    raw = input(f"  Productions for {nt} (| separated, 'e'=epsilon): ")
    grammar[nt] = [alt.strip().split() for alt in raw.split('|')]

# --- output ---
print("\nFIRST:")
for nt in grammar:
    print(f"  FIRST({nt}) = {{ {', '.join(sorted(get_first(nt)))} }}")

follow = get_follow()
print("\nFOLLOW:")
for nt in grammar:
    print(f"  FOLLOW({nt}) = {{ {', '.join(sorted(follow[nt]))} }}")

