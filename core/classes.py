class Car:
    def __init__(self, brand=None, model=None):
        self.brand = brand
        self.model = model


class Garage:
    def __init__(self, cars=None):
        self.cars = cars
        if cars is None:
            self.cars = []

    def add(self, car):
        self.cars.append(car)
        return 'ok'

    def delete(self, index):
        if len(self.cars) != 0:
            return self.cars.pop(index)

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        if self.cursor + 1 >= len(self.cars):
            raise StopIteration()
        self.cursor += 1
        return self.cars[self.cursor]
