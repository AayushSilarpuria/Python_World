# Program to find sum of array:

# Method-1:

arr = {1,2,3}
print(sum(arr))

print()

# Method-2:

from collections import Counter

arr = [12,3,4,15]

c = Counter(arr)
sum = 0

for key,value in c.items():
    sum += key*value
print(f"Sum of the array is {sum}")

print()