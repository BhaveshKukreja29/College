# Experiment 2: Hamming Code

def calculate_parity(arr, p_bit):
    """Calculates the parity for a given position."""
    count = 0
    for i in range(len(arr)):
        # Check if the bit position should be checked by this parity bit
        if (i + 1) & p_bit:
            if arr[i] == '1':
                count += 1
    return '1' if count % 2 != 0 else '0'

def hamming_encode(data):
    """Encodes data using Hamming Code."""
    n = len(data)
    r = 0
    # Calculate number of redundant bits
    while (2**r < n + r + 1):
        r += 1

    # Create array for codeword, leaving space for parity bits
    codeword = ['0'] * (n + r)
    j = 0
    for i in range(n + r):
        if (i + 1) & i != 0:  # Not a power of 2
            codeword[i] = data[j]
            j += 1

    # Calculate parity bits
    for i in range(r):
        p_pos = 2**i
        codeword[p_pos - 1] = calculate_parity(codeword, p_pos)

    return "".join(codeword)

def hamming_decode_correct(received_code):
    """Detects and corrects a single-bit error in a Hamming code."""
    r = 0
    l = len(received_code)
    while 2**r < l + 1:
        r += 1

    error_pos = 0
    for i in range(r):
        p_pos = 2**i
        parity_val = calculate_parity(list(received_code), p_pos)
        if parity_val == '1':
            error_pos += p_pos

    if error_pos == 0:
        print("No error detected.")
        return received_code
    else:
        print(f"Error detected at position: {error_pos}")
        # Correct the bit
        code_list = list(received_code)
        correct_bit = '0' if code_list[error_pos - 1] == '1' else '1'
        code_list[error_pos - 1] = correct_bit
        return "".join(code_list)

# --- Main Program ---
data_bits = "101"
print(f"Original Data: {data_bits}")

encoded_data = hamming_encode(data_bits)
print(f"Encoded Data (Hamming Code): {encoded_data}")

# Simulate an error at position 5
error_data = list(encoded_data)
error_data[4] = '0' if error_data[4] == '1' else '1'
error_data = "".join(error_data)
print(f"Received Data with error:    {error_data}")

corrected_data = hamming_decode_correct(error_data)
print(f"Corrected Data:              {corrected_data}")