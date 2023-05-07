# Program to check Prime Number:

# Method-1:

def count_p(num):
    if num>1:
        for i in range(2, int(num/2)+1):
            if num%i == 0:
                print(f"{num} is not a prime number.")
                break
        else:
            print(f"{num} is a prime number.")
    else:
        print(f"{num} is out of range.")

in_num = int(input("Enter the number: "))
count_p(in_num)

print()

# Time_Complexity: O(n)
# Space_Complexity: O(1)

# Method-2:

from math import sqrt

n = int(input("Enter Number: "))

prime_flag = 0     # This flag maintains status whether the n is prime or not. 

if(n>1):
    for i in range(2, int(sqrt(n))+1):
        if (n%i == 0):
            prime_flag = 1
            break
    if prime_flag == 0:
        print("True")
    else:
        print("False")
else:
    print("False")


print()

# Method-3: Using math

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

num = int(input("Enter number to check prime: "))
print(is_prime(num))

print()

# Time_Cpmplexity: O(sqrt(n))
# O(sqrt(n)) because we traverse all number in the range of 2 to sqrt(n)+1,
# to check if n is divisible by any of them.

# Space_Complexity: O(1)
# O(1) because we only using constant amount of memory to store the input number n,
# and the loop variable.

# Method-4: Trial_Division_Method

def is_prime_trial(n):

    if n<=1:
        return False
    
    for i in range(2, int(n**0.5)+1):

        if n%i == 0:
            return False
    return True

num = int(input("Enter the number: "))
print(is_prime_trial(num))

# Time_Cpmplexity: O(sqrt(n))
# Space_Complexity: O(sqrt(n))
