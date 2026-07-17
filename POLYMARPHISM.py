class Car:
    def move(self):
        print("Driving on the road!")

class Boat:
    def move(self):
        print("Sailing through water!")

# Unified iteration loop
for vehicle in [Car(), Boat()]:
    vehicle.move() 
# Output:
# Driving on the road!
# Sailing through water!
