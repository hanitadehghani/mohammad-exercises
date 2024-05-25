def filter(sen):
    lst = ["kir", "koon", "chos", "an", "gooz",
           "kos", "jaghi"]
    message = ""
    word = sen.split(" ")
    for i in lst:
        badWord = sen.index(i)
        for q in word:
            if q in badWord:
                message += len(q)+"*"
            else:
                message += q

    return message


print(filter("marde kiri koon goshad"))
