"""
OOP Assignment - 

This file includes:
1. Assignment 1: Design Your Own Class
2. Activity 2: Polymorphism Challenge

Language: Python
"""

# =============================
# Assignment 1: Design Your Own Class
# =============================

class Smartphone:
    # Constructor with attributes
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
    
    # Method to simulate making a call
    def make_call(self, number):
        print(f"📞 Calling {number} from {self.model}...")

    # Method to display phone details
    def details(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")

# Inheritance Example (Adding polymorphism/encapsulation)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        # Call the parent constructor
        super().__init__(brand, model, storage)
        self.gpu = gpu

    # Overriding the details method
    def details(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, GPU: {self.gpu}")

# Testing Assignment 1
print("=== Assignment 1: Smartphone Classes ===")
phone1 = Smartphone("Samsung", "Galaxy S21", 128)
phone1.details()
phone1.make_call("123-456-789")

gaming_phone = GamingPhone("Asus", "ROG Phone 6", 256, "Adreno")
gaming_phone.details()


# =============================
# Activity 2: Polymorphism Challenge
# =============================

class Vehicle:
    def move(self):
        print("The vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky")

class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing on the water")

# Testing Activity 2
print("\n=== Activity 2: Polymorphism Challenge ===")
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
