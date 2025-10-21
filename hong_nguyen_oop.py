import datetime
import math

class GeometricObject:
    """A general class for geometric objects."""

    def __init__(self, color = "white", filled = False):
        """
        Initializes a GeometricObject with a color, filled status, and creation date.
        """
        self._color = color
        self._filled = filled
        self._dateCreated = datetime.datetime.now()

    # Getter method for color
    def get_color(self):
        """Returns the color of the object."""
        return self._color

    # Setter method for filled
    def set_color(self, new_color):
        """Sets the color of the object."""
        self._color = new_color

    # Getter method for color
    def get_filled(self):
        """Returns the filled status (Boolean) of the object."""
        return self._filled

    # Setter method for filled
    def set_filled(self, filled):
        """Sets the filled status (Boolean) of the object."""
        if isinstance(filled, bool):
            self._filled = filled
        else:
            print("Error: 'filled' must be a boolean (True/False).")

    def __str__(self):
        """Returns a string representation of the GeometricObject."""
        return (f"created on {self._dateCreated}\n"
                f"Color of object is {self._color}\n"
                f"Filled: {self._filled}")

class Circle(GeometricObject):
    """A specialized GeometricObject representing a Circle."""

    def __init__(self, radius = 1.0, color="blue", filled=True):
        """
        Initializes a Circle, inheriting from GeometricObject.
        Calls the base class constructor first.
        """
        super().__init__(color, filled)
        self._radius = radius

    # Getter for radius
    def getRadius(self):
        """Returns the radius of the circle"""
        return self._radius

    # Setter for radius
    def setRadius(self, radius):
        """Sets the radius of the circle with input validation."""
        try:
            r = float(radius)
            if r > 0:
                self._radius = r
            else:
                print("Error: Radius must be positive.")

        except ValueError:
            print("Error: Radius must be a number.")

    # Specialized methods
    def getArea(self):
        """Calculates and returns the area of the circle."""
        return math.pi * self._radius**2

    def getPerimeter(self):
        """
        Calculates and returns the perimeter (circumference) of the circle.
        We call it getPerimeter to match the general GeometricObject concept.
        """
        return 2 * math.pi * self._radius

    def __str__(self):
        """Returns a string representation of the Circle."""
        # Use the base class __str__ and modify the first line
        base_str = super().__str__()
        # The '1' at the end of the replace() method specifies the maximum number of times the substitution should occur.
        formatted_base_str = base_str.replace("created on", "A circle was created on", 1)

        return (f"{formatted_base_str}\n"
                f"The radius is {self._radius}\n"
                f"The area is {self.getArea()}\n"
                f"The perimeter is {self.getPerimeter()}")

class Rectangle(GeometricObject):
    """A specialized GeometricObject representing a Rectangle."""

    def __init__(self, width=1.0, height=1.0, color="red", filled=False):
        super().__init__(color, filled)
        self._width = float(width)
        self._height = float(height)

    # Getter for width
    def getWidth(self):
        """Returns the width of the rectangle."""
        return self._width

    # Setter for width
    def setWidth(self, width):
        """Sets the width of the rectangle with input validation."""
        try:
            w = float(width)
            if w > 0:
                self._width = width
            else:
                print("Error: Width must be positive.")
        except ValueError:
            print("Error: Width must be a number.")

    # Getter for height
    def getHeight(self):
        """Returns the height of the rectangle."""
        return self._height

    # Setter for height
    def setHeight(self, height):
        """Sets the height of the rectangle with input validation."""
        try:
            h = float(height)
            if h > 0:
                self._height = h
            else:
                print("Error: Height must be positive.")
        except ValueError:
            print("Error: Height must be a number.")

    # Specialized methods
    def getArea(self):
        """Calculates and returns the area of the rectangle."""
        return self._width * self._height

    def getPerimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self._height + self._width)

    # String representation method
    def __str__(self):
        """Returns a string representation of the Rectangle."""
        # Use the base class __str__ and modify the first line
        base_str = super().__str__()
        formatted_base_str = base_str.replace("created on", "A rectangle was created on", 1)

        return (f"{formatted_base_str}\n"
                f"The width is {self._width}\n"
                f"The height is {self._height}\n"
                f"The area is {self.getArea()}\n"
                f"The perimeter is {self.getPerimeter()}")

while True:
    try:
        radius_input = input("Enter the radius of your choice: ")
        circle_radius = float(radius_input)

        if circle_radius <= 0:
            print("Radius must be a positive number. Please try again.")
            continue
        break

    except ValueError:
        print("Invalid input. Please enter a number for the radius.")

# 1. Create the Circle object (uses default color='blue', filled=True)
my_circle = Circle(radius = circle_radius)

# 2. Create the Rectangle object (uses specified arguments)
test_rectangle = Rectangle()
test_object = GeometricObject(color="black", filled=True)

my_rectangle = Rectangle(width=4.0, height=2.0, color="red", filled=False)

print("-" * 30)

# Print the circle results using the __str__ method
print(my_circle)

print("-" * 30)

# Print the rectangle results using the __str__ method
print(my_rectangle)












