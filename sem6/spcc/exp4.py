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
    pass

grammar = {
    'S':[['A']],
    'A':[['B'], [None]],
    'B':[['b']]
}

first(grammar)
follow(grammar)
