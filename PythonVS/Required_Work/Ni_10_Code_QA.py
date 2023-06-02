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

