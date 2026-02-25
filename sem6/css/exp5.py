def get_primitive_root(p):
    # This finds the smallest primitive root for the prime p
    for g in range(2, p):
        is_root = True
        powers = set()
        for i in range(1, p):
            val = pow(g, i, p)
            if val in powers:
                is_root = False
                break
            powers.add(val)
        if is_root:
            return g
    return None

q = int(input("Enter a prime number (P): "))
a = get_primitive_root(q)

print(f"Using {a} as the primitive root (G) for {q}")

a_secret = int(input(f"Alice, enter a private key (less than {q}): "))
a_public_key = pow(a, a_secret, q)
print(f"Alice's Public Key (R1): {a_public_key}")

b_secret = int(input(f"Bob, enter a private key (less than {q}): "))
b_public_key = pow(a, b_secret, q)
print(f"Bob's Public Key (R2): {b_public_key}")

shared_key_a = pow(b_public_key, a_secret, q)

shared_key_b = pow(a_public_key, b_secret, q)

print()
print(f"Alice's calculated shared secret: {shared_key_a}")
print(f"Bob's calculated shared secret: {shared_key_b}")

if shared_key_a == shared_key_b:
    print("The shared secret keys match.")
else:
    print("The keys do not match.")
