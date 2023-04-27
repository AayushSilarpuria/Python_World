# Progrma for compound interest

# Method-1:
def comp(pri, rate, time):
    amount = pri*(pow((1+rate/100), time))
    compound_intrest = amount - pri
    
    return compound_intrest

print(comp(10000, 10.25, 5))

print()

# Method-2: With input

def comp(principle, rate, time):
    amount = principle*(pow((1+rate/100), time))
    compound_intrest = amount - principle
    print("Compound Intrest is {c:1.2f}".format(c = compound_intrest))

principle = int(input("Enter the Principle amount: "))
rate = int(input("Enter the Rate of intrest: "))
time = int(input("Enter the time in years: "))

comp(principle, rate, time)

# Time Complexity: O(1)
# Space Complexity (or Auxiliary space): O(1) 