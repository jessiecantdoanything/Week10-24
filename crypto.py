# Transposition Cipher

# encryption function
def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText

def scramble2Decrypt(cipherText):
    halfLenght = len(cipherText) // 2
    evenChars = cipherText[halfLenght:]    # halflenght to the end
    oddChars = cipherText[:halfLenght]     # 0 to halflenght - 1
    plainText = ""

    for i in range(halfLenght):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChar) < len(evenChars):
        plaintext = plainText + evenChars[-1]

    return plainText