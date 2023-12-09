value = input("Въведи стойност: ")
value2 = input("Какво въвеждаш - km, mile: ")
km_value = "km"
mile_value = "mile"

if value2 == km_value:
    value = float(value)
    mile = value * 0.621371192
    print("Разстоянието в мили е: ", mile)
elif value2 == mile_value:
    value = float(value)
    km = value * 1.609344
    print("Разстоянието в километри е: ", km)
else:
    print("Грешка във въвеждането на стойностите.")
    exit(-1)

