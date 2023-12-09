# Nylon entry data
needed_amount_of_nylon = int(input("Please enter the needed amount of nylon: "))
ask_for_additional_amount_of_nylon = input("Do you want to buy additional amount of nylon?: ")
if ask_for_additional_amount_of_nylon == "yes":
    additional_amount_of_nylon = int(input("Please enter the additional amount of nylon: "))

# Paint entry data
needed_liters_of_paint = int(input("Please enter the needed liters of paint: "))
ask_for_additional_amount_of_paint = input("Do you want to buy additional liters of paint?: ")
if ask_for_additional_amount_of_paint == "yes":
    additional_amount_of_paint = int(input("Please enter the additional liters of paint: "))

# Thinner entry data
needed_liters_of_thinner = int(input("Please enter the needed liters of thinner: "))
ask_for_additional_liters_of_thinner = input("Do you want to buy additional liters of thinner?: ")
if ask_for_additional_liters_of_thinner == "yes":
    additional_amount_of_thinner = int(input("Please enter the additional liters of thinner: "))

# Working hours entry data
working_hours = int(input("How many working hours will be needed: "))
ask_for_additional_amount_of_working_hours = input("Will the workers have to work more hours?: ")
if ask_for_additional_amount_of_working_hours == "yes":
    additional_amount_of_working_hours = int(input("Please enter the additional amount of working hours: "))

# Variables
nylon_price_per_sq_meter = 1.50
paint_price_per_liter = 14.50
thinner_price_per_liter = 5.00

# Nylon calculations
if ask_for_additional_amount_of_nylon == "yes":
    total_sum_for_nylon = (needed_amount_of_nylon + additional_amount_of_nylon) * nylon_price_per_sq_meter
else:
    total_sum_for_nylon = needed_amount_of_nylon * nylon_price_per_sq_meter

# Paint calculations
if ask_for_additional_amount_of_paint == "yes":
    total_sum_for_paint = (needed_liters_of_paint + additional_amount_of_paint) * paint_price_per_liter
else:
    total_sum_for_paint = needed_liters_of_paint * paint_price_per_liter

# Thinner calculations
if ask_for_additional_liters_of_thinner == "yes":
    total_sum_for_thinner = (needed_liters_of_thinner + additional_amount_of_thinner) * thinner_price_per_liter
else:
    total_sum_for_thinner = needed_liters_of_thinner * thinner_price_per_liter

# All materials total sum calculation
total_sum_for_all_materials = total_sum_for_nylon + total_sum_for_paint + total_sum_for_thinner

# Working hours calculations
if ask_for_additional_amount_of_working_hours == "yes":
    total_sum_for_working_hours = ((total_sum_for_all_materials * 0.3) * (working_hours + additional_amount_of_working_hours))
else:
    total_sum_for_working_hours = ((total_sum_for_all_materials * 0.3) * working_hours)

# Output
print(f'You ordered {int(needed_amount_of_nylon + additional_amount_of_nylon)} sq. meters of nylon and the total price for it will be: {total_sum_for_nylon} USD')
print(f'The total price for the paint will be: {total_sum_for_paint} USD')
print(f'The total price for the thinner will be: {total_sum_for_thinner} USD')
print(f'The total price for the all needed materials will be: {total_sum_for_all_materials} USD')
print(f'We need to pay the workers {total_sum_for_working_hours} USD for {working_hours} working hours')
print(f'The total amount for the repairs will be: {int(total_sum_for_working_hours + total_sum_for_all_materials)} USD')
