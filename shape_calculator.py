class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ""
            i = 0
            while self.height > i:
                picture += self.width * "*" + "\n"
                i += 1
            picture.rstrip()
            return picture

    def get_amount_inside(self, other):
        self_area = self.get_area()
        other_area = other.get_area()
        amount_inside = int(self_area / other_area)
        return amount_inside


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, new_side):
        super().set_width(new_side)
        super().set_height(new_side)
