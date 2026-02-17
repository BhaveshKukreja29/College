plaintext = input("Enter plain text: ")

cipher = ""

for i in plaintext:
    temp = ord(i)
    temp += 3
    cipher += chr(temp)

print("Ciphered text:", cipher)

decrypted = ""
for i in cipher:
    temp = ord(i)
    temp -= 3
    decrypted += chr(temp)

print("Decrypted using ciphered text:", decrypted)

