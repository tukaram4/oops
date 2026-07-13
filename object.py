# Defining a class (blueprint)
class Dog:
    def __init__(self, name):
        self.name = name  # Attribute

    def bark(self):
        return "Woof!"  # Method

# Creating an object (instance)
my_dog = Dog("Buddy")

# Accessing attributes and methods
print(my_dog.name)  # Output: Buddy
print(my_dog.bark())  # Output: Woof!
