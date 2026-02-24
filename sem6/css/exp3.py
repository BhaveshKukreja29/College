def generate_key_table(key):
    key = key.upper().replace("X", "I")
    key = "".join(c for c in key if c.isalpha())

    seen = []
    for c in key:
        if c not in seen:
            seen.append(c)

    for c in "ABCDEFGHIJKLMNOPQRSTUVWYZ":
        if c not in seen:
            seen.append(c)

    table = []
    for i in range(5):
        table.append(seen[i * 5 : i * 5 + 5])
    return table


def format_input(text):
    text = text.upper().replace("X", "I")
    text = "".join(c for c in text if c.isalpha())

    result = list(text)
    i = 0
    while i < len(result) - 1:
        if result[i] == result[i + 1]:
            result.insert(i + 1, "J")
        i += 2

    if len(result) % 2 != 0:
        result.append("J")

    return "".join(result)


def find_position(table, ch):
    for i in range(5):
        for j in range(5):
            if table[i][j] == ch:
                return i, j
    return None


def encrypt(table, plaintext):
    plaintext = format_input(plaintext)
    cipher = ""

    for i in range(0, len(plaintext), 2):
        r1, c1 = find_position(table, plaintext[i])
        r2, c2 = find_position(table, plaintext[i + 1])

        if r1 == r2:
            cipher += table[r1][(c1 + 1) % 5]
            cipher += table[r2][(c2 + 1) % 5]
        elif c1 == c2:
            cipher += table[(r1 + 1) % 5][c1]
            cipher += table[(r2 + 1) % 5][c2]
        else:
            cipher += table[r1][c2]
            cipher += table[r2][c1]

    return cipher


def decrypt(table, ciphertext):
    plain = ""

    for i in range(0, len(ciphertext), 2):
        r1, c1 = find_position(table, ciphertext[i])
        r2, c2 = find_position(table, ciphertext[i + 1])

        if r1 == r2:
            plain += table[r1][(c1 + 4) % 5]
            plain += table[r2][(c2 + 4) % 5]
        elif c1 == c2:
            plain += table[(r1 + 4) % 5][c1]
            plain += table[(r2 + 4) % 5][c2]
        else:
            plain += table[r1][c2]
            plain += table[r2][c1]

    return plain


key = input("Enter key: ")
table = generate_key_table(key)

print("Key table is")
for row in table:
    print(" ".join(row))

text = input("Enter text to encrypt: ")

encrypted = encrypt(table, text)
print("Encrypted text:", encrypted)

decrypted = decrypt(table, encrypted)
print("Decrypted text:", decrypted)
