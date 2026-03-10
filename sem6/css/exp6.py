import struct
import math


def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF


def md5(message):
    # Per-round shift amounts
    s = [
        7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
        5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
        4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
        6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21,
    ]

    # Precomputed constants from sine function
    K = [int(abs(math.sin(i + 1)) * (2 ** 32)) & 0xFFFFFFFF for i in range(64)]

    # Initial hash values
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    # Pre-processing: adding padding bits
    msg = bytearray(message, "utf-8")
    orig_len_bits = (8 * len(msg)) & 0xFFFFFFFFFFFFFFFF
    msg.append(0x80)

    while len(msg) % 64 != 56:
        msg.append(0)

    # Append original length in bits as 64-bit little-endian
    msg += struct.pack("<Q", orig_len_bits)

    # Process each 512-bit (64-byte) block
    for offset in range(0, len(msg), 64):
        block = msg[offset : offset + 64]
        M = struct.unpack("<16I", block)

        A, B, C, D = a0, b0, c0, d0

        for i in range(64):
            if i < 16:
                F = (B & C) | (~B & D)
                g = i
            elif i < 32:
                F = (D & B) | (~D & C)
                g = (5 * i + 1) % 16
            elif i < 48:
                F = B ^ C ^ D
                g = (3 * i + 5) % 16
            else:
                F = C ^ (B | ~D)
                g = (7 * i) % 16

            F = (F + A + K[i] + M[g]) & 0xFFFFFFFF
            A = D
            D = C
            C = B
            B = (B + left_rotate(F, s[i])) & 0xFFFFFFFF

        a0 = (a0 + A) & 0xFFFFFFFF
        b0 = (b0 + B) & 0xFFFFFFFF
        c0 = (c0 + C) & 0xFFFFFFFF
        d0 = (d0 + D) & 0xFFFFFFFF

    digest = struct.pack("<4I", a0, b0, c0, d0)
    return digest.hex()


message = input("Enter message: ")
hash_value = md5(message)
print("MD5 Hash:", hash_value)

# Verify with hashlib
import hashlib

expected = hashlib.md5(message.encode()).hexdigest()
print("Expected:", expected)

if hash_value == expected:
    print("Hash matches!")
else:
    print("Hash does not match.")
