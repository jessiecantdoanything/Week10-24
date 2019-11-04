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
def letterToIndex(letter):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    idx = alphabet.find(letter)
    if idx == -1:       #means that it wasn't in the alphabet
        print("error:", letter, "is not in the alphabet")
    return idx


letter = input("wots your mesij")
key = input("wots youe shift")
def letterToIndex(letter, key):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '

    for i in range(0, len(letter) + 1):
        idx = alphabet.find(letter) + key


        if idx > 26:
            idx = idx - 26



    let = ascii_lowercase[idx]


    return let



print(letterToIndex("y", 4))


