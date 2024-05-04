from .coordinate import Coordinate


class Vehicle:
    """Представляет авто с параметрами."""

    def __init__(self, name, model, year, color, price, latitude, longitude, id=None):
        self.id = id
        self.name = name
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"<Vehicle: {self.name} {self.model} {self.year} {self.color} {self.price}>"

    def coordinate(self):
        return Coordinate(self.latitude, self.longitude)
