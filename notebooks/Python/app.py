# file: my_program.py
class Car2:
    # __init__ is the Constructor — runs automatically when object is created
    def __init__(self, brand, speed):
        print(self)
        self.brand = brand
        self.speed = speed
        print(f"Car object created: {self.brand}")

    def show(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} km/h")

class Car:
    # __init__ is the Constructor — runs automatically when object is created
    def __init__(self, brand, speed):
        print(self)
        self.brand = brand
        self.speed = speed
        print(f"Car object created: {self.brand}")

    def show(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} km/h")


# __name__ is a built-in variable
# When you RUN this file directly  → __name__ == "__main__"
# When you IMPORT this file        → __name__ == "my_program"

print(f"Value of __name__ is: {__name__}")

if __name__ == "__main__":
    print(__name__)
    # This block runs ONLY when file is executed directly
    # NOT when imported by another file
    
    print("--- Program Started ---")
    
    # Creating objects → triggers __init__ automatically
    car1 = Car2("Toyota", 180)
    car2 = Car("BMW", 250)
    
    car1.show()
    car2.show()
    
    print("--- Program Ended ---")


    
