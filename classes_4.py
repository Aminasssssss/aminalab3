#4. Write the definition of a Point class. Objects from this class should have a
#   - a method `show` to display the coordinates of the point
#   - a method `move` to change these coordinates
#    - a method `dist` that computes the distance between 2 points

import math  

class Point:
    def __init__(self, x, y):
        self.x = x  
        self.y = y  

    def show(self):
        print(f"Points: ({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance


point1 = Point(1,4)  
point2 = Point(3,5) 

point1.show()  
point2.show()  


point1.move(7,8)
point1.show()  


point2.move(3,9)
point2.show()  

distance = point1.dist(point2)
print(f"Dictance: {distance:.2f}")  
