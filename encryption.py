def encrypt_text(text, n, m):
    encrypted = []
    for char in text:
        if char.islower():
            original = ord(char)
            if 'a' <= char <= 'm':
                # Shift forward within a-m (13 letters)
                shift = (n * m) % 13  # Constrain shift to 0-12
                new_pos = ord('a') + (original - ord('a') + shift) % 13
            else:
                # Shift backward within n-z (13 letters)
                shift = (n + m) % 13
                new_pos = ord('n') + (original - ord('n') - shift) % 13
            encrypted.append(chr(new_pos))
        elif char.isupper():
            original = ord(char)
            if 'A' <= char <= 'M':
                # Shift backward within A-M (13 letters)
                shift = n % 13
                new_pos = ord('A') + (original - ord('A') - shift) % 13
            else:
                # Shift forward within N-Z (13 letters)
                shift = (m ** 2) % 13
                new_pos = ord('N') + (original - ord('N') + shift) % 13
            encrypted.append(chr(new_pos))
        else:
            encrypted.append(char)
    return ''.join(encrypted)

def decrypt_text(text, n, m):
    decrypted = []
    for char in text:
        if char.islower():
            encrypted_pos = ord(char)
            if 'a' <= char <= 'm':
                # Reverse forward shift (a-m)
                shift = (n * m) % 13
                new_pos = ord('a') + (encrypted_pos - ord('a') - shift) % 13
            else:
                # Reverse backward shift (n-z)
                shift = (n + m) % 13
                new_pos = ord('n') + (encrypted_pos - ord('n') + shift) % 13
            decrypted.append(chr(new_pos))
        elif char.isupper():
            encrypted_pos = ord(char)
            if 'A' <= char <= 'M':
                # Reverse backward shift (A-M)
                shift = n % 13
                new_pos = ord('A') + (encrypted_pos - ord('A') + shift) % 13
            else:
                # Reverse forward shift (N-Z)
                shift = (m ** 2) % 13
                new_pos = ord('N') + (encrypted_pos - ord('N') - shift) % 13
            decrypted.append(chr(new_pos))
        else:
            decrypted.append(char)
    return ''.join(decrypted)

def check_correctness(original, decrypted):
    return original == decrypted

def main():
    try:
        with open('raw_text.txt', 'r') as file:
            original_text = file.read()
    except FileNotFoundError:
        print("Error: raw_text.txt not found.")
        return

    try:
        n = int(input("Enter value for n (integer): "))
        m = int(input("Enter value for m (integer): "))
    except ValueError:
        print("Error: n and m must be integers.")
        return

    encrypted_text = encrypt_text(original_text, n, m)
    
    with open('encrypted_text.txt', 'w') as file:
        file.write(encrypted_text)
    
    decrypted_text = decrypt_text(encrypted_text, n, m)
    
    is_correct = check_correctness(original_text, decrypted_text)
    
    print("\nDecryption correct:", is_correct)

if __name__ == "__main__":
    main()