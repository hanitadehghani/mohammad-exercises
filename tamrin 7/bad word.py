def filter(sen):
    lst = ["kir", "koon", "chos", "an", "gooz"]
    word = sen.split(" ")
    message = ""
    for i in word:
        if i in lst:
            for j in range(len(i)):
                message += "*"
        else:
            message += " "+i+" "
    return message


print(filter("marde kir kheli koon dad mesle chos"))
