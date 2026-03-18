# file: other_program.py

import app   # importing the above file
import app as app1  # importing the above file

print("I am in other_program")

if __name__ == "__main__":
     print("--- Program Started ---")

     car = app1.Car("BMW", 250)
     car.show()
     print("--- Program Ended ---")