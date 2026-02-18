"""
S -> AB
A -> a | epsilon
B -> b

"""
def first(grammar):
    ans = {}
    for i in grammar:
        # we use this to iterate over each key in the grammar dictionary
        ans[i] = grammar[i][0][0]

    # Resolve the non-terminal ones
    while not all(ans[i].islower() for i in ans):
        for i in grammar:
            if ans[i].isupper():
                ans[i] = ans[ans[i]]

    print(ans)

def follow(grammar):
    ans = {}
    for i in grammar:
        ans[i] = None

    start = list(grammar.keys())[0]
    ans[start] = '$'

    while not all(ans[i] is not None for i in ans):
        for i in grammar:
            for j in grammar[i]:
                for k in j:
                    if k is None:
                        continue
                    if k.isupper() and ans[k] is None:
                        ans[k] = ans[i]

    print(ans)

grammar = {
    'S': [['a'], ['b'], ['a', 'S', 'A'], ['b', 'S', 'b']],
    'A': [['a', 'B']],
    'B': [['b']]
}

first(grammar)
follow(grammar)
