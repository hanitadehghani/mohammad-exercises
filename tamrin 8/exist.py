def found(string):
    lowercase = string.lower()
    new = lowercase.split(" ")

    if "hanita" in new:
        print("found")
    else:
        print("notfound")


found("mersi komak behem mikoni az tarafe Hanita ")
