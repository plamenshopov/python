mackerel_price = float(input())
sprinkle_price = float(input())
bonito = float(input())
safrid = float(input())
mussels = int(input())
mussels_price = 7.50

bonito_price = (mackerel_price * 0.6) + mackerel_price
bonito_total = bonito * bonito_price

safrid_price = (sprinkle_price * 0.8) + sprinkle_price
safrid_total = safrid * safrid_price

mussels_total = mussels * mussels_price
total_fish = bonito_total + safrid_total + mussels_total

print(f"{total_fish:.2f}")
