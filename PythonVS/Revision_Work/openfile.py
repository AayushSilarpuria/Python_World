# Interview task to open and read file then write it.

# Text file write, read and append:

with open("Revision_Work/myfile.txt", mode='w') as mf:
    mf.write("Hello World \n")

with open("Revision_Work/myfile.txt", mode='r') as mf:
    print(mf.read())

with open("Revision_Work/myfile.txt", mode='a') as mf:
    mf.write("New line add just now")

with open("Revision_Work/myfile.txt", mode='r') as mf:
    print(mf.read())

# Excel file write then read:

with open("Revision_Work/file.xlsx", mode="w+") as fi:
    fi.write("New record\n 1st record")

with open("Revision_Work/file.xlsx", mode='r+') as fi:
    print(fi.read())


print()

# from random import shuffle
import json

mydict = {'a': 1,
          'b': 2, 
          'c': 3, 
          'd': 4,
          'e': 6,}

with open("Revision_Work/myfile2.txt", "a" ) as fi:
    fi.write(json.dumps(mydict)+'\n')
with open("Revision_Work/myfile2.txt", "r" ) as fi:
    print(fi.read())



with open('Revision_Work/myfile3.txt', 'r') as input,\
    open('Revision_Work/myfile4.txt', 'w') as output:
    text = input.readlines()
    uppercase = [t.upper() for t in text]
    output.writelines(uppercase)