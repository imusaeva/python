weight = int(input("weight: "))
type = (input("(K)g: " + "or " + "(L)bs :"))
if type.upper() == "K":
    print("weight in pound: " + str(weight / 0.45))
else:
    print("weight in kilogram: " + str(weight * 0.45))