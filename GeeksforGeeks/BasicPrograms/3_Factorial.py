# Iterative Approach:
 # Method 1:
def fact(num):
    if num == 1 or num == 0:
        return 1
    elif num<0:
        return 0
    else:
        n = 1
        while num>1:
            n *= num
            num -= 1
        return n
print(fact(5))

 # Method 2:
def factorial(n):
    res = 1
    
    for i in range(2, n+1):
        res *= i
    return res

n=5
print("Factorial of", n , "is", factorial(n),".")

 # Time Complexity: O(n)
 # Auxiliary Space: O(1)

# Recursive approach or Using Ternary Operation(One line solution):

    # def fact(nums):
    #     return 1 if (n==1 or n==0) else nums * fact(nums-1)

    # num = 5
    # print("Fact of", num, "is", fact(num))

 # RecursionError: maximum recursion depth exceeded
   
   # Time Complexity: O(n)
   # Auxiliary Space: O(n)

# By using build-in method:

import math 
def fact(n):
    return math.factorial(n)

num = 5
print("Fact of", num, "is", fact(num))

 # Time Complexity: O(1)
 # Auxiliary Space: O(1)

# Using numpy:

import numpy
n = 5
num = numpy.prod([i for i in range(1,n+1)])
print(num)

 # Time Complexity: O(n)
 # Auxiliary Space: O(1)