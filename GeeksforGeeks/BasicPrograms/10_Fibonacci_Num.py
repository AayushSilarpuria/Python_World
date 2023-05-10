# Program for n-th Fibonacci number:

def fibonacci(n):
    if n <= 0:
        print("INCORRECT INPUT") # First Fibonacci number is 0.
    elif n == 1:
        return 0 # Second Fibonacci number is 1.
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Enter number: "))
print(fibonacci(num))

print()

# Time_Complexity: O(2^n)
# Space_Complexity: O(n)

# Method-2:

fibarray = [0,1]

def fibonacci(n):
    if n<0:
        print("Incorrect Input")
    elif n<= len(fibarray):
        return fibarray[n-1]
    else:
        temp_fib = fibonacci(n-1) + fibonacci(n-2)
        fibarray.append(temp_fib)
        return temp_fib

print(fibonacci(9))
print(fibarray)

print()

# Time_Complexity: O(n)
# Space_Complexity: O(n)

fiblist = [0,1]
# print(len(fiblist))
def fib(n):
    if n < 0:
        print("Invalid input")
    elif n<=len(fiblist):
        return fiblist[n-1]
    else:
        new_fib = fib(n-1) + fib(n-2)
        fiblist.append(new_fib)
        return new_fib
print(fib(9))
print(fiblist)

print()

# Method-3:
def fibo(n):
    if n<=0:
        return "Incorrect Output"
    data = [0,1]
    if n > 2:
        for i in range(2,n):
            datanow = data[i-1] + data[i-2]
            data.append(datanow)
    return data[n-1]
    print(data)
print(fibo(10))


print()

# Time_Complexity: O(n)
# Space_Complexity: O(n)

# Method-4:

def fibonacci1(n):
    a = 0
    b =1
    fib = [0,1]
    if n<= 0:
        print("Incorrect Input! Please enter positive ineger.")
    elif n == 1:
        return a
    elif n==2:
        return fib
    else:
        for i in range(2,n): 
            c = a + b
            a,b = b,c
            fib.append(c)
        return fib
    
print(fibonacci1(11))

print()
print("---------------ANOTHER_WAY-------------------")
print()

fib = [0,1]
def fibonacci1(n):
    a = 0
    b =1
    
    if n<= 0:
        print("Incorrect Input! Please enter positive ineger.")
    elif n == 1:
        return a
    elif n==2:
        return fib
    else:
        for i in range(2,n): 
            c = a + b
            a,b = b,c
            fib.append(c)
        return b

d = int(input("Enter fibonacci number:: "))    
print(fibonacci1(d))
print(fib)


# Time_complexity: O(n)
# Space_complexity: O(1)