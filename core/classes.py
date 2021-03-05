class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars):
        self.cars = cars

    def __iter__(self):
        for car in self.cars:
            yield car

    def add(self, car):
        self.cars.append(car)

    def delete(self, index):
        self.cars.pop(index)
