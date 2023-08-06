import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        # Check if the sides form a valid triangle
        if not self._is_valid_triangle():
            raise ValueError("Invalid sides for a triangle")

    def _is_valid_triangle(self):
        return (
                self.a + self.b > self.c
                and self.b + self.c > self.a
                and self.a + self.c > self.b
        )

    def get_sides(self):
        return self.a, self.b, self.c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        s = self.get_perimeter() / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

    def get_triangle_type(self):
        if self.a == self.b == self.c:
            return "Equilateral"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Isosceles"
        else:
            return "Irregular"

# Example usage:
try:
    triangle = Triangle(5, 5, 5)  # Equilateral triangle
    print("Sides:", triangle.get_sides())
    print("Perimeter:", triangle.get_perimeter())
    print("Area:", triangle.get_area())
    print("Triangle type:", triangle.get_triangle_type())
except ValueError as error:
    print("Error:", error)

try:
    triangle2 = Triangle(3, 4, 5)  # Right-angled triangle (Irregular)
    print("Sides:", triangle2.get_sides())
    print("Perimeter:", triangle2.get_perimeter())
    print("Area:", triangle2.get_area())
    print("Triangle type:", triangle2.get_triangle_type())
except ValueError as error:
    print("Error:", error)

try:
    triangle3 = Triangle(5, 5, 8)  # Isosceles triangle
    print("Sides:", triangle3.get_sides())
    print("Perimeter:", triangle3.get_perimeter())
    print("Area:", triangle3.get_area())
    print("Triangle type:", triangle3.get_triangle_type())
except ValueError as error:
    print("Error:", error)
