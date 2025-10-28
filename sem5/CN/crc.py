def crc_division(dividend, divisor):
    div_len = len(divisor)
    dividend_list = list(dividend) # Work with a mutable list

    # Loop through the dividend
    for i in range(len(dividend_list) - div_len + 1):
        # If the leading bit of the current window is 1, perform XOR
        if dividend_list[i] == '1':
            for j in range(div_len):
                # XOR operation: '1' if different, '0' if same
                dividend_list[i + j] = '0' if dividend_list[i + j] == divisor[j] else '1'
    
    # The remainder is the last (div_len - 1) bits
    remainder = "".join(dividend_list[-(div_len - 1):])
    return remainder

# --- Hardcoded Values ---
data = "10011101"
generator = "1011"
gen_len = len(generator)

print("--- SENDER ---")
print(f"Data: {data}")
print(f"Generator: {generator}")

# 1. Append (gen_len - 1) zeros to the data
appended_data = data + '0' * (gen_len - 1)
print(f"Appended Data: {appended_data}")

# 2. Calculate the CRC remainder
crc_remainder = crc_division(appended_data, generator)
print(f"Calculated CRC (Remainder): {crc_remainder}")

# 3. Create the final codeword to be sent
codeword = data + crc_remainder
print(f"Codeword to be sent: {codeword}")

# --- RECEIVER SIDE ---
print("\n--- RECEIVER ---")
print(f"Received Codeword: {codeword}")
print(f"Generator: {generator}")

# 1. Verify the received codeword by getting its remainder
remainder_at_receiver = crc_division(codeword, generator)
print(f"Remainder at receiver: {remainder_at_receiver}")

# 2. Check if the remainder is all zeros
if int(remainder_at_receiver) == 0:
    print("Result: No error detected. The data is correct.")
else:
    print("Result: Error detected! The data is corrupted.")