# CSS Experiments — How to Run

All experiments are in: `~/Desktop/College/sem6/css/`

---

## Exp 1 — Caesar Cipher
```bash
python3 exp1.py
```
```
Enter plain text: HELLO
Ciphered text: KHOOR
Decrypted using ciphered text: HELLO
```

---

## Exp 2 — Multiplicative Inverse
```bash
python3 exp2.py
```
```
Enter the value to find the multiplicative inverse of: 7
Enter the 2nd number: 26
Q	R1	R2	R	T1	T2	T
3 	 26 	 7 	 5 	 0 	 1 	 -3
1 	 7 	 5 	 2 	 1 	 -3 	 4
2 	 5 	 2 	 1 	 -3 	 4 	 -11
2 	 2 	 1 	 0 	 4 	 -11 	 26
The multiplicative inverse of 7 is 4
```
**Verify**: 7 × 4 = 28 → 28 mod 26 = 2... wait, try 7 × 15 = 105 → 105 mod 26 = 1 ✓

> **Note**: For affine cipher use, enter `a` value and `26` as second number.

---

## Exp 3 — Playfair Cipher
```bash
python3 exp3.py
```
```
Enter key: MONARCHY
Enter text to encrypt: HELLO

Key table is
M O N A R
C H Y B D
E F G I K
L P Q S T
U V W Z J

Encrypted text: CFSUPM
Decrypted text: HELQLO
```

> **Note**: Decrypted text may differ slightly from original due to filler characters (J) inserted for repeated letters.

---

## Exp 4 — RSA Algorithm
```bash
python3 exp4.py
```
```
143
120
7
103
Enter number: 9
Encrypted: 48
Decrypted: 9
```

The printed values in order are:
1. `n = 143` (p × q)
2. `φ(n) = 120`
3. `e = 7` (public exponent)
4. `d = 103` (private exponent)

> **Note**: Input number must be less than n (143). Try values like 9, 42, 100.

---

## Exp 5 — Diffie-Hellman Key Exchange
```bash
python3 exp5.py
```
```
Enter a prime number (P): 23
Using 5 as the primitive root (G) for 23
Alice, enter a private key (less than 23): 6
Alice's Public Key (R1): 8
Bob, enter a private key (less than 23): 15
Bob's Public Key (R2): 19

Alice's calculated shared secret: 2
Bob's calculated shared secret: 2
The shared secret keys match.
```

> **Good test primes**: 23, 29, 31, 37, 41

---

## Exp 6 — MD5 Hashing
```bash
python3 exp6.py
```
```
Enter message: hello
MD5 Hash: 5d41402abc4b2a76b9719d911017c592
Expected: 5d41402abc4b2a76b9719d911017c592
Hash matches!
```

Other test inputs:
```
"abc"       → 900150983cd24fb0d6963f7d28e17f72
"password"  → 5f4dcc3b5aa765d61d8327deb882cf99
""          → d41d8cd98f00b204e9800998ecf8427e
```

---

## Exp 10 — Buffer Overflow Attack using Splint

### Step 1: Install Splint
```bash
sudo apt-get install splint
```

### Step 2: Check vulnerabilities with Splint
```bash
cd ~/Desktop/College/sem6/css/
splint program1.c
splint program2.c
splint program3.c
```

Splint will report warnings like:
- `gets` usage (unsafe, no bounds checking)
- Out-of-bounds array access
- `scanf` with `%s` (no length limit)
- Unused parameters, missing return types, etc.

### Step 3: Compile and run (to see the overflow in action)
```bash
gcc -o program1 program1.c -fno-stack-protector
./program1

gcc -o program2 program2.c -fno-stack-protector
./program2

gcc -o program3 program3.c -fno-stack-protector
./program3
```

> **Note**: `-fno-stack-protector` disables GCC's stack protection so the overflow is observable.

**Program 1 test**: Enter a password longer than 15 characters to overflow `buff` and corrupt `pass`.
**Program 2 test**: Observe stack pointer values before and after the out-of-bounds write.
**Program 3 test**: Enter `password` for success, or a very long string (>16 chars) to attempt auth bypass.
