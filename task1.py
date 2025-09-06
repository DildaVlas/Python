class Rectangle:
    def __init__(self, identifier, x, y, width, height):
        self.identifier = identifier
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def is_intersect(self, other):
        if isinstance(other, Quad):
            # Проверка пересечения прямоугольника и квадрата
            rect_left = self.x
            rect_right = self.x + self.width
            rect_top = self.y
            rect_bottom = self.y + self.height

            quad_left = other.x
            quad_right = other.x + other.side
            quad_top = other.y
            quad_bottom = other.y + other.side

            return not (
                        rect_right < quad_left or rect_left > quad_right or rect_bottom < quad_top or rect_top > quad_bottom)
        else:
            raise TypeError("Unsupported type for intersection check")


class Quad:
    def __init__(self, identifier, x, y, side):
        self.identifier = identifier
        self.x = x
        self.y = y
        self.side = side

    def area(self):
        return self.side ** 2

    def is_intersect(self, other):
        if isinstance(other, Rectangle):
            # Проверка пересечения квадрата и прямоугольника
            quad_left = self.x
            quad_right = self.x + self.side
            quad_top = self.y
            quad_bottom = self.y + self.side

            rect_left = other.x
            rect_right = other.x + other.width
            rect_top = other.y
            rect_bottom = other.y + other.height

            return not (
                        quad_right < rect_left or quad_left > rect_right or quad_bottom < rect_top or quad_top > rect_bottom)
        else:
            raise TypeError("Unsupported type for intersection check")


def compare(t1, t2):
    if isinstance(t1, Rectangle) and isinstance(t2, Quad):
        return t1.area() - t2.area()
    elif isinstance(t1, Quad) and isinstance(t2, Rectangle):
        return t2.area() - t1.area()
    else:
        raise TypeError("Unsupported types for comparison")


# Пример использования
rect = Rectangle("rect1", 0, 0, 4, 4)
quad = Quad("quad1", 2, 2, 4)

print(f"Area of rectangle: {rect.area()}")  # Вывод: Area of rectangle: 16
print(f"Area of quad: {quad.area()}")  # Вывод: Area of quad: 16

print(f"Intersection: {rect.is_intersect(quad)}")  # Вывод: Intersection: True
print(f"Comparison: {compare(rect, quad)}")  # Вывод: Comparison: 0

