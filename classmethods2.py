class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = round(self.pi * (self.radius ** 2), 2)
        self.circumference = round(2 * self.pi * self.radius, 2)

    # def get_area(self):
    #     return self.pi * (self.radius ** 2)

    # def get_circumference(self):
    #     return 2 * self.pi * self.radius


circle1 = Circle(5)
# ca1 = circle1.get_area()
# # cc1 = circle1.get_circumference()
# print(ca1)
# print(round(cc1, 2))
print(circle1.area)
print(circle1.circumference)
