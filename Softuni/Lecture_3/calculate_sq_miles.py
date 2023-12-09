print("Please enter a square miles:")
sq_km = int(input())
price_per_sq_km = 7.61

total_price = sq_km * price_per_sq_km
discount = total_price * 0.18
final_price = total_price - discount

print(f'The total price for this order is: {total_price} lv.')
print(f'The calculated discount is: {discount} lv.')
print(f'The final price for you will be: {final_price} lv.')
