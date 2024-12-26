class Car:
    
    category = "merced"
    
    def __init__(self, model, color):
        self.model = model
        self.color = color
        
    def display(self):
        print(self.model, self.color)
        
    def update(self, model, color):
        self.tick = model
        self.model = model
        self.color = color
        print(self.model, self.color)
    
    def test(self):
        print("Asdasd") 

        
new_car = Car("merced", "Black")
new_car.display()
new_car.update("merced up", "Black up")

print(Car.category)