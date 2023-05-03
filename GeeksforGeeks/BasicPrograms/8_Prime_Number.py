# Program for Prime Number:

# Method-1:

def prime(num):
    
    # Limit the range of num
    if num < 2:      
        return 0
    
    # Fix already prime number
    primes = [2]

    # Counter going up to input num
    st = 3

    while st <= num:
        for se in range(3,st,2):
            if st%se == 0:
                st += 2
                break
        else:
            primes.append(st)
            st += 2
    print(primes)
    print(len(primes))

prime(6)

print()


# Method-2: 

def prime(x,y):
    prime_list = []

    for i in range(x, y):
        if i == 0 or i == 1:
            return 0
        
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

# Driver Program:
starting_range = int(input("Enter Starting value of range: "))
ending_range = int(input("Enter End value of range: "))
list_prime = prime(starting_range, ending_range)
if len(list_prime) == 0:
    print("There are no prime number in this range.")
else:
    print("The prime number in this range are: ", list_prime)


print()
