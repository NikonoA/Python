class User:
    def __init__(self, first_name, last_name):
        self.fn = first_name
        self.ln = last_name

    def sayFN(self):
        print("My name is", self.fn)

    def sayLN(self):
        print("My last name is", self.ln)

    def sayAll(self):
        print("My full name is", self.fn, self.ln)
