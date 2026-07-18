1. Basic Concepts & Types of InheritanceQ: What are the different types of inheritance supported by Python?Python supports five distinct structural variations of inheritance:Single Inheritance: A child class inherits directly from one single parent class.Multiple Inheritance: A child class inherits features from more than one parent class.Multilevel Inheritance: A child class inherits from a parent, which itself is a child of another base class (forming a vertical chain).Hierarchical Inheritance: Multiple different child classes all inherit from a single parent class.Hybrid Inheritance: A complex architecture that combines two or more of the types listed above.Q: How do you verify an object's type or class inheritance lineage?Interviewers frequently ask this to verify your knowledge of built-in type-checking tools:isinstance(object, Class): Returns True if the object is an instance of that specific class or any subclass derived from it.issubclass(ChildClass, ParentClass): Returns True if the first class directly or indirectly inherits from the second class.2. Constructor Execution & super()Q: What is the role of super() and how do you call a parent constructor?The super() function returns a proxy object that delegates method calls to a parent or sibling class. It allows a child class to invoke its parent's __init__ constructor so that inherited attributes are properly initialized alongside new child-specific attributes.pythonclass Person:
    def __init__(self, name):
        self.name = name  # Initialize parent attribute

class Employee(Person):
    def __init__(self, name, employee_id):
        # Call the parent class constructor
        super().__init__(name) 
        self.employee_id = employee_id  # Initialize child attribute

emp = Employee("Alice", "E101")
print(emp.name, emp.employee_id)  # Output: Alice E101
Use code with caution.3. Advanced Mechanics: MRO & The Diamond ProblemQ: What is the Diamond Problem, and how does Python solve it?The Diamond Problem occurs in multiple inheritance when a child class inherits from two parent classes, and both of those parent classes inherit from the exact same base class. This creates ambiguity regarding which version of a shared method should be called.Python cleanly resolves this ambiguity using the C3 Linearization Algorithm, which establishes a deterministic Method Resolution Order (MRO). You can view this order explicitly for any class by printing ClassName.__mro__ or calling ClassName.mro().pythonclass A:
    def process(self):
        print("Class A")

class B(A):
    def process(self):
        print("Class B")

class C(A):
    def process(self):
        print("Class C")

class D(B, C):
    pass

obj = D()
obj.process()  # Output: Class B

# Checking the resolution hierarchy:
print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
Use code with caution.Why this output? Python looks at class D first. Because B is listed before C in class D(B, C):, Python searches B next and instantly executes its process() method.4. Code Architecture: Inheritance vs. CompositionQ: What is the difference between Inheritance and Composition? When should you choose one over the other?This architectural question separates junior developers from senior engineers. It boils down to structural relationships:FeatureInheritanceCompositionRelationship"Is-A" relationship (e.g., a Car is a Vehicle)."Has-A" relationship (e.g., a Car has an Engine).CouplingTightly coupled. Changes in the parent impact the child.Loosely coupled. Component internals can change safely.FlexibilityStatic. Relationships are locked during compilation.Dynamic. Behavior can be swapped out at runtime.Rule of Thumb: Default to composition to build flexible, modular code systems. Only use inheritance if you need to deeply customize, extend, or override a large portion of a parent class's behavior.5. Private Attributes & Access ControlQ: Are private variables inherited in Python? How does Name Mangling work?Python does not feature strict access specifiers like private or protected found in other object-oriented languages. Instead, it uses variable naming conventions:Protected (_variable): A single underscore acts as a warning to developers that the variable is intended for internal use. It is fully accessible by child classes.Private (__variable): A double underscore triggers Name Mangling. Python internally rewrites the variable name as _ClassName__variable to prevent accidental overriding in a subclass.pythonclass Parent:
    def __init__(self):
        self.__private_var = "Secret"

class Child(Parent):
    def show(self):
        # This will raise an AttributeError:
        # print(self.__private_var)
        
        # This works because of name mangling:
        print(self._Parent__private_var) 

obj = Child()
obj.show()  # Output: Secret
