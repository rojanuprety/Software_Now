import string

def encrypt_char(char, n, m):
    if char in string.ascii_lowercase:
        if char <= 'm':
            shift = n * m
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            shift = n + m
            return chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
    elif char in string.ascii_uppercase:
        if char <= 'M':
            shift = n
            return chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            shift = m ** 2
            return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    return char

def decrypt_char(char, n, m):
    if char in string.ascii_lowercase:
        if char <= 'm':
            shift = n * m
            return chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            shift = n + m
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    elif char in string.ascii_uppercase:
        if char <= 'M':
            shift = n
            return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            shift = m ** 2
            return chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
    return char

def encrypt_text(input_file, output_file, n, m):
    try:
        with open(input_file, 'r') as f:
            text = f.read()
        
        encrypted_text = ''.join(encrypt_char(char, n, m) for char in text)
        
        with open(output_file, 'w') as f:
            f.write(encrypted_text)
        
        return encrypted_text
    except FileNotFoundError:
        return "Error: Input file not found."
    except Exception as e:
        return f"Error: {str(e)}"

def decrypt_text(input_file, n, m):
    try:
        with open(input_file, 'r') as f:
            text = f.read()
        
        decrypted_text = ''.join(decrypt_char(char, n, m) for char in text)
        return decrypted_text
    except FileNotFoundError:
        return "Error: Input file not found."
    except Exception as e:
        return f"Error: {str(e)}"

def check_decryption(original_file, decrypted_text):
    try:
        with open(original_file, 'r') as f:
            original_text = f.read()
        
        return original_text == decrypted_text
    except FileNotFoundError:
        return False

def main():
    try:
        n = int(input("Enter n: "))
        m = int(input("Enter m: "))
        
        encrypted = encrypt_text("raw_text.txt", "encrypted_text.txt", n, m)
        if "Error" in encrypted:
            print(encrypted)
            return
            
        decrypted = decrypt_text("encrypted_text.txt", n, m)
        if "Error" in decrypted:
            print(decrypted)
            return
            
        is_correct = check_decryption("raw_text.txt", decrypted)
        print(f"Encryption successful. Output written to encrypted_text.txt")
        print(f"Decryption {'successful' if is_correct else 'failed'}.")
        
    except ValueError:
        print("Error: Please enter valid integers for n and m.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()