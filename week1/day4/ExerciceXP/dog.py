""" 🌟 Exercise 2: Dogs

Goal: Create a Dog class with methods for barking, running speed, and fighting.


Key Python Topics:

    Classes and objects
    Methods
    Attributes


Instructions:

Step 1: Create the Dog Class

    Create a class called Dog with name, age, and weight attributes.
    Implement a bark() method that returns “ is barking”.
    Implement a run_speed() method that returns weight / age * 10.
    Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight.


Step 2: Create Dog Instances

    Create three instances of the Dog class with different names, ages, and weights.


Step 3: Test Dog Methods

    Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.


Example (Conceptual, No Direct Solution):

class Dog:
    def __init__(self, name, age, weight):
        # ... code to initialize attributes ...

    def bark(self):
        # ... code to return bark message ...

    def run_speed(self):
        # ... code to return run speed ...

    def fight(self, other_dog):
        # ... code to determine and return winner ...

# Step 2: Create dog instances
#... your code here

# Step 3: Test dog methods
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))
 """
class Dog:
    def __init__(self, name: str, age: int, weight: int):
        if age <= 0 or weight <= 0:
            raise ValueError("Age and weight must be positive.")
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other: "Dog"):
        my_power = self.run_speed() * self.weight
        their_power = other.run_speed() * other.weight
        if my_power > their_power:
            return f"{self.name} wins the fight"
        elif my_power < their_power:
            return f"{other.name} wins the fight"
        return "It's a draw"

dog1 = Dog("MEdor", 3, 20)
dog2 = Dog("Rex", 5, 25)
dog3 = Dog("Cubitus", 2, 15)

print(dog1.bark())
print(f"{dog2.name}'s run speed: {dog2.run_speed():.2f}")
print(dog1.fight(dog2))