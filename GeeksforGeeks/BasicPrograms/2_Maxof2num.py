# Maximum of these two numbers.
def max_num(a,b):
    maxnum = max(a,b)
    print(maxnum)
    #return maxnum 

max_num(2,4)

# GFG:
def maximum(a,b):
    if a>b:
        return a
    else:
        return b
print(maximum(2,4))

# Using Ternary Operation:
a=2
b=4
print(a if a>b else b)

# Time Complexity: O(1)
# Auxiliary Space: O(1)

# Using Lambda function:
maximum = lambda a,b:a if a>b else b
print(f"{maximum(a,b)} is a maximum number")

# Using list comprehension:
x=[a if a>b else b ]
print("maximum number is: ", x)

#Using sort() method:
x = [a,b]
x.sort()
print(x[-1])

# Time Complexity: O(nlogn)
# Auxiliary Space: O(1)
