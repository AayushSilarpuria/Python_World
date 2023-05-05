# Program to check Prime Number:

# Method-1:

def count_p(num):
    if num>1:
        for i in range(2, int(num/2)+1):
            if num%i == 0:
                print(f"{num} is not a prime number.")
                break
        else:
            print(f"{num} is a prime number.")
    else:
        print(f"{num} is out of range.")

in_num = int(input("Enter the number: "))
count_p(in_num)

