def filter(sen):
    lst = ["kir", "koon", "chos", "an", "gooz",
           "kos", "jaghi"]
    word = sen.split(" ")
    message = ""
    for i in word:
        if i in lst:
            for j in range(len(i)):
                message += "*"
        else:
            message += " "+i+" "
    return message


print(filter("marde kiri koon dad be an agha mesle gooz dar chos"))
