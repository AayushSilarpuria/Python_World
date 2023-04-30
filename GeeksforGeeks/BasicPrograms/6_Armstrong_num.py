# Program to check Armstrong Number

# Method-1:

n = int(input("Enter number: "))
s = n 
b = len(str(n))
sum1 = 0

while n != 0:
    r = n%10
    sum1 = sum1+(r**b)
    n = n//10
if s == sum1:
    print("The given number", s, "is Armstrong Number.")
else:
    print("The given number", s, "is not Armstrong Number.")