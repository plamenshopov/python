# Input Data
length_in_centimetres = int(input("Please enter the aquarium LENGTH in centimetres: "))
width_in_centimetres = int(input("Please enter the aquarium WIDTH in centimetres: "))
height_in_centimetres = int(input("Please enter the HEIGHT in centimetres: "))
percentage_of_occupied_space = float(input("Please enter the percentage of occupied space in the aquarium: "))

# Calculations
total_volume_of_the_aquarium = length_in_centimetres * width_in_centimetres * height_in_centimetres
total_volume_in_litres = total_volume_of_the_aquarium * 0.001  # // or "total_volume_of_the_aquarium / 1000"
occupied_space = percentage_of_occupied_space / 100
litres_needed_to_fill_the_aquarium = total_volume_in_litres * (1 - occupied_space)

# Output
print(total_volume_of_the_aquarium)
print(total_volume_in_litres)
print(occupied_space)
print(litres_needed_to_fill_the_aquarium)
