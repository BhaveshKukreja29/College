op1 = int(input('Enter operand 1: '))
op2 = int(input('Enter operand 2: '))
op = input('Enter the operation to perform(+,-,/,*): ')

if op == '+':
    print(op1 + op2)
elif op == '-':
    print(op1 - op2)
elif op == '/':
    if op2 == 0:
        print('Do not enter zero as divisor.')
    else:
        print(op1 / op2)
elif op == '*':
    print(op1 * op2)
else:
    print('Incorrect operand try again.')
