value = input("Въведи стойност: ")
value2 = input("Какво въвеждаш - km, mile: ")

if value2 == "km":
    print(value + " километра е равно на " + str(int(value) / 1.6) + " мили ")
elif value2 == "mile":
    print(value + " мили е равно на " + str(int(value) * 1.6) + " километра ")
else:
    print("Something happened :( ")
    exit(-1)
