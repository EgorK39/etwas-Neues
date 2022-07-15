import requests


class Rectangle:
    def __init__(self, a, b):
        self.a = a #Breite
        self.b = b #Lange

    def get_area(self):
        return self.a * self.b
