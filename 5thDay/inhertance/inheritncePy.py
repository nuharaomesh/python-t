class Animal:
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass
    
class Dog(Animal):
    
    def __init__(self, name, color):
        self.color = color
        super().__init__(name)
        
    def speak(self):
        print(self.color, self.name, "speak baw baw")
        
class Cat(Animal):
    
    def speak(self):
        print(self.name, "speak meow meow")
        
dog = Dog("Roxy", "black")
dog.speak()