print("Please enter a number to convert: ")
value = int(input())
print("Please choose the unit type (inch / cent): ")
value2 = input()

if value2 == "cent":
    print(float(value / 2.54))
elif value2 == "inch":
    print(float(value * 2.54))
else:
    print("Error!!!")
