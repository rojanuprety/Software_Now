# Function to encrypt the text
def encrypt_text(text, n, m):
    result = []  # List to hold the encrypted characters
    for char in text:  # Loop through each character in the input text
        if char.islower():  # Check if character is lowercase
            if 'a' <= char <= 'm':  # If in first half of alphabet
                # Shift forward by n * m and wrap around alphabet
                new_char = chr(((ord(char) - ord('a') + n * m) % 26) + ord('a'))
            else:  # If in second half of alphabet (n-z)
                # Shift backward by n + m and wrap around alphabet
                new_char = chr(((ord(char) - ord('a') - (n + m)) % 26) + ord('a'))
            result.append(new_char)  # Add encrypted character to result
        elif char.isupper():  # Check if character is uppercase
            if 'A' <= char <= 'M':  # If in first half of uppercase alphabet
                # Shift backward by n
                new_char = chr(((ord(char) - ord('A') - n) % 26) + ord('A'))
            else:  # If in second half of uppercase alphabet
                # Shift forward by m squared
                new_char = chr(((ord(char) - ord('A') + m**2) % 26) + ord('A'))
            result.append(new_char)  # Add encrypted character to result
        else:
            result.append(char)  # Leave numbers and special characters unchanged
    return ''.join(result)  # Return the encrypted string

# Function to decrypt the text
def decrypt_text(text, n, m):
    result = []  # List to hold the decrypted characters
    for char in text:  # Loop through each character in the input text
        if char.islower():  # Check if character is lowercase
            if 'a' <= char <= 'm':  # If originally in first half
                # Reverse the forward shift
                new_char = chr(((ord(char) - ord('a') - n * m) % 26) + ord('a'))
            else:  # If originally in second half
                # Reverse the backward shift
                new_char = chr(((ord(char) - ord('a') + (n + m)) % 26) + ord('a'))
            result.append(new_char)  # Add decrypted character to result
        elif char.isupper():  # Check if character is uppercase
            if 'A' <= char <= 'M':  # If originally in first half
                # Reverse the backward shift
                new_char = chr(((ord(char) - ord('A') + n) % 26) + ord('A'))
            else:  # If originally in second half
                # Reverse the forward shift
                new_char = chr(((ord(char) - ord('A') - m**2) % 26) + ord('A'))
            result.append(new_char)  # Add decrypted character to result
        else:
            result.append(char)  # Leave numbers and special characters unchanged
    return ''.join(result)  # Return the decrypted string

# Function to check if decryption is successful
def check_correctness(original_text, decrypted_text):
    return original_text == decrypted_text  # Compare both strings

# Main program execution
if __name__ == "__main__":
    # Get encryption inputs from user
    n = int(input("Enter value for n: "))
    m = int(input("Enter value for m: "))

    # Read original text from raw_text.txt
    with open("raw_text.txt", "r") as f:
        original_text = f.read()

    # Encrypt the text
    encrypted_text = encrypt_text(original_text, n, m)

    # Save encrypted text to file
    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted_text)

    # Decrypt the text
    decrypted_text = decrypt_text(encrypted_text, n, m)

    # Check if decryption is correct and display result
    if check_correctness(original_text, decrypted_text):
        print("Decryption is correct.")
    else:
        print("Decryption failed.")
