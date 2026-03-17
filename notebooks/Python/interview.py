class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 
    
    def show(self):
        print(f"I have a {self.year} {self.make} {self.model}.")

if __name__ == '__main__':   
    car1 = car("Honda", "Accord", 1998)
    car1.show()


       