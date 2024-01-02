import math

figure_type = str(input("What type of figure do you have: "))

if figure_type == "square":
    square_side_length = float(input("Please enter the square side length: "))
    print(f"The area of the square is {square_side_length * square_side_length:.3f} ")
elif figure_type == "rectangle":
    rectangle_side_one = float(input("Please enter the first rectangle side length: "))
    rectangle_side_two = float(input("Please enter the second rectangle side length: "))
    rectangle_area = rectangle_side_one * rectangle_side_two
    print(f"The area of the rectangle is {rectangle_area:.3f}")
elif figure_type == "circle":
    circle_radius = float(input("Please enter the diameter of the circle: "))
    circle_area = (circle_radius ** 2) * math.pi
    print(f"The area of the circle is {circle_area:.3f}")
elif figure_type == "triangle":
    triangle_side_one = float(input("Please enter the first triangle side length: "))
    triangle_side_two = float(input("Please enter the second triangle side length: "))
    print(f"The area of the triangle is {(triangle_side_one * triangle_side_two) / 2:.3f}")
