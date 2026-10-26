def eliminate_cse(code):
    lines = [line.strip() for line in code if line.strip()]
    expr_map = {}
    optimized = []

    for line in lines:
        parts = line.split('=', 1)
        lhs = parts[0].strip()
        rhs = parts[1].strip()

        if rhs in expr_map:
            optimized.append(f"{lhs} = {expr_map[rhs]}")
        else:
            expr_map[rhs] = lhs
            optimized.append(line)

    return optimized


n = int(input("Enter number of TAC lines: "))
code = []
for i in range(n):
    code.append(input(f"  Line {i + 1}: "))

print("\nOriginal Code:")
for line in code:
    print(f"  {line.strip()}")

result = eliminate_cse(code)

print("\nOptimized Code (after CSE):")
for line in result:
    print(f"  {line}")
