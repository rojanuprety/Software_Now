def read_file(filename):
    """Reads content from a file"""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

def write_file(filename, content):
    """Writes content to a file"""
    with open(filename, 'w') as file:
        file.write(content)

def encrypt_char(ch, n, m):
    """Encrypts a single character using the given rules"""
    if 'a' <= ch <= 'z':  # Lowercase letters
        if ch <= 'm':  # First half (a-m)
            shift = n * m
            new_pos = (ord(ch) - ord('a') + shift) % 26 + ord('a')
        else:  # Second half (n-z)
            shift = n + m
            new_pos = (ord(ch) - ord('a') - shift) % 26 + ord('a')
        return chr(new_pos)
    
    elif 'A' <= ch <= 'Z':  # Uppercase letters
        if ch <= 'M':  # First half (A-M)
            shift = n
            new_pos = (ord(ch) - ord('A') - shift) % 26 + ord('A')
        else:  # Second half (N-Z)
            shift = m ** 2
            new_pos = (ord(ch) - ord('A') + shift) % 26 + ord('A')
        return chr(new_pos)
    
    else:  # Numbers and special characters
        return ch

def decrypt_char(ch, n, m):
    """Decrypts a single character"""
    if 'a' <= ch <= 'z':  # Lowercase letters
        # First try decrypting as if it was first half (a-m)
        decrypted_first_half = chr((ord(ch) - (n * m) - ord('a')) % 26 + ord('a'))
        if decrypted_first_half <= 'm':
            return decrypted_first_half
        # Otherwise decrypt as second half (n-z)
        return chr((ord(ch) + (n + m) - ord('a')) % 26 + ord('a'))
    
    elif 'A' <= ch <= 'Z':  # Uppercase letters
        # First try decrypting as if it was first half (A-M)
        decrypted_first_half = chr((ord(ch) + n - ord('A')) % 26 + ord('A'))
        if decrypted_first_half <= 'M':
            return decrypted_first_half
        # Otherwise decrypt as second half (N-Z)
        return chr((ord(ch) - (m ** 2) - ord('A')) % 26 + ord('A'))
    
    else:  # Numbers and special characters
        return ch

def encrypt_text(text, n, m):
    """Encrypts entire text"""
    return ''.join([encrypt_char(ch, n, m) for ch in text])

def decrypt_text(text, n, m):
    """Decrypts entire text"""
    return ''.join([decrypt_char(ch, n, m) for ch in text])

def main():
    # Read original text
    original = read_file("raw_text.txt")
    if original is None:
        return
    
    # Get encryption keys
    try:
        n = int(input("Enter integer value for n: "))
        m = int(input("Enter integer value for m: "))
    except ValueError:
        print("Please enter valid integers for n and m")
        return
    
    # Encrypt and save
    encrypted = encrypt_text(original, n, m)
    write_file("encrypted_text.txt", encrypted)
    print("\nEncrypted text saved to 'encrypted_text.txt'")
    
    # Decrypt to verify
    decrypted = decrypt_text(encrypted, n, m)
    
    # Check if decryption matches original
    if decrypted == original:
        print("✓ Decryption successful - matches original")
    else:
        print("✗ Decryption failed - doesn't match original")
    
    # Show samples
    print("\nOriginal start:", original[:50])
    print("Encrypted start:", encrypted[:50])
    print("Decrypted start:", decrypted[:50])

if __name__ == "__main__":
    main()