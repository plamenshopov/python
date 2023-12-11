# Entry data
needed_amount_of_nylon = int(input("Please enter the needed amount of nylon: "))
needed_liters_of_paint = int(input("Please enter the needed liters of paint: "))
needed_liters_of_thinner = int(input("Please enter the needed liters of thinner: "))
working_hours = int(input("How many working hours will be needed: "))

# Variables
nylon_price_per_sq_meter = 1.50
paint_price_per_liter = 14.50
thinner_price_per_liter = 5.00

# Calculations
total_sum_for_nylon = needed_amount_of_nylon * nylon_price_per_sq_meter
total_sum_for_paint = needed_liters_of_paint * paint_price_per_liter
total_sum_for_thinner = needed_liters_of_thinner * thinner_price_per_liter
total_sum_for_all_materials = total_sum_for_nylon + total_sum_for_paint + total_sum_for_thinner
total_sum_for_working_hours = ((total_sum_for_all_materials * 0.3) * working_hours)

# Output
print(f'The total price for the nylon will be: {total_sum_for_nylon} USD')
print(f'The total price for the paint will be: {total_sum_for_paint} USD')
print(f'The total price for the thinner will be: {total_sum_for_thinner} USD')
print(f'The total price for the all needed materials will be: {total_sum_for_all_materials} USD')
print(f'We need to pay the workers {total_sum_for_working_hours} USD for {working_hours} working hours')
print(f'The total amount for the repairs will be: {int(total_sum_for_working_hours + total_sum_for_all_materials)} USD')
