import string

def teaser_cipher():
    # Read text from a file named 'plaintext'
    with open('plaintext', 'r') as file:
        text = file.read().lower()

    shift = int(input("Enter the shift value: "))

    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet, shifted_alphabet)

    encrypted_text = text.translate(translation_table)
    encrypted_text = encrypted_text.replace(" ", "")
    encrypted_text = encrypted_text.upper()

    formatted_text = ' '.join(encrypted_text[i:i+5] for i in range(0, len(encrypted_text), 5))
    print(formatted_text)

teaser_cipher()
