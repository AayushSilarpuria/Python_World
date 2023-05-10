strnew = "AAAAEERCCEETTTAA"

def str1(string):

    count = 1
    newstr1 = ""

    for let in range(len(string)):
        if let == len(string)-1 or string[let] != string[let+1]:
            newstr1 = newstr1 + string[let] + str(count)
            count = 1
        else:
            count += 1
    return newstr1

print(str1(strnew))