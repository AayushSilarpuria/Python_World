# Program to add two numbers:
Num1 = int(input("Enter Num1: "))
print(Num1)
Num2 = int(input("Enter Num2: "))
print(Num2)
sum = Num1+Num2
print(f"Sum of number {Num1} and {Num2} is {sum}")
print("\n")

# Different approach:
if __name__ == "__main__":


    num1 = int(input("Enter Num1: "))
    num2 = int(input("Enter Num2: "))

    sum_twoNum = lambda num1, num2 : num1 + num2

    print(f"Sum of number {num1} and {num2} is {sum_twoNum(num1, num2)}")


    # Time complexity: O(1)
    # Auxilary Space: O(1)