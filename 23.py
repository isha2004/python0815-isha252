side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

is_right_triangle = (
    side1**2 + side2**2 == side3**2 or
    side1**2 + side3**2 == side2**2 or
    side2**2 + side3**2 == side1**2
)

if is_right_triangle:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
