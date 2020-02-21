import math

class Vector2:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, obj):
        x = self.x + obj.x
        y = self.y + obj.y
        return Vector2(x, y)

    def __mul__(self, obj):
        x = self.x * obj
        y = self.y * obj
        return Vector2(x, y)

    def __truediv__(self, obj):
        x = self.x / obj
        y = self.y / obj
        return Vector2(x, y)

    @staticmethod
    def dot(a, b):
        return a.x * b.x + a.y * b.y

    def magnitude2(self):
        return Vector2.dot(self, self)

    def magnitude(self):
        return math.sqrt(self.magnitude2())

    def normalized(self):
        return self / self.magnitude()
