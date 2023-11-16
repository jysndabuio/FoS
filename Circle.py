# create the class Circle
# create the constructor with passing the radius
# create a function which returns the area of that circle (math library)
# write the main, instantiate the class and get the area

import math

class Circle:

    def __int__(self, radius):
        self.radius = radius

    def getArea(self):
        return 2 * math.pi * self.radius

