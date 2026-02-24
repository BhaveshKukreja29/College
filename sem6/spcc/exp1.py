"""
    • Keywords – int, float, if, else, while

    • Identifiers – variable names

    • Operators – + - * / =

    • Relational Operators – < > <= >= == !=

    • Constants – numbers

    • Special Symbols – ; , ( ) { }

"""


num_lines = int(input("Enter number of lines: "))
lines = list()
for _ in range(num_lines):
    lines.append(input())

# lex
keywords = ['int', 'float', 'double', 'if', 'else', 'while', 'for', 'return', 'void', 'char']
operators = ['+', '-', '*', '/', '=', '<', '>', '!', '%']
separators = [';', ',', '(', ')', '{', '}', '[', ']']

ans = []

# processing
for line in lines:
    i = 0
    while i < len(line):
        ch = line[i]

        # skip whitespace
        if ch.isspace():
            i += 1
            continue

        # multi-char operators like ==, <=, >=, !=
        if ch in operators and i + 1 < len(line) and line[i + 1] == '=':
            ans.append(('Operator', ch + '='))
            i += 2
            continue

        if ch in operators:
            ans.append(('Operator', ch))
            i += 1
            continue

        if ch in separators:
            ans.append(('Separator', ch))
            i += 1
            continue

        # numbers (int or float)
        if ch.isdigit():
            num = ''
            while i < len(line) and (line[i].isdigit() or line[i] == '.'):
                num += line[i]
                i += 1
            ans.append(('Number', num))
            continue

        # keywords or identifiers
        if ch.isalpha() or ch == '_':
            word = ''
            while i < len(line) and (line[i].isalnum() or line[i] == '_'):
                word += line[i]
                i += 1
            if word in keywords:
                ans.append(('Keyword', word))
            else:
                ans.append(('Identifier', word))
            continue

        i += 1
    


# output
for i in ans:
    print(f"{i[0]}: {i[1]}")

