# Prompt user to enter  number / test if even or odd

input = input("Please enter an integer: ")
number = int(input)

if number % 2 == 0: #if the number is a multiple of 2
    print("Your number is even. ")
else:
    print("Your number is odd. ")