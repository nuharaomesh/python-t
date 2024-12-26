class MyExample:
    
    def __init__(self):
        self.__data = "My class"
    
    def get_data(self):
        return self.__data
        
    def set_data(self, data):
        self.__data = data
        
example = MyExample()
print(example.get_data(), "Is your data")
example.set_data("Omesh")
print(example.get_data(), "Is your data")