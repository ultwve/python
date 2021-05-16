# Weight converter

weight = float(input("Weight?"))
unit = input("(L)bs or (K)g?")

if unit.upper() == "K":
    print(weight*2.2)
elif unit.upper() == "L":
    print(weight*0.45)
else:
    print("Error, please verify your input")