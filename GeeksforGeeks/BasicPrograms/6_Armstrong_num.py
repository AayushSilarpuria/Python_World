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

print()

# Time Complexity: O(logn)
# Space Complexity: O(1)

# Method-2:

def armstrong(num):
    num_str = str(num)
    l = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(str(digit)) ** l
    if sum == num:
        return True
    else:
        return False


num =153 # print(int(input("Enter an number: ")))
print(armstrong(num))

# Time Complexity: O(n)
# Space Complexity: O(1)