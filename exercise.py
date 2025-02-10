weight = input ("weight: ")
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = float(weight) / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    print("Weight in Kg: "+ weight)