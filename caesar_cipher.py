def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    print("--- Caesar Cipher Tool ---")
    message = input("Enter your message: ")
    shift_val = int(input("Enter shift value (e.g., 3): "))

    encrypted = caesar_encrypt(message, shift_val)
    decrypted = caesar_decrypt(encrypted, shift_val)

    print(f"\nEncrypted Message: {encrypted}")
    print(f"Decrypted Message: {decrypted}")
