# Print ASCII Value of a character.

# Method-1: For Letters and number.

Input_letter = input("Enter letter: ")
let = ord(Input_letter)
print(f"The ASCII value of {Input_letter} is {let}.")

print()

# Method-2: For String

Input_string = input("Enter the string: ")
stringlen = print(len(Input_string))
for let in Input_string:
    ascii_code = ord(let)
    print(f"ASCII OF LETTER {let} is {ascii_code}.")