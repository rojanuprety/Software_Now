def encrypt_char(c, n, m):
    if c.islower():
        shift = n * m if 'a' <= c <= 'm' else -(n + m)
        new_char = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        return new_char
    elif c.isupper():
        shift = -n if 'A' <= c <= 'M' else m * m
        new_char = chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        return new_char
    else:
        return c  # leave digits, symbols, and whitespace unchanged

def decrypt_char(c, n, m):
    if c.islower():
        shift = n * m if 'a' <= c <= 'm' else -(n + m)
        new_char = chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
        return new_char
    elif c.isupper():
        shift = -n if 'A' <= c <= 'M' else m * m
        new_char = chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
        return new_char
    else:
        return c

def encrypt_text(text, n, m):
    return ''.join([encrypt_char(c, n, m) for c in text])

def decrypt_text(text, n, m):
    return ''.join([decrypt_char(c, n, m) for c in text])

def check_decryption(original, decrypted):
    return original == decrypted

def main():
    n = int(input("Enter value for n: "))
    m = int(input("Enter value for m: "))

    with open("raw_text.txt", "r", encoding="utf-8") as f:
        original_text = f.read()

    encrypted_text = encrypt_text(original_text, n, m)

    with open("encrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(encrypted_text)

    decrypted_text = decrypt_text(encrypted_text, n, m)

    if check_decryption(original_text, decrypted_text):
        print("✅ Decryption successful. Text matches original.")
    else:
        print("❌ Decryption failed. Text does not match original.")
        # Optional: Show where it mismatches
        for i in range(len(original_text)):
            if i >= len(decrypted_text) or original_text[i] != decrypted_text[i]:
                print(f"Mismatch at pos {i}: '{original_text[i]}' != '{decrypted_text[i]}'")
                break

if __name__ == "__main__":
    main()
