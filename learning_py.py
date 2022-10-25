name = " Irina Musaeva"

# String :
# print the type of var 
print (type(name))

# combine var and str 
print ("Hello there" + name )

# len will count the number of characters in the var
print (len(name)) 

# dir - gives options what we can do with this string
print (dir(name))

#replace option will replace string for what you want, example:
print(name.replace("Irina", "Ira"))
# when you execute this script it will replace Irina to Ira

# # Built in functions :
# dir()
# type()
# len()

# Integer
amount = 120
print (type(amount))

# List can store strings or integer , with integer ww don't need to use ""
cars = ["Toyota", "Jeep", "Lexus"]
print (type(cars))
cars.append ("Ferrari") # append is the option of dir to add a string to a list
print (type(cars)) # it will print the list with new modification

# Tuple - is a list that can not be changed
# use case : data bases - because this data should not be change. Other than that we don't really use tuple
car = 

# Dictionary - key=value , dictionary should start with { and end with }.
user = {
    "name": "Irina" , 
    "age" : 22 , 
    "location": "Skokie , IL"
    }  # 22 here is without "" showing that it is in integer
print(user)
print (type(user))

# floats
number = 34.50
print(number)
print(type(number))

# boolean yes/no , true/false
light = True  #it has to be capital because it is a build in variable
print(light)
print(type(light))

