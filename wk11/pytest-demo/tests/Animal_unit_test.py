import unittest

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I make sounds"

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class TestAnimalOperations(unittest.TestCase):
    def test_Animal(self):
        dog = Dog("Buddy")
        cat = Cat("Whiskers")
        
        self.assertEqual(dog.speak(), "Woof!")
        self.assertEqual(cat.speak(), "Meow!")
        

if __name__ == '__main__':
    unittest.main()
