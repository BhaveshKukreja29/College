"""
    Keywords – int, float, if, else, while
    Identifiers – variable names
    Operators – + - * / =
"""
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
for _ in range(len(nt_list)): # Iterate to stabilize
    for head, body in prods:
        for i, char in enumerate(body):
            if char.isupper():
                rest = body[i+1:]
                if not rest: follow[char] |= follow[head]
                else:
                    f_next = get_first(rest[0])
                    follow[char] |= (f_next - {'e'})
                    if 'e' in f_next: follow[char] |= follow[head]

# Build Table & Check LL(1)
table = {nt: {t: "" for t in t_list} for nt in nt_list}
is_ll1 = True
for head, body in prods:
    f_body = get_first(body[0]) if body != 'e' else {'e'}
    for s in f_body:
        if s != 'e':
            if table[head][s]: is_ll1 = False
            table[head][s] = f"{head}->{body}"
        else:
            for f_s in follow[head]:
                if table[head][f_s]: is_ll1 = False
                table[head][f_s] = f"{head}->{body}"

print("\nFIRST:", first, "\nFOLLOW:", follow)
print("\nTable (NT | Terminals):")
for nt in nt_list:
    print(f"{nt} | " + " | ".join([table[nt][t] or "-" for t in t_list]))

print("\nGrammar is LL(1):", is
_ll1)
