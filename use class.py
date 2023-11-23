from Address import Address

# instantiate
hans_meier = Address("Hauptsraße", 12, 84347, "Pfarrkirchen")
senf = Address("Innstraße", 32, 84359, "Simbach")

#print
print(hans_meier.getAddress())
print(senf.getAddress())

print(hans_meier.get_street())

hans_meier.set_street("Friedriech")

print(hans_meier.getAddress())
print(hans_meier.get_street())

##################################

from Circle import Circle

r = int(input("Please enter the radius: "))

circle1 = Circle(r)

print(circle1.getArea())

#