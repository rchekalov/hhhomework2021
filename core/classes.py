# Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
# Поля должны задаваться через конструктор

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __repr__(self):
        return "Car({})".format(self.brand)

    pass


# Написать класс гаража Garage, у которого есть поле списка машин
# Поле должно задаваться через конструктор
# По аналогии с классом Company из лекции реализовать интерфейс итерируемого
# Реализовать методы add и delete(удалять по индексу) машин из гаража

class Garage:

    def __init__(self, cars=None):
        if cars is None:
            cars = []
        self.cars = cars

    def __iter__(self):
        return iter(self.cars)

    def __next__(self):
        return next(self.cars)

    def add(self, car):
        self.cars.append(car)
        pass

    def delete(self, index):
        self.cars.pop(index)
        pass

    def __repr__(self):
        return 'Garage({})'.format(self.cars)

    pass
