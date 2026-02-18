def calc_e(phi_n):
    import math

    i = 2
    while True:
        rem = math.gcd(i, phi_n)
        if rem == 1:
            break
        i += 1
    return i

# Select 2 prime numbers where they are not equal
p = 13
q = 11

n = p * q
print(n)

phi_n = (p - 1) * (q - 1)
print(phi_n)

e = calc_e(phi_n)
print(e)

d = pow(e, - 1, phi_n)

print(d)

public_key = [e, n]
private_key = [d, n]

M = int(input("Enter number: "))

C = pow(M, e, n)

print("Encrypted:", C)

A = pow(C, d, n)

print("Decrypted:", A)
