import math

# HW_1

import math

def sector_area(radius, angle_degrees):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)

    # Calculate the area of the sector
    area = (math.pi * radius ** 2) * angle_radians / (2 * math.pi)

    print(f"The area of the sector with radius {radius} and angle {angle_degrees} degrees is: {area:.2f} square units.")

# Test the function
radius = 5
angle_degrees = 60
sector_area(radius, angle_degrees)