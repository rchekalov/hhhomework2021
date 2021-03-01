from collections.abc import Iterable

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Garage(Iterable):
    def __init__(self, cars = []):
        self.cars = cars

    def __iter__(self):
        return self.cars.__iter__()

    def add(self, car):
        self.cars.append(car)

    def delete(self, index):
        self.cars.pop(index)
