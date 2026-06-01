message = input("Enter a message to encrypt: ")
encrypted_message = ""

for char in message:
    if char.isalpha():
        shift_base = 65 if char.isupper() else 97
        encrypted_char = chr((ord(char) - shift_base + 3) % 26 + shift_base)
        encrypted_message += encrypted_char
    else:
        encrypted_message += char

print("Encrypted message:", encrypted_message)