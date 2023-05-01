# Program to find area of circle:

# Method-1:

def area(r):
    pi = 3.14
    area1 = pi* (r**2)
    return area1
print("Area is %.2f " %area(int(input("Enter radius of circle: "))))

print()

# Method-2:

import math

def area(r):
    area1 = math.pi *pow(r,2)
    return print(f"Area of circle is: {area1:.2f}")
area(int(input("Enter radius of circle: ")))

# Time Complexity: O(1)
# Auxiliary Space: O(1)
