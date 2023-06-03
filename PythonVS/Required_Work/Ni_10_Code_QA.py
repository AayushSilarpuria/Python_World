# NitMan Talks:
# 10 Coding Questions Asking in Interviews:

# Q.1: Plindrome:
def palindrome(s):
    temp = s[::-1]
    if s == temp:
        print("Yes! It is a plindrome.")
    else: 
        print("No! It is not Plindrome.")

def pal2(s):
    ls = len(s)
    for i in range(ls):
        if s[i] != s[ls-i-1]:
            return False
    return True

def pal3(s):
    # rev_s = reversed(s)
    # print(rev_s)
    # for i in rev_s:
    #     print(i)
    temp = ''.join(reversed(s))
    #print(temp)
    if s == temp:
        return True
    else:
        return False
    

def pal4(s):
    ls = len(s)
    first = 0
    last = ls-1
    while(first < last):
        if s[first] == s[last]:
            first += 1
            last -= 1
        else:
            return False
    return True

s = "AyushsuyA"
palindrome(s)
print(pal2(s))
print(pal3(s))
print(pal4(s))
print()
# Palindrome with number:

# By using split method - converting num into string.
# Not Preferred:

def palin(n):
    cs = str(n)
    rev = s[::-1]
    if cs == rev:
        return True
    else:
        return False
    

def palin2(n):
    temp = n #123
    rev_n = 0
    while(temp>0):
        digit = temp%10 #3
        rev_n = rev_n*10 + digit #3
        temp = temp//10 # 12
        if n == rev_n:
            return True
        else:
            return False
        

n = 12345654321
print(palin(n))
print(palin2(n))
print()

# Q.2: Fibonnaci Series

def fibonnaci(n):
    a, b = 0, 1
    print(a)
    while (b<n):
        print(b)
        c = a+b
        a,b = b,c
    print(c)

fibonnaci(7)
print()

def fibo2(n):
    a,b = 0,1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            print(c)

fibo2(7)
print()

# Recurtion:

def fibo(n):
    if n<=1:
        return n
    else:
        return (fibo(n-1) + fibo(n-2))

n = 7
if n<= 0 :
    print("Invalid")
else:
    for i in range(n):
        print(fibo(i))

print()
# Q.3: Compress String:
# Input: 
inp = "aabbccddeeeefffiiiii"
# output: "a2b2c2d4"

def compr(inp):
    n = len(inp)
    string = ""
    for i in range(n):
        if inp[i] not in string:
            string += inp[i] + str(inp.count(inp[i]))
    return string

print(compr(inp))

# Method-2:

def compress(s):
    n = len(s)
    new_s = ''
    count = 1
    for i in range(n-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            new_s += s[i] + str(count)
            count = 1
    new_s += s[n-1] + str(count)
    return new_s

print(compress(inp))

# Method-3:

def compress2(s):
    n = len(s)
    new_s = ""
    i = 0
    while (i<n-1):
        count = 1
        while(i<n-1 and s[i]== s[i+1]):
            count+=1
            i += 1
        i += 1
        new_s += s[i-1] + str(count)
    return new_s

print(compress(inp))
print()
# Q.3: FizzBuzz Problem:
# If number divisible by 3 - print Fizz
# If number divisible by 5 - print Buzz
# If number divisible by 15 - print FizzBuzz

def fzzbzz(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0: #i%15 == 0
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)
fzzbzz(15)
print()

def fizzbuzz2(n):
    d = {3: 'fizz',
         5: 'Buzz'}
    
    for i in range(1,n+1):
        result = ''
        for k,v in d.items():
             if i%k == 0:
                 result += v
        if not result:
            result = i
        print(result)
    
fizzbuzz2(15)
print()

# Q.4: Character Occurence:

# 1. Least repeating character in a string.
print("1. Least repeating character in a string.")


def least_char_occ(s):
    print(s)
    ch = {}
    for i in s:
        if i in ch:
            ch[i] = ch[i]+1
        else:
            ch[i] = 1
    print(ch)
    result = min(ch, key=ch.get)
    print(result)

s = "aaabbggjjjeejjuutteflajdlkj"
least_char_occ(s)

# Using inbuilt functions counter:

from collections import Counter
s = "aaabbggjjjeejjuutteflajdlkj"
ch = Counter(s)
result = min(ch, key=ch.get)
print(result)
print()

# 2. Count of an perticular element.
print("2. Count of an perticular element.")


def count_char_occu(s, search_ch):
    ch = {}
    for i in s:
        if i in ch:
            ch[i] = ch[i]+1
        else:
            ch[i] = 1
    print(ch)
    try:
        print(ch[search_ch])
    except:
        print(0)
s = "aaabbggjjjeejjuutteflajdlkj"
#im = input("Enter letter: ")
count_char_occu(s, "m")
print()


# 3. Count of all values.
print("3. Count of all elements.")


def count_all(s):
    ch = {}
    for i in s:
        if i in ch:
            ch[i] = ch[i]+1
        else:
            ch[i] = 1
    print(ch)

s = "aaabbggjjjeejjuutteflajdlkj"
count_all(s)
print()

# Q.5: Prime Number:

def prime_num(n):
    if n < 2:
        return 0
    
    pri = [2]
    x = 3
    while x <= n:
        for i in range(3,x,2):
            if x%i == 0:
                x += 2
                break   
        else:
            pri.append(x)
            x += 2
    print(pri)

prime_num(100)


# Method-2:

def prime_num(n):
    flag = False
    if n>1:
        for i in range(2,(n//2+1)):
            if n%i == 0:
                flag = True
                break
    if flag:
        return "No! its not a prime number."
    else:
        return "Yes! its a prime number."
print(prime_num(4))


# Method-3:

def prime3(n):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i == 0:
                print("No! its not prime.")
                break
        else:
            print("Yes! Its prime.")
    else:
        print("No! its not prime.")
prime3(3)
print()


# Method-4:
print("Mehtod-4:")

def prime4(start, end):
    for n in range(start, end):
        if n>1:
            for i in range(2, n//2+1):
                if n%i == 0:
                    break
            else:
                print(n)
prime4(13,100)

# Q.6: Modify String Format:

input = "I_Am_Coder"
# output = i.aM.cODER

def string_m(string):
    temp = string.split('_')
    #print(temp)
    str_new = []
    for i in temp:
        str_new.append(i[0].lower() + i[1:].upper())
    #print(str_new)
    return ".".join(str_new)

print(string_m(input))

# Using String

def string_m1(senta):
    tmp = senta.split('_')
    senta_new = ""
    for i in tmp:
        senta_new += i[0].lower() + i[1:].upper() + '.'
    return "".join(senta_new[:-1])

print(string_m1(input))


