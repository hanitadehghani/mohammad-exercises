
def max(sentence):
    sen = sentence.lower()
    newWords = sen.split(" ")
    myDict = {}

    for item in newWords:
        if item in myDict:
            myDict[item] += 1
        else:
            myDict[item] = 1

    Max = 0
    for i in myDict:
        if myDict[i] > Max:
            Max = myDict[i]
    for i in myDict:
        if myDict[i] == Max:
            maximum = i
    return maximum


print(max("hanita mohammad mohammad mohammad hanita"))
