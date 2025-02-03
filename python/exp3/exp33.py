from sys import exit

def calculator(opr, *args):
        map = {'+', '-', '*', '/'}
        if opr not in map:
                exit("Enter a valid operand")

        if len(args) < 2:
                exit("Enter minimum 2 operands")
        sum = args[0]
        if opr == '+':
                for i in args[1:]:
                        sum += i

        elif opr == '-':
                for i in args[1:]:
                        sum -= i
        elif opr == '*':
                for i in args[1:]:
                        sum *= i
        else:
                for i in args[1:]:
                        if args[i] == 0:
                                exit("Cannot have 0 as divisor")
                        sum /= i

        print(sum)

size = int(input("How many operands do you want to operate on? "))
oprs = []
for i in range(size):
        oprs.append(int(input(f"Enter number {i + 1}: ")))
opr = input("Enter an operand: ")
calculator(opr, *oprs)
