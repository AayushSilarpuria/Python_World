# Program to find largest element in an array.

# Method-1:

arr = [1,23,4,6,55]
print(max(arr))

print()

# Method-2:

def largest(arr, n):
    
    maximum = arr[0]
    for i in range(1, n):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum

# Driver Code:
arr = [10, 3231, 44, 776, 9298]
n = len(arr) 
Ans = largest(arr, n)
print(f"Largest number in given array {Ans}.")

print()

# Time_Complexity: O(n)
# Space_Complexity: O(1)

# Method-3:

def large(arr):
    arr.sort()
    return arr[-1]

arr = [10, 3231, 44, 776, 9298]
print(f"Maximum Number of array is {large(arr)}.")

print()

# Method-4:

from functools import reduce

def large(arr):

    an = reduce(max, arr)
    return an

arr = [1,27,3780,344,53,836,1707,80,2239,1010]
print(f"Large_Large_Large number is {large(arr)}.")

# Time_Complexity: O(n)
# Space_Complexity: O(1)