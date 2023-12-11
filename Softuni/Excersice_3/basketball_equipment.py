# Input data
year_payment = int(input("How much is the early payment for the training: "))

# Calculations
snickers = year_payment - (year_payment * 0.4)
clothes = snickers - (snickers * 0.2)
basketball_ball = clothes * 0.25
accessories = basketball_ball * 0.20

# Output data
print(snickers, clothes, basketball_ball, accessories)
