def caesar_cipher(text, shift, mode):
    result = ""

    if mode.lower() == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char

    return result

message = input("Enter your message: ")
shift_value = int(input("Enter shift value: "))
mode = input("Do you want to Encrypt or Decrypt? ").strip().lower()

output = caesar_cipher(message, shift_value, mode)
print(f"Output: {output}")
