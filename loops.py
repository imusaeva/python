print("Hello there")
name = input("what is your name:") #input is build in
print("Nice to meet you" + name)

# for loop will print strings in order one by one
names = ["Irina", "Raya", "Akmaral", "Alisher"]
for name in names:
    print(name)

# if statement
if "Irina" in names:
    print("Irina is here")

for name in names:
    x = len(name)
    if x > 5:
        print("Thats Alisher")
    elif x <= 5:
        print("Not Alisher")


# functions: def - defining the function
def function1():
    print("hello world")
print(function1()) # call the function1 

