#Scalene triange: all sides have different lenghts.
#Isosceles triangle: Two sides have the same length.
#Equilateral triangle: All sides are equal

a = int(input("the length of side a= "))
b = int(input("the length of side b= "))
c = int(input("the length of side c= "))

if a != b and b != c and a != c:
    print("\033[1;34m This is a scalene triangle. \n")
elif a == b and b == c:
    print("\033[1;32m This is an equilateral triangle. \n")
else:
    print("\033[1;33m This is an isosceles triangle. \n")