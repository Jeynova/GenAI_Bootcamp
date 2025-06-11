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