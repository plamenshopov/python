# Entry data
number_of_pens = int(input("Please enter number of pen packages: "))
number_of_markers = int(input("Please enter number of marker packages: "))
cleaning_detergent = int(input("Please enter number of bottles: "))
price_discount_percentage = int(input("Please enter the discount in percentages: "))

# Variables
price_per_pen_package = 5.80
price_per_marker_package = 7.20
price_per_cleaning_detergent_bottle = 1.20

# Calculations
total_price_for_pen_packages = number_of_pens * price_per_pen_package
total_price_for_marker_packages = number_of_markers * price_per_marker_package
total_price_for_detergent_bottles = cleaning_detergent * price_per_cleaning_detergent_bottle
total_price_for_all_products = (total_price_for_pen_packages
                                + total_price_for_marker_packages
                                + total_price_for_detergent_bottles)
total_discounted_price = total_price_for_all_products - (total_price_for_all_products * price_discount_percentage / 100)

# Output
print(f'Your total price for all needed products is: {total_price_for_all_products}')
print(f'Your discounted price is: {total_discounted_price}')
