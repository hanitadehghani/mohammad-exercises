def even(names):
    lst = []
    for item in names:
        if len(item) % 2 == 0:
            lst.append(item)
    return lst


print(even(['hanita', 'mohammad', 'helena', 'armin', 'sana', 'amin', 'arman']))
