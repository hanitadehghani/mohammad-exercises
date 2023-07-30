def abcd(letters):
    lowerLetter = letters.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in lowerLetter:
        alphabet = alphabet.replace(i, '')
        if alphabet == '':
            return True
    return False


print(abcd("abcdefghijklmnopqrstuvwxyz"))
