def reverse(num):
    numbers = [1,2,3,4,5,6,7]

    newList = []
    for item in numbers:
        if item == num:
            newList.append(item)
            numbers.reverse()
            for n in numbers:
                if n == num:
                    return newList
                newList.append(n)
                
        else:
            newList.append(item)
    # return newList
print(reverse(7))
