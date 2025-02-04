#3. Define a class named `Rectangle` which inherits from `Shape` 
# class from task 2. Class instance can be constructed by a `length` and `width`. 
# The `Rectangle` class has a method which can compute the `area`.
class shape:
    def area(self):
        return 0

class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length*self.width

shape= shape()
print(shape.area())
rectangle= rectangle(6,7)
print(rectangle.area())