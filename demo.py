"""Dummy challenge for Kitt Demo"""



import math

def circle_area(radius):
    """
    Returns the area of the circle of given radius.
    If the radius is negative, return 0.
    """
    if radius > 0:
        return radius * radius * math.pi
    else:
        return 0
    