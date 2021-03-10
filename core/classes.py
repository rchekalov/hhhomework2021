class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, _mark, _model):
        self.mark = _mark
        self.model = _model


class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    cars = []

    def __init__(self, _cars):
        self.cars = _cars

    def add(self, car):
        self.cars.add(car)

    def delete(self, idx):
        self.cars.delete(idx)