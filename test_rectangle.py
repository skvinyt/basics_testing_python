class Rectangle:
    def __init__(self, width=0, height=0):
        self.set_dimensions(width, height)

    def set_dimensions(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

# Тесты с использованием doctest
def test_rectangle():
    """
    >>> rect = Rectangle(3, 4)
    >>> rect.get_area()
    12
    >>> rect.get_perimeter()
    14

    >>> rect.set_dimensions(5, 6)
    >>> rect.get_area()
    30
    >>> rect.get_perimeter()
    22

    >>> rect.set_dimensions(0, 0)
    >>> rect.get_area()
    0
    >>> rect.get_perimeter()
    0

    >>> rect.set_dimensions(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: Width and height must be non-negative
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
