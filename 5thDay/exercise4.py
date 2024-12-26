class MyClass:
    
    def __init__(self, protected_var, private_var):
        self._protected_var = protected_var
        self.__private_var = private_var
    
    def _protected_func(self):
        print("protected function")
        
    def __private_func(self):
        print("protected function")
        
my_obj = MyClass("test1", "test2")

print(my_obj._protected_var)
# print(my_obj.__private_var)

my_obj._protected_func()
my_obj.__private_func()