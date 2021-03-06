from collections.abc import Iterable


class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, make, model):
        self.make = make
        self.model = model


class Garage(Iterable):
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars=None):
        if cars is None:
            cars = []
        self.cars = cars

    def __iter__(self):
        return self.cars.__iter__()

    def add(self, car):
        self.cars.append(car)

    def delete(self, index):
        return self.cars.pop(index)
