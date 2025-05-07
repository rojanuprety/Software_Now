def encrypt_text(text, n, m):
    encrypted = []  # List to collect encrypted characters
    for char in text:
        if char.islower():

            # Handle lowercase letters
            original = ord(char)
            if 'a' <= char <= 'm':

                # Shift forward within a-m
                shift = (n * m) % 13  # Modulo to stay within range
                new_pos = ord('a') + (original - ord('a') + shift) % 13
            else:

                # Shift backward within n-z
                shift = (n + m) % 13
                new_pos = ord('n') + (original - ord('n') - shift) % 13
            encrypted.append(chr(new_pos))

        elif char.isupper():

            # Handle uppercase letters
            original = ord(char)
            if 'A' <= char <= 'M':

                # Shift backward within A-M
                shift = n % 13
                new_pos = ord('A') + (original - ord('A') - shift) % 13
            else:

                # Shift forward within N-Z
                shift = (m ** 2) % 13
                new_pos = ord('N') + (original - ord('N') + shift) % 13
            encrypted.append(chr(new_pos))
        else:

            # Leave non-alphabet characters unchanged
            encrypted.append(char)
    return ''.join(encrypted)  # Combine characters into a single string

def decrypt_text(text, n, m):
    decrypted = []  # List to collect decrypted characters
    for char in text:
        if char.islower():

            # Handle lowercase letters
            encrypted_pos = ord(char)
            if 'a' <= char <= 'm':

                # Reverse forward shift for a-m
                shift = (n * m) % 13
                new_pos = ord('a') + (encrypted_pos - ord('a') - shift) % 13
            else:

                # Reverse backward shift for n-z
                shift = (n + m) % 13
                new_pos = ord('n') + (encrypted_pos - ord('n') + shift) % 13
            decrypted.append(chr(new_pos))

        elif char.isupper():

            # Handle uppercase letters
            encrypted_pos = ord(char)
            if 'A' <= char <= 'M':

                # Reverse backward shift for A-M
                shift = n % 13
                new_pos = ord('A') + (encrypted_pos - ord('A') + shift) % 13
            else:

                # Reverse forward shift for N-Z
                shift = (m ** 2) % 13
                new_pos = ord('N') + (encrypted_pos - ord('N') - shift) % 13
            decrypted.append(chr(new_pos))
        else:

            # Leave non-alphabet characters unchanged
            decrypted.append(char)
    return ''.join(decrypted)  # Combine characters into a single string

def check_correctness(original, decrypted):
    return original == decrypted  # Returns True if decryption matches original

def main():
    try:
        with open('raw_text.txt', 'r') as file:
            original_text = file.read()  # Read input text from file
    except FileNotFoundError:
        print("Error: raw_text.txt not found.")  # Handle missing file
        return

    try:
        n = int(input("Enter value for n (integer): "))  # Get integer input n
        m = int(input("Enter value for m (integer): "))  # Get integer input m
    except ValueError:
        print("Error: n and m must be integers.")  # Handle non-integer input
        return

    encrypted_text = encrypt_text(original_text, n, m)  # Encrypt text using provided keys

    with open('encrypted_text.txt', 'w') as file:
        file.write(encrypted_text)  # Write encrypted text to file

    decrypted_text = decrypt_text(encrypted_text, n, m)  # Decrypt the encrypted text

    is_correct = check_correctness(original_text, decrypted_text)  # Check correctness of decryption

    print("\nDecryption correct:", is_correct)  # Output the result

if __name__ == "__main__":
    main()  # Run the main function
