# Program for simple intrest:

# formula: Simple Intrest = (P*R*T)/100
# P = Principle, R = Rate, T = Time 

def sim_int(p,t,r):
    
    si = (p*r*t)/100
    print(f"The Simple Interest is {si}")
    return si

P = int(input("Enter Principle amount: "))
R = int(input("Enter Rate percentage: "))
T = int(input("Enter Time: "))
sim_int(P, T, R)