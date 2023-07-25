def revers(n):
    message = ""
    for letter in range(len(n)-1, -1, -1):
        message += n[letter]
    return message


print(revers("hanita"))
