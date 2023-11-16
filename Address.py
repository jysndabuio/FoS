class Address:

    # constructor
    def __init__(self, street, number, postalcode, city):
        self.street = street
        self.number = number
        self.postalcode = postalcode
        self.city = city

    def getAddress(self):
        return self.street + " " + str(self.number) + ", " + \
            str(self.postalcode) + " " + self.city

    #getter and setter
    def get_street(self):
        return self.street

    def get_postalcode(self):
        return self.postalcode
    def set_street(self, street):
        self.street = street

    def set_street(self, pc):
        self.postalcode = pc