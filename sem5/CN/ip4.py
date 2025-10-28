if __name__ == "__main__":
    try:
        # --- USER INPUT ---
        ip_input = input("Enter the IP address (e.g., 150.100.10.5): ")
        num_subnets = int(input("Enter the number of subnets (must be a power of 2): "))

        ip_octets = [int(octet) for octet in ip_input.split('.')]

        # --- VALIDATION ---
        if not ((num_subnets > 0) and (num_subnets & (num_subnets - 1) == 0)):
            print("\nError: Number of subnets must be a power of 2 (e.g., 2, 4, 8).")
        elif len(ip_octets) != 4:
            raise ValueError("Invalid IP format.")
        else:
            print("\n--- IP Address Analysis ---")
            print(f"IP Address: {'.'.join(map(str, ip_octets))}")

            # --- DETERMINE IP CLASS ---
            first_octet = ip_octets[0]
            ip_class = ''
            if 1 <= first_octet <= 126:
                ip_class = 'A'
            elif 128 <= first_octet <= 191:
                ip_class = 'B'
            elif 192 <= first_octet <= 223:
                ip_class = 'C'
            else:
                print("IP Address is Class D or E. Cannot be subnetted with this tool.")
                exit()
            
            print(f"Class: {ip_class}")

            # --- CALCULATE SUBNET MASK AND BLOCK SIZE ---
            block_size = 256 // num_subnets
            custom_mask_octet = 256 - block_size

            mask = []
            if ip_class == 'A':
                mask = [255, custom_mask_octet, 0, 0]
            elif ip_class == 'B':
                mask = [255, 255, custom_mask_octet, 0]
            elif ip_class == 'C':
                mask = [255, 255, 255, custom_mask_octet]

            print(f"Custom Subnet Mask: {'.'.join(map(str, mask))}")

            # --- PRINT SUBNET DETAILS ---
            print("\n--- Subnet Details ---")
            for i in range(num_subnets):
                network_start = i * block_size
                print(f"\nSubnet #{i + 1}:")

                if ip_class == 'A':
                    print(f"  Network ID        : {ip_octets[0]}.{network_start}.0.0")
                    print(f"  First Host IP     : {ip_octets[0]}.{network_start}.0.1")
                    print(f"  Last Host IP      : {ip_octets[0]}.{network_start + block_size - 1}.255.254")
                    print(f"  Broadcast Address : {ip_octets[0]}.{network_start + block_size - 1}.255.255")
                
                elif ip_class == 'B':
                    print(f"  Network ID        : {ip_octets[0]}.{ip_octets[1]}.{network_start}.0")
                    print(f"  First Host IP     : {ip_octets[0]}.{ip_octets[1]}.{network_start}.1")
                    print(f"  Last Host IP      : {ip_octets[0]}.{ip_octets[1]}.{network_start + block_size - 1}.254")
                    print(f"  Broadcast Address : {ip_octets[0]}.{ip_octets[1]}.{network_start + block_size - 1}.255")
                
                elif ip_class == 'C':
                    print(f"  Network ID        : {ip_octets[0]}.{ip_octets[1]}.{ip_octets[2]}.{network_start}")
                    print(f"  First Host IP     : {ip_octets[0]}.{ip_octets[1]}.{ip_octets[2]}.{network_start + 1}")
                    print(f"  Last Host IP      : {ip_octets[0]}.{ip_octets[1]}.{ip_octets[2]}.{network_start + block_size - 2}")
                    print(f"  Broadcast Address : {ip_octets[0]}.{ip_octets[1]}.{ip_octets[2]}.{network_start + block_size - 1}")

    except ValueError:
        print("\nError: Invalid input. Please enter the IP address and subnet number correctly.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")