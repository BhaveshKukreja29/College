OP_MAP = {
    '+': 'ADD',
    '-': 'SUB',
    '*': 'MUL',
    '/': 'DIV',
}

reg_count = 0

def getreg():
    global reg_count
    reg_count += 1
    return f"R{reg_count}"


def generate(tac_lines):
    code = []

    for line in tac_lines:
        parts = line.split('=', 1)
        lhs = parts[0].strip()
        rhs = parts[1].strip().split()

        if len(rhs) == 1:
            # simple assignment: x = y
            r = getreg()
            code.append(f"MOV {r}, {rhs[0]}")
            code.append(f"MOV {lhs}, {r}")

        elif len(rhs) == 3:
            # x = y op z
            y, op, z = rhs
            r = getreg()
            code.append(f"MOV {r}, {y}")
            code.append(f"{OP_MAP[op]} {r}, {z}")
            code.append(f"MOV {lhs}, {r}")

    return code


n = int(input("Enter number of TAC lines: "))
tac = []
for i in range(n):
    tac.append(input(f"  Line {i + 1}: "))

print("\nInput TAC:")
for line in tac:
    print(f"  {line}")

result = generate(tac)

print("\nGenerated Target Code:")
for line in result:
    print(f"  {line}")
