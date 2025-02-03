def add4(func):
        def wrap(n):
                res = func(n)
                return res + 4
        return wrap

def mulby2(func):
        def wrap(n):
                res = func(n)
                return res * 2
        return wrap


@add4
def calSquare(n):
        return n*n


@mulby2
def calCube(n):
        return n*n*n

num = int(input("Enter a number: "))
print(f"Square normal: {num*num}")
print(f"Square decorated: {calSquare(num)}")
print()
print(f"Cube normal: {num*num*num}")
print(f"Cube decorated: {calCube(num)}")
