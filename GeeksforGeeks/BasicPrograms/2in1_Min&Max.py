# Maximum { max() } & Mininum { min() } : 

# These functions are used to compute the maximum and minimum of the values as passed in its argument.
# or it gives the lexicographically largest value and lexicographically smallest value respectively, 
# when we passed string or list of strings as arguments.

# Syntax: max(x1, x2, ...., xn, key= Function_name)
# key: function that serves as a key for the min/max comparison 
# function_name: It denotes which type of operation you want to perform on these arguments.
# Let,function_name=len.

# Laxicographical order: 
# It is a generalization of the alphabetical order of the dictionaries to sequences of ordered symbols.

l = ["ab", "abc", "abd", "b"]
l1 = "abc"
print(max(l))  # 'b'
print(min(l))  # 'ab'

print(max(l1)) # 'c'
print(min(l1)) # 'a'

print(max(l, key=len)) # "abc"

# Using Function:

def fun(element):
    return (len(element))

l = ["ab", "abc", "abd", "b"]
print(max(l, key=fun))          # "abc"

# Using Lmbda Function:

print(max(l, key = lambda element: len(element)))  # "abc"

# Using Dictionary:

l = [{'name':'ramu', 'score':90, 'age':24},
     {'name':'golu', 'score':70, 'age':19}]

print(max(l, key= lambda item: item.get('age')))
