class Address:

    def __init__(self, index, city, street, house, apartment):
        self.ind = index
        self.cit = city
        self.str = street
        self.hous = house
        self.apart = apartment

    def __str__(self):
        return f"{self.ind}, {self.cit}, {self.str}, {self.hous}, {self.apart}"
