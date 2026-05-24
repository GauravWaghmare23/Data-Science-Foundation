# Polymorphism in Python

#compile time polymorphism or method overloading

class Math:
    def add(self, a, b, c=0):
        return a + b + c
    
    def multiply(self, a, b, c=1):
        return a * b * c
    
    def power(self, a, b):
        return a ** b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."
        
math = Math()
print(math.add(2, 3))          # Output: 5

print(math.add(2, 3, 4))       # Output: 9


# runtime polymorphism or method overriding

class Animal:
    def sound(self):
        return "Some sound"
    
class Dog(Animal):
    def sound(self):
        return "Woof!"
    
class Cat(Animal):
    def sound(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())