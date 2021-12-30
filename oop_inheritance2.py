class Shape:
    def __init__(self, x,y):
        self.X = x
        self.Y = y

    def area(self):
        result = self.X * self.Y
        print("THE AREA IS ", result)

    def perimeter(self):
        result= 2 * self.X+2 * self.Y
        print("THIS IS PERIMETER", result)

class Rectangle(Shape):
    def __init__(self,x,y):
        self.X = x
        self.Y = y

class Square(Shape):
    def __init__(self,x):
        self.X = x
        self.Y = x

#original class called
Square_object =Shape(20,30)
Square_object.area()
Square_object.perimeter()

#inheritance by parent class
#we used parent class method
Rectangle_object = Rectangle(50,30)
Rectangle_object.area()
Rectangle_object.perimeter()

#inheritance by parent class
#we used parent class method
Square_object= Square(50)
Square_object.area()
Square_object.perimeter()