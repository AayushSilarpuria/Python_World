# Interview Q & A from NitMan Talk video 20 Mostly Asked Python Question!!


# Q.1: Write a function calculate, which given a string like "4+1*1+1", 
# return the result of the formula in the string (6). 
# Allowed operations are +,*. Assume all opperands are positive integer.

string1 = "4+1*1+1"
new_str = string1.split("+")

num = [ int(num) for num in string1 if num.isdigit()]
cal_mul = 0

for i in range(len(string1)):
    if string1[i] == '+':
        cal_mul = int(string1[i-1]) * int(string1[i+1])
        print(cal_mul)
        print()
#         if string1[i] == '+':
#             cal += int(string1[i-1]) + int(string1[i+1])
#             print(cal)
# print()
# print(cal)  
# for i in range(len(new_str)):
#     for j in   

print("-------------")

# Q.2: Write fibonacci Series using Generator for 10 range.
# or Generate an infinite fibonacci series by using Genetator.

def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b = b,(a+b)
        
f1 = fibonacci()
print(next(f1))
print(next(f1)) 
print(next(f1)) 
print(next(f1)) 
print(next(f1)) 
print(next(f1)) 
print(next(f1)) 
print(next(f1)) 
print(next(f1)) 
print(next(f1)) 


print("-------------")


# Q.3: Write a decorator and also Write two decorator using same function. 

# Q.4: Write Union of set.

# Q.5: Write a list comprehension for a given list in which even number get squared and odd number get cube.

lst = [1,4,-6,2,-1, 11,9,]
# output = [1, 16, ]

lst1 = [i**2 if i%2==0 else i**3 for i in lst]
print(lst1)

print("-------------")


# Q.6: Write a Dictionary comprehension for a given dictionary in which even number get squared and odd number get cube.

# Q.7: How do you process json 

# Q.8: Convert this dictionary in string.
mydict = {'a': 1,
          'b': 2, 
          'c': 3, 
          'd': 4,
          'e': 5,}

print("-------------")

# Q.9: Send data of mydict into a file in json format. 

# Q.10: Sort A list without using a sort keyword.

list1 = [41,2,12,43,6,778,3,4]
print("Before: ",list1)
n = len(list1)
for i in range(len(list1)):
    for j in range(i+1, n):
        if list1[i] > list1[j]:
            list1[i],list1[j] = list1[j], list1[i]
print("After: ",list1)

print("-------------")

# Q.11: Write a code to check Whether a string is Palindrome or not?

s = input("Write to check Plindrome: ")

if s == s[::-1]:
    print("The string is Palindrome.")
else:
    print("Not Palindrome.")

print("-------------")

s = "AyushsuyA"
n = len(s)
Flag = 0
for i in range(n):
    if s[i] != s[n-i-1]:
        Flag = 1
        break
if Flag == 0:
    print("True")
else:
    print("False")

print("-------------")

# Q.12: Sort a dictionary or by using dict comprehension.

dict1 = { 500: "Apple", 350: "Mango",
      200: "Banana",  250: "Grapes"}

dic = sorted(dict1.keys())
dict2 = {}
for i in dic:
    dict2[i] = dict1[i]

print(dict2)

print("-------------")

#dict2 = {key:value for key,value in sorted(dict1.items(), key = lambda x:x[i])}

print("-------------")

# Q.13: Find the pair of given number in a list with sum equal to 10.

list1 = [3,4,5,1,7,2,8]
k = 10
n = len(list1)
for i in range(n):
    for j in range(i+1, n):
        if list1[i] + list1[j] == k:
            print(list1[i], list1[j])

print()

ni = 5
for i in range(ni):
    for j in range(i+1):
        print("*", end=' ')
    print()

print("-------------")

# Q.14: Create a fibonacci series by using recursion.

def fibonacci(n):
    a = 0
    b = 1
    fib = [0,1]
    if n<=0:
        print("Invalid Input, please insert positive integer.")
    elif n == 1:
        return 1
    elif n == 2:
        return fib
    else:
        for i in range(n):
            c = a+b
            a,b = b,c 
            fib.append(c)
        
    print(fib[-1])
    return fib
print(fibonacci(10))

print("-------------")

# Q.15: Find the required Output.

Input = "the sky is blue"
# Output = "blue is sky the"

a=Input.split()
a = a[::-1]
a = " ".join(a)
print(a)

print()

str10 = "/*apples are & found%  only @red & green"
strn = ""
for i in str10:
    if ((i>= 'a' and i<='z') | (i>= 'A' and i<= 'Z') | (i == ' ')):
        strn += i
print(strn)


print("-------------")

# Q.16: Find the Maximum repeated character in a string without having On2 complexity.

ads = "itinitntyennhhn"
ch = {}
for i in ads:
    if i in ch:
        ch[i] += 1
    else:
        ch[i] = 1
print(ch)
print()

max_chr = max(ch, key= ch.get)
print(max_chr)


print("-------------")

max_ch = ''
count1 = 0 
for i in ads:
    sim = ads.count(i)
    if sim > count1:
        max_ch = i
        coutn1 = 0
print(max_ch)

print("-------------")


# Q.17: Find the maximum and minimum value from a list without using any predefined function.

l = [30,5,88,665,2,0,19]
maximum = l[0]
minimum = l[0]
for i in l:
    if i>maximum:
        maximum = i
    if i < minimum:
        minimum = i
print(f"Maximum number: {maximum}")
print(f"Minimum number: {minimum}")

print("-------------")


