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

# 1. Setup - Get the prime number from user
q = int(input("Enter a prime number (P): "))
a = get_primitive_root(q)

print(f"Using {a} as the primitive root (G) for {q}")

# 2. Alice's Part
a_secret = int(input(f"Alice, enter a private key (less than {q}): "))
a_public_key = pow(a, a_secret, q)
print(f"Alice's Public Key (R1): {a_public_key}")

# 3. Bob's Part
b_secret = int(input(f"Bob, enter a private key (less than {q}): "))
b_public_key = pow(a, b_secret, q)
print(f"Bob's Public Key (R2): {b_public_key}")

# 4. Shared Key Calculation
# Alice uses Bob's public key and her private key
shared_key_a = pow(b_public_key, a_secret, q)

# Bob uses Alice's public key and his private key
shared_key_b = pow(a_public_key, b_secret, q)

# 5. Verification
print("-" * 20)
print(f"Alice's calculated shared secret: {shared_key_a}")
print(f"Bob's calculated shared secret: {shared_key_b}")

if shared_key_a == shared_key_b:
    print("Success! The shared secret keys match.")
else:
    print("Error: The keys do not 
    match.")
