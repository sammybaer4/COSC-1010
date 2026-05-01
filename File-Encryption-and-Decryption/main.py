#
# sam
# 4/30/26
# File Encryption and Decryption Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# Encryption Program

# Create dictionary (A–Z and a–z)
codes = {
'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '!', 'c': '1',
'D': '^', 'd': '2', 'E': '&', 'e': '3', 'F': '*', 'f': '4',
'G': '(', 'g': '5', 'H': ')', 'h': '6', 'I': '-', 'i': '7',
'J': '+', 'j': '8', 'K': '=', 'k': '0', 'L': '{', 'l': '}',
'M': '[', 'm': ']', 'N': ':', 'n': ';', 'O': '"', 'o': "'",
'P': '<', 'p': '>', 'Q': '/', 'q': '?', 'R': '~', 'r': '`',
'S': '|', 's': '\\', 'T': '€', 't': '£', 'U': '¥', 'u': '¢',
'V': '§', 'v': '©', 'W': '®', 'w': '™', 'X': '∆', 'x': 'π',
'Y': '✓', 'y': '✔', 'Z': '◊', 'z': '•',
'.': '○', ',': '●'
}

# Open original file
infile = open("text.txt", "r")

# Open encrypted file
outfile = open("encrypted.txt", "w")

# Read and encrypt
for line in infile:
    encrypted_line = ""
    for char in line:
        if char in codes:
            encrypted_line += codes[char]
        else:
            encrypted_line += char # keep spaces, punctuation
    outfile.write(encrypted_line)

# Close files
infile.close()
outfile.close()

print("Encryption complete. Check encrypted.txt")

# Decryption Program

# Original dictionary
codes = {
'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '!', 'c': '1',
'D': '^', 'd': '2', 'E': '&', 'e': '3', 'F': '*', 'f': '4',
'G': '(', 'g': '5', 'H': ')', 'h': '6', 'I': '-', 'i': '7',
'J': '+', 'j': '8', 'K': '=', 'k': '0', 'L': '{', 'l': '}',
'M': '[', 'm': ']', 'N': ':', 'n': ';', 'O': '"', 'o': "'",
'P': '<', 'p': '>', 'Q': '/', 'q': '?', 'R': '~', 'r': '`',
'S': '|', 's': '\\', 'T': '€', 't': '£', 'U': '¥', 'u': '¢',
'V': '§', 'v': '©', 'W': '®', 'w': '™', 'X': '∆', 'x': 'π',
'Y': '✓', 'y': '✔', 'Z': '◊', 'z': '•',
'.': '○', ',': '●'
}

# Reverse dictionary
decode = {}
for key, value in codes.items():
    decode[value] = key

# Open encrypted file
infile = open("encrypted.txt", "r")

# Read and decrypt
for line in infile:
    decrypted_line = ""
    for char in line:
        if char in decode:
            decrypted_line += decode[char]
        else:
            decrypted_line += char
    print(decrypted_line, end="")

# Close file
infile.close()
