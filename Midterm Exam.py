class Circle:
    def __init__(self):
        self.radius = float(input("Enter the radius of the circle: "))
        self.diameter = 2 * self.radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius


c = Circle()
print("Area of circle:", c.area())
print("Perimeter of circle:", c.perimeter())
