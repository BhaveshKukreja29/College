def generate_tac(expr):
    # split assignment if present
    target = None
    if '=' in expr:
        parts = expr.split('=', 1)
        target = parts[0].strip()
        expr = parts[1].strip()

    tokens = tokenize(expr)
    result, tac, _ = parse_expression(tokens, 0)
    
    if target:
        tac.append(f"{target} = {result}")
    
    return tac


def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isspace():
            i += 1
            continue
        if expr[i] in '+-*/()':
            tokens.append(expr[i])
            i += 1
        else:
            word = ''
            while i < len(expr) and (expr[i].isalnum() or expr[i] == '_'):
                word += expr[i]
                i += 1
            tokens.append(word)
    return tokens


temp_count = 0

def new_temp():
    global temp_count
    temp_count += 1
    return f"t{temp_count}"


def parse_expression(tokens, pos):
    left, tac, pos = parse_term(tokens, pos)
    while pos < len(tokens) and tokens[pos] in ('+', '-'):
        op = tokens[pos]
        pos += 1
        right, tac2, pos = parse_term(tokens, pos)
        tac.extend(tac2)
        t = new_temp()
        tac.append(f"{t} = {left} {op} {right}")
        left = t
    return left, tac, pos


def parse_term(tokens, pos):
    left, tac, pos = parse_factor(tokens, pos)
    while pos < len(tokens) and tokens[pos] in ('*', '/'):
        op = tokens[pos]
        pos += 1
        right, tac2, pos = parse_factor(tokens, pos)
        tac.extend(tac2)
        t = new_temp()
        tac.append(f"{t} = {left} {op} {right}")
        left = t
    return left, tac, pos


def parse_factor(tokens, pos):
    if tokens[pos] == '(':
        pos += 1  # skip (
        result, tac, pos = parse_expression(tokens, pos)
        pos += 1  # skip )
        return result, tac, pos
    else:
        return tokens[pos], [], pos + 1


expr = input("Enter expression (e.g. a = b + c * d): ")
tac = generate_tac(expr)

print("\nThree Address Code:")
for line in tac:
    print(f"  {line}")
