def count_words(sentence):
    sen = sentence.lower()
    newWords = sen.split(" ")
    myDict = {}

    for item in newWords:
        if item in myDict:
            myDict[item] += 1
        else:
            myDict[item] = 1
    return myDict


print(count_words("Millions of people in the United States consider autumn to be football season. Football is a very popular sport that is played at high schools, colleges, and professional stadiums"))
