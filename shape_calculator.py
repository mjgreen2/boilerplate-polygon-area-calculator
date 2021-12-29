#Solution to Polygon Area Calculator
#Created in Visual Studio Code
#By Michael Green

class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.printed_object ="Rectangle"

    def set_height(self, newHeight):
        self.height = newHeight

    def set_width(self, newWidth):
        self.width = newWidth

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return (2 * self.height) + (2 * self.width)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)
        #diagonal = sqrt(w^2 + h^2)

        '''* `get_picture`: Returns a string that represents the shape using lines of "\*". 
        The number of lines should be equal to the height and the number of "\*" 
        in each line should be equal to the width. There should be a new line (`\n`) 
        at the end of each line. If the width or height is larger than 50, this should return the string: 
        "Too big for picture.".'''
    def get_picture(self):

        if self.height > 50 or self.width > 50:
            return "Too big for picture."

        picture = ""

        for heightCntr in range(0, self.height, 1):
            for widthCntr in range(0, self.width, 1):
                picture += '*' 
            picture += '\n'

        return picture

        '''* `get_amount_inside`: Takes another shape (square or rectangle) as an argument. 
        Returns the number of times the passed in shape could fit inside the shape (with no rotations). 
        For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
        '''
    def get_amount_inside(self, Rectangle):  #how many times Rectangle fits inside self
        amount = self.get_area()/Rectangle.get_area()
        return int(amount)

        '''
        Additionally, if an instance of a Rectangle is represented as a string, it should look like: 
        `Rectangle(width=5, height=10)`
        '''
    def __str__(self):
        self.printed_object ="Rectangle"
        self.printed_object += "(width=" + str(self.width) + ", height=" + str(self.height) + ")"
        return self.printed_object

'''
#### Square class
The Square class should be a subclass of Rectangle. 
When a Square object is created, a single side length is passed in. 
The `__init__` method should store the side length in both the `width` and `height` attributes 
from the Rectangle class.

The Square class should be able to access the Rectangle class methods but should also contain 
a `set_side` method. If an instance of a Square is represented as a string, it should look like: 
`Square(side=9)`

Additionally, the `set_width` and `set_height` methods on the Square class should set both 
the width and height.'''
class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side
        self.printed_object = "Square"

    def set_height(self, newSide):
        self.height = newSide
        self.width = newSide

    def set_width(self, newSide):
        self.width = newSide
        self.height = newSide

    def set_side(self, newSide):
        self.width = newSide
        self.height = newSide

    def __str__(self):
        self.printed_object = "Square"
        self.printed_object += "(side=" + str(self.width) + ")"
        return self.printed_object