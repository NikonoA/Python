class Address:

    def __init__(self, index, city, street, home, flat):
        self.ind = index
        self.c = city
        self.str = street
        self.h = home
        self.f = flat

    def __str__(self):
        return f"{self.ind}, {self.c}, {self.str}, {self.h} - {self.f}"
