# Base Class (Parent)
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_info(self):
        return f"Brand: {self.brand}, Speed: {self.speed} km/h"

# Derived Class (Child)
class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        # Initialize parent attributes
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def honk(self):
        return "Beep beep!"