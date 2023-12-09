deposit_amount = float(input("Enter the amount of deposit: "))
months = int(input("Enter the number of months: "))
yearly_interest_rate = float(input("Enter the yearly interest rate: "))

total_interest = deposit_amount * yearly_interest_rate / 100
monthly_interest = total_interest / 12
total_sum = deposit_amount + months * monthly_interest

print("total sum: ", total_sum)