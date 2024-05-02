import sys

if len(sys.argv) < 2:
    print("Usage: python3 mycipher.py <shift>")
    sys.exit(1)

shift = int(sys.argv[1])

message = ""
for line in sys.stdin:
    message += line

message = ''.join(filter(str.isalpha, message)).upper()

cipher_message = ""
for char in message:
    cipher_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
    cipher_message += cipher_char

output = ""
for x in range(len(cipher_message)):
    if (x % 5) == 0 and x != 0:
        output += " "
    if (x % 50) == 0 and x != 0:
        print(output.strip())
        output = ""
    output += cipher_message[x]

if len(cipher_message) % 50 != 0:
    print(output.strip())
