class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"My dog  {self.name}  is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class JackRussellTerrier(Dog):
    def speak(self, sound = "Arf"):
        return f"{self.name} says {sound}"


class Dachshund(Dog):
    def speak(self, sound="Wof"):
        return f"{self.name} says {sound}"


class Bulldog(Dog):
    def speak(self, sound="WAF WAF"):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):
    def speak(self, sound = "Bark"):
        return super().speak(sound)

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
gr = GoldenRetriever("GG", 8
                     )

print(jim.speak())
print(buddy.speak())
print(gr.speak())
