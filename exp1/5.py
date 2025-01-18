n = int(input('Enter n: '))

a = 0
b = 1
c = 0
while True:
    c = a + b
    a = b
    b = c
    if c < n:
        print(c)
    else:
        break
