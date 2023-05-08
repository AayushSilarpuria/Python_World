# Sum of Square of first n natural numbers.

# Method-1:

def sum_series(n):
    sum1 = 0
    for i in range(1, n+1):
        sum1 = sum1 + (i*i)
    return sum1
num = int(input("Enter Number: "))
print(sum_series(num))

print()

# Time_complexity: O(n)
# Space_complexity: O(1)

# Method-2:

num = int(input("Enter Number to sum of square: "))
squar_list = [i*i for i in range(1, num+1)]
sum_of_list = sum(squar_list)
print(f"Sum of square of first {num} natual number is {sum_of_list}")

print()

# Time_complexity: O(n)
# Space_complexity: O(n)


# Cube sum of first n natural number.

# Method-1:

def sum_cube(n):
    sum1 = 0
    for i in range(1, n+1):
        sum1 += pow(i,3)
    return sum1

num = int(input("Enter for cube: "))
print(sum_cube(num))

print()


# Method-2:

num = int(input("Enter number for cube sum : "))
cube_list = [pow(i,3) for i in range(1, num+1)]
sum_of_cube = sum(cube_list)
print(sum_of_cube)

