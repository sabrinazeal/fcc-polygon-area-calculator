class Rectangle:
    """Contains geometric properties of a rectangle."""

    def __init__(self, width, height):
        """Initializes rectangle attributes."""
        self.width = width
        self.height = height

    def __str__(self):
        """Defines rectangle string representation."""
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        """Sets rectangle width."""
        self.width = width

    def set_height(self, height):
        """Sets rectangle height."""
        self.height = height

    def get_area(self):
        """Returns rectangle area."""
        return self.width * self.height

    def get_perimeter(self):
        """Returns rectangle perimeter."""
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        """Returns rectangle diagonal."""
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        """Returns rectangle drawing made of asterisks."""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""
        for row in range(0, self.height):
            picture += ("*" * self.width + "\n")
        return picture

    def get_amount_inside(self, inner_shape):
        """Returns how many times a second shape (rectangle/square) can fit inside the rectangle."""
        horizontal_fit = int(self.width / inner_shape.width)
        vertical_fit = int(self.height / inner_shape.height)
        return horizontal_fit * vertical_fit


class Square(Rectangle):
    """Contains geometric properties of a square."""

    def __init__(self, side):
        """Initializes the Rectangle parent class."""
        super().__init__(width=side, height=side)
        self.side = side

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        """Sets square side."""
        self.side = self.width = self.height = side

    def set_width(self, width):
        """Sets square width."""
        self.set_side(width)

    def set_height(self, height):
        """Sets square height."""
        self.set_side(height)
