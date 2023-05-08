# Check if a given number is Fibonacci Number:

import math 

# function return true only if x is perfect square.
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

# function return true if n is a Fibonacci number, else false.
def isfibonacci(n):

    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n-4)

n = int(input("Enter number upto check Fibonacci: "))
for i in range(1,n):
    if (isfibonacci(i) == True):
        print(i, "is a Fibonacci Number.")
    else:
        print(i, "is a not fibonacci number.")
        
        