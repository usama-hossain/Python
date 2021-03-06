import math


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


emp_1 = Employee('Usama', 'Hossain', 100000)

print(emp_1.first)


# Python 3 Object-Oriented Programming - Dusty Phillips; Chapter 2
class Point:
    """Represents a point in two-dimensional geometric coordinates
    """
    
    def __init__(self, x=0, y=0):
        """Initialize the position of a new point. The x
        and y coordinates can be specified. If they are not, the 
        point defaults to the origin.

        Args:
            x (int, optional): x-point. Defaults to 0.
            y (int, optional): y-point. Defaults to 0.
        """
        self.move(x, y)
    
    def move(self, x, y):
        """Move the point to a new location in 2D space.

        Args:
            x (int): x-point
            y (int): y-point
        """
        self.x = x
        self.y = y
        
    def reset(self):
        """Reset the point back to the geometric origin: 0, 0
        """
        self.move(0, 0)

    def calculate_distance(self, other_point):
        """Calculate the distance from this point to a second
        point passed as a parameter.
        
        This function uses the Pythagorean Theorem to calculate the 
        distance between the two points. The distance is 
        returned as a float.

        Args:
            other_point (Point): another Point instance.

        Returns:
            float: returns the square root of difference squared of x, y 
            points.
        """
        return math.sqrt(
            (self.x - other_point.x)**2 +
            (self.y - other_point.y)**2
        )

