# CSS Experiments — Explain + Viva Q&A

---

## Experiment 1 — Caesar Cipher

### What It Is
A **substitution cipher** where each letter in the plaintext is shifted by a fixed number (key). Here key = 3.

### How It Works
- **Encrypt**: Shift each character's ASCII value forward by 3 → `ord(char) + 3`
- **Decrypt**: Shift back by 3 → `ord(char) - 3`

### Example
```
Input:  HELLO
Cipher: KHOOR    (H→K, E→H, L→O, L→O, O→R)
```

### Code Walkthrough
```python
for i in plaintext:
    temp = ord(i)    # Get ASCII value of the character
    temp += 3        # Shift by 3
    cipher += chr(temp)  # Convert back to character
```
That's it. Decryption is the exact reverse with `-3`.

### Viva Questions

**Q1: What is the Caesar Cipher?**
A substitution cipher that shifts each letter by a fixed number of positions in the alphabet. Named after Julius Caesar who used a shift of 3.

**Q2: What is the key in this implementation?**
The key is 3 (hardcoded). Every character is shifted by 3 positions.

**Q3: What's the difference between Caesar Cipher and ROT13?**
ROT13 is a special case of Caesar Cipher with key = 13. Since 13 is half of 26, applying ROT13 twice gives you the original text.

**Q4: Is Caesar Cipher secure?**
No. It has only 25 possible keys (for English), so it can be broken by brute force in seconds. It's also vulnerable to **frequency analysis**.

**Q5: What is frequency analysis?**
A technique where you count how often each character appears in the ciphertext. Since letter frequencies in a language are known (e.g., 'E' is most common in English), you can deduce the shift.

**Q6: What happens if you shift beyond 'Z'?**
In this code, it uses raw ASCII, so it may produce non-alphabetic characters. A proper implementation would use `(char - 'A' + key) % 26 + 'A'` to wrap around.

**Q7: What type of cipher is Caesar — symmetric or asymmetric?**
Symmetric — the same key is used for both encryption and decryption.

**Q8: What is the mathematical formula for Caesar Cipher?**
- Encrypt: `C = (P + K) mod 26`
- Decrypt: `P = (C - K) mod 26`
Where P = plaintext letter position, C = cipher letter position, K = key.

---

## Experiment 2 — Multiplicative Inverse (Extended Euclidean Algorithm)

### What It Is
Finds the **multiplicative inverse** of a number `a` modulo `b`. That means finding `x` such that `(a × x) mod b = 1`. This is needed in RSA and other ciphers.

### How It Works (Extended Euclidean Algorithm)
Repeatedly divide and track quotients/remainders until remainder = 0:
```
Q = R1 // R2
R = R1 - Q × R2
T = T1 - Q × T2
```
Then shift: `R1 ← R2, R2 ← R, T1 ← T2, T2 ← T`

When done, if `R1 = 1`, then `T1` is the inverse. If `T1 < 0`, add 26.

### Example
Find inverse of 7 mod 26:
```
Q   R1   R2   R   T1   T2   T
3   26    7   5    0    1   -3
1    7    5   2    1   -3    4
2    5    2   1   -3    4  -11
2    2    1   0    4  -11   26
```
Answer: `T1 = 4` → because `7 × 4 = 28 = 1 mod 26` ✓

### Code Walkthrough
```python
while r2 > 0:
    q = r1 // r2          # Quotient
    r = r1 - q * r2       # New remainder
    t = t1 - q * t2       # New T coefficient
    # Shift values for next iteration
```
When the loop ends, `t1` holds the inverse (if `r1 == 1`).

### Viva Questions

**Q1: What is a multiplicative inverse?**
For number `a` mod `m`, the inverse `x` is a number such that `(a × x) mod m = 1`. Example: inverse of 7 mod 26 is 4 because 7×4 = 28 ≡ 1 (mod 26).

**Q2: When does a multiplicative inverse NOT exist?**
When `gcd(a, m) ≠ 1`. The inverse exists only if `a` and `m` are **coprime** (their GCD is 1).

**Q3: Why is this important in cryptography?**
RSA decryption requires finding `d` such that `e × d ≡ 1 (mod φ(n))`. This is a multiplicative inverse computation.

**Q4: What is the Extended Euclidean Algorithm?**
An extension of the Euclidean algorithm (GCD) that also finds coefficients `x, y` such that `ax + by = gcd(a, b)`. When `gcd = 1`, `x` is the modular inverse.

**Q5: Why do we add 26 if T1 is negative?**
Because we want a positive result in the range `[0, 25]`. Adding the modulus doesn't change the mathematical result: `-3 mod 26 = 23`.

**Q6: What is the time complexity?**
O(log(min(a, b))) — logarithmic, very efficient.

**Q7: Why is the modulus hardcoded to 26 in the negative check?**
It's specific to alphabetic ciphers (26 letters). For general use, you'd add `b` instead of 26.

---

## Experiment 3 — Playfair Cipher

### What It Is
A **digraph substitution cipher** — encrypts **two letters at a time** using a 5×5 key matrix.

### How It Works

**1. Generate Key Table (5×5)**
- Write the key letters first (no duplicates), then fill remaining with unused alphabet letters.
- Combine I and X (both map to I). Only 25 letters fit in 5×5.

**2. Format the Plaintext**
- Split into pairs of two letters.
- If both letters in a pair are same, insert a filler ('J') between them.
- If odd length, append 'J' at the end.

**3. Encrypt Each Pair**
| Condition | Rule |
|-----------|------|
| Same row | Shift each letter **right** by 1 (wrap around) |
| Same column | Shift each letter **down** by 1 (wrap around) |
| Rectangle | Swap columns (keep same row) |

**4. Decrypt**: Reverse the rules (left instead of right, up instead of down, same swap for rectangle).

### Example
Key: `MONARCHY`, Plaintext: `HELLO`
```
Key Table:
M O N A R
C H Y B D
E F G I K
L P Q S T
U V W Z J

Pairs: HE LL O → HE LJ LO  (insert J between LL, pad)
HE → same column? No. Same row? No. Rectangle → CF
```

### Code Walkthrough
```python
# Key table generation — deduplicate key, fill remaining alphabet
seen = []
for c in key:
    if c not in seen: seen.append(c)
for c in "ABCDEFGHIJKLMNOPQRSTUVWYZ":   # no X (mapped to I)
    if c not in seen: seen.append(c)

# Rectangle rule
cipher += table[r1][c2]   # first char keeps its row, takes second's column
cipher += table[r2][c1]   # second char keeps its row, takes first's column
```

### Viva Questions

**Q1: Why is the matrix 5×5 and not 26 cells?**
English has 26 letters but the matrix can only hold 25. So two letters are merged — here I and X are treated as the same letter.

**Q2: What are the three rules for encryption?**
1. **Same row**: shift right by 1
2. **Same column**: shift down by 1
3. **Rectangle**: swap columns

**Q3: Why is Playfair better than Caesar?**
It encrypts **pairs** of letters, not individual ones, making frequency analysis much harder. There are 600+ possible digraphs vs. 26 single letters.

**Q4: What happens with repeated letters like 'LL'?**
A filler character (here 'J') is inserted between them: `LL → LJ L`.

**Q5: How does decryption differ from encryption?**
Same row → shift **left** by 1 (use `(col + 4) % 5` instead of `(col + 1) % 5`).
Same column → shift **up** by 1. Rectangle rule stays the same.

**Q6: Is Playfair symmetric or asymmetric?**
Symmetric — same key is used for encryption and decryption.

**Q7: Can Playfair be broken?**
Yes. With enough ciphertext, digraph frequency analysis can break it. It was used in WWI/WWII but is not secure by modern standards.

**Q8: Why replace X with I and not J with I (like traditional Playfair)?**
This is an implementation choice. Traditional Playfair merges I/J. This code merges I/X instead. Both are valid approaches.

**Q9: What's the time complexity of Playfair encryption?**
O(n) where n is the length of plaintext — each pair is encrypted in O(1) using the table lookup.

---

## Experiment 4 — RSA Algorithm

### What It Is
An **asymmetric encryption** algorithm. Uses a **public key** to encrypt and a **private key** to decrypt. Security relies on the difficulty of factoring large numbers.

### How It Works

| Step | Formula | In Code |
|------|---------|---------|
| 1. Pick two primes | p = 13, q = 11 | Hardcoded |
| 2. Compute n | n = p × q = 143 | `n = p * q` |
| 3. Compute φ(n) | φ(n) = (p−1)(q−1) = 120 | `phi_n = (p-1)*(q-1)` |
| 4. Find e | smallest e where gcd(e, φ(n)) = 1 | `calc_e(phi_n)` → e = 7 |
| 5. Find d | d = e⁻¹ mod φ(n) | `pow(e, -1, phi_n)` → d = 103 |
| 6. Public key | (e, n) = (7, 143) | |
| 7. Private key | (d, n) = (103, 143) | |
| 8. Encrypt | C = M^e mod n | `pow(M, e, n)` |
| 9. Decrypt | M = C^d mod n | `pow(C, d, n)` |

### Example
```
M = 9
C = 9^7 mod 143 = 48   (encrypted)
M = 48^103 mod 143 = 9  (decrypted back)
```

### Code Walkthrough
```python
e = calc_e(phi_n)       # Find smallest e coprime with φ(n)
d = pow(e, -1, phi_n)   # Modular inverse of e — this IS the private key exponent
C = pow(M, e, n)        # Encrypt: M^e mod n
A = pow(C, d, n)        # Decrypt: C^d mod n
```

### Viva Questions

**Q1: What makes RSA asymmetric?**
It uses **two different keys**: public key (e, n) for encryption, private key (d, n) for decryption. Anyone can encrypt, only the private key holder can decrypt.

**Q2: What is φ(n) (Euler's Totient)?**
The count of numbers from 1 to n that are coprime with n. For n = p×q, φ(n) = (p−1)(q−1).

**Q3: Why must gcd(e, φ(n)) = 1?**
So that `e` has a modular inverse `d`. If they share a factor, the inverse doesn't exist and decryption won't work.

**Q4: What is the relationship between e and d?**
`e × d ≡ 1 (mod φ(n))`. They are modular inverses of each other.

**Q5: Why is RSA secure?**
Because to find `d`, you need `φ(n)`, which requires factoring `n` into `p` and `q`. For very large n (2048+ bits), factoring is computationally infeasible.

**Q6: Can RSA encrypt messages larger than n?**
No. The message M must satisfy `0 ≤ M < n`. For larger messages, you'd break them into blocks or use RSA to encrypt a symmetric key (hybrid encryption).

**Q7: What is `pow(e, -1, phi_n)` doing?**
Python 3.8+ built-in for modular inverse. It computes `d` such that `e * d mod phi_n = 1`. Internally uses the Extended Euclidean Algorithm.

**Q8: What happens if p and q are not prime?**
The algorithm breaks. φ(n) = (p−1)(q−1) is only valid when p and q are prime. Decryption would produce incorrect results.

**Q9: What's the difference between RSA and Diffie-Hellman?**
RSA is for **encryption/decryption** and **digital signatures**. Diffie-Hellman is only for **key exchange** — it lets two parties agree on a shared secret but can't encrypt messages directly.

---

## Experiment 5 — Diffie-Hellman Key Exchange

### What It Is
A **key exchange protocol** that allows two parties (Alice and Bob) to generate a **shared secret** over an insecure channel, without ever transmitting the secret itself.

### How It Works

| Step | Who | Formula | Purpose |
|------|-----|---------|---------|
| 1 | Public | Choose prime P and primitive root G | Public parameters |
| 2 | Alice | Pick private key `a`, compute R1 = G^a mod P | Alice's public key |
| 3 | Bob | Pick private key `b`, compute R2 = G^b mod P | Bob's public key |
| 4 | Alice | Shared = R2^a mod P = G^(b×a) mod P | Alice computes secret |
| 5 | Bob | Shared = R1^b mod P = G^(a×b) mod P | Bob computes secret |

Both get the same result because `G^(ab) mod P = G^(ba) mod P`.

### Example
```
P = 23, G = 5
Alice: a = 6 → R1 = 5^6 mod 23 = 8
Bob:   b = 15 → R2 = 5^15 mod 23 = 19

Alice's secret: 19^6 mod 23 = 2
Bob's secret:   8^15 mod 23 = 2   ← Same! ✓
```

### Code Walkthrough
```python
# Primitive root: a number G where G^1, G^2, ..., G^(P-1) mod P
# produces all values from 1 to P-1 (no repeats)
def get_primitive_root(p):
    for g in range(2, p):
        powers = set()
        for i in range(1, p):
            val = pow(g, i, p)
            if val in powers: break  # Repeated → not a primitive root
            powers.add(val)
        if is_root: return g

# Key exchange
a_public_key = pow(a, a_secret, q)     # R1 = G^a mod P
shared_key_a = pow(b_public_key, a_secret, q)  # R2^a mod P
```

### Viva Questions

**Q1: What is Diffie-Hellman used for?**
Secure key exchange over an insecure channel. It doesn't encrypt data itself — it creates a shared secret that both parties can then use as a key for symmetric encryption.

**Q2: What is a primitive root?**
A number G is a primitive root of prime P if the set {G^1 mod P, G^2 mod P, ..., G^(P-1) mod P} contains all integers from 1 to P-1.

**Q3: Why does the shared secret match?**
Alice computes `(G^b)^a mod P = G^(ba) mod P`.
Bob computes `(G^a)^b mod P = G^(ab) mod P`.
Since ab = ba, both results are identical.

**Q4: What is the Discrete Logarithm Problem?**
Given G, P, and R = G^a mod P, finding `a` is computationally hard for large P. This is what makes Diffie-Hellman secure.

**Q5: Is Diffie-Hellman vulnerable to any attack?**
Yes — **Man-in-the-Middle (MITM)**. An attacker can intercept and replace public keys. Solution: authenticate the exchange using digital signatures or certificates.

**Q6: Is Diffie-Hellman symmetric or asymmetric?**
It's neither — it's a **key agreement protocol**. But the shared secret it produces is typically used for **symmetric** encryption.

**Q7: What happens if P is not prime?**
Primitive roots may not exist, and the security of the discrete log problem weakens significantly. P must be a large prime.

**Q8: What's the difference between Diffie-Hellman and RSA?**
DH = key exchange only. RSA = encryption + digital signatures. DH produces a shared symmetric key; RSA uses asymmetric key pairs.

**Q9: What is the time complexity?**
Modular exponentiation is O(log n) multiplications using fast exponentiation. Primitive root finding is O(P × P) in this brute-force implementation.

---

## Experiment 6 — MD5 Hashing Algorithm

### What It Is
**MD5** (Message Digest 5) produces a **128-bit (32 hex character) hash** from any input. It's a **one-way function** — you can't reverse it. Used for checksums and integrity verification.

### How It Works

**Step 1: Pad the Message**
- Append `0x80` (a 1-bit), then zeros until length ≡ 56 mod 64.
- Append the original message length (in bits) as 8 bytes.
- Now message is a multiple of 64 bytes (512 bits).

**Step 2: Initialize 4 Buffers**
```
A = 0x67452301
B = 0xEFCDAB89
C = 0x98BADCFE
D = 0x10325476
```

**Step 3: Process Each 512-bit Block (64 rounds)**

| Rounds | Function | Word Index |
|--------|----------|------------|
| 0–15   | F = (B & C) \| (~B & D) | g = i |
| 16–31  | G = (D & B) \| (~D & C) | g = (5i+1) % 16 |
| 32–47  | H = B ⊕ C ⊕ D | g = (3i+5) % 16 |
| 48–63  | I = C ⊕ (B \| ~D) | g = (7i) % 16 |

Each round:
```
F = F + A + K[i] + M[g]     ← mix function result + buffer + constant + message word
Rotate buffers: A←D, D←C, C←B, B←B+left_rotate(F, s[i])
```

**Step 4: Concatenate A, B, C, D → 128-bit hash**

### Constants
- `K[i]` = `floor(2^32 × |sin(i+1)|)` — 64 fixed constants derived from sine.
- `s[i]` = predefined per-round shift amounts (7,12,17,22 for rounds 0-15, etc.)

### Code Walkthrough
```python
# Padding
msg.append(0x80)               # Add 1-bit
while len(msg) % 64 != 56:     # Pad with zeros
    msg.append(0)
msg += pack("<Q", orig_len)    # Append 64-bit length

# Per block: 64 rounds of mixing
for i in range(64):
    F = ...  # One of 4 functions based on round
    g = ...  # Index into message words
    F = (F + A + K[i] + M[g]) & 0xFFFFFFFF
    # Shift buffers
    B = B + left_rotate(F, s[i])
```

### Viva Questions

**Q1: What is hashing?**
A one-way function that converts any input into a fixed-size output (digest). It's deterministic (same input → same output), but you can't recover the input from the hash.

**Q2: What is the output size of MD5?**
128 bits = 16 bytes = 32 hexadecimal characters.

**Q3: What are the properties of a good hash function?**
1. **Deterministic**: Same input → same hash
2. **Fast to compute**
3. **Pre-image resistant**: Can't find input from hash
4. **Collision resistant**: Hard to find two inputs with same hash
5. **Avalanche effect**: Small input change → completely different hash

**Q4: Is MD5 secure?**
**No.** Collisions have been found (two different inputs producing the same hash). It's broken for security purposes. Use SHA-256 instead.

**Q5: What is a collision?**
When two different inputs produce the same hash output. For MD5, deliberate collisions can be computed in seconds.

**Q6: Why is padding needed?**
MD5 processes data in 512-bit blocks. Padding ensures the message is a multiple of 512 bits. The length is appended to prevent length extension attacks.

**Q7: What is the difference between hashing and encryption?**
Hashing is **one-way** (can't get original back). Encryption is **two-way** (can decrypt with key). Hashing produces fixed-size output; encryption output size depends on input.

**Q8: Where is MD5 still used?**
File integrity checks (checksums), non-security purposes like cache keys. **Never** for passwords or digital signatures.

**Q9: What is `left_rotate`?**
A circular left shift: bits shifted out from the left re-enter from the right. `left_rotate(x, 5)` moves the top 5 bits to the bottom. This provides diffusion in the hash.

**Q10: What are the 4 rounds in MD5?**
Each uses a different boolean function (F, G, H, I) and a different formula for selecting which message word to use. This ensures all parts of the message influence the final hash.

**Q11: What's the difference between MD5 and SHA-256?**
| Feature | MD5 | SHA-256 |
|---------|-----|---------|
| Output size | 128 bits | 256 bits |
| Rounds | 64 | 64 |
| Security | Broken | Secure |
| Speed | Faster | Slightly slower |

**Q12: What is the avalanche effect? Give an example.**
A 1-bit change in input produces a completely different hash:
- MD5("hello") = `5d41402abc4b2a76b9719d911017c592`
- MD5("hellp") = `10f481e681b0afc2caa6459d8e97ade0`
Completely different despite 1 letter change.
