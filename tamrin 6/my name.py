def count_hanita(sen):
    h = sen.split(" ")
    count = 0
    for item in h:
        if item == "hanita":
            count += 1

    return count


print(count_hanita(
    "hanita dehghani is good girl, hanita is always good and hanita is pretty girl."))
