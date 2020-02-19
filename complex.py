import math

class ComplexNumber:
    real = 0.0
    imaginary = 0.0

    def __init__(self, real, imaginary = 0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, obj):
        real = self.real + obj.real
        imaginary = self.imaginary + obj.imaginary
        return ComplexNumber(real, imaginary)

    def __sub__(self, obj):
        real = self.real - obj.real
        imaginary = self.imaginary - obj.imaginary
        return ComplexNumber(real, imaginary)

    def __mul__(self, obj):
        real = (self.real * obj.real) - (self.imaginary * obj.imaginary)
        imaginary = (self.real * obj.imaginary) + (self.imaginary * obj.real)
        return ComplexNumber(real, imaginary)

    def __neg__(self):
        real = -self.real
        imaginary = -self.imaginary
        return ComplexNumber(real, imaginary)

    def __str__(self):
        return "{}+{}i".format(self.real, self.imaginary)

    @staticmethod
    def exp(val):
        real = math.exp(val.real) * math.cos(val.imaginary)
        imaginary = math.sin(val.imaginary)
        return ComplexNumber(real, imaginary)