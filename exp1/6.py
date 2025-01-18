row = 5
alpha = 65

for i in range(5):
    for j in range(i + 1):
        ch = chr(alpha)
        print(ch, end='')
    print()
    alpha += 1
print()

for i in range(row,0,-1):
    print((row - i) * ' ' + i * '*')

print()

for i in range(row + 1):
    print((row - i) * ' ', end='')
    for j in range(1, i):
        print(j, end='')
    for j in range(i, 0, -1):
        print(j, end='')
    print()

print()

for i in range(row):
    print(" "*(row - i - 1), end="")
    for j in range(i + 1):
        print("* ", end="")
    print()
