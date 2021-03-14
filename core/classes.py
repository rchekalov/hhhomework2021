class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    class Car:
        def __init__(self, mark, make):
            self.mark = mark
            self.make = make


class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars=list[Car]):
        self.cars = cars

    def __iter__(self):
        return iter(self.cars)

    def add(self, car):
        self.cars.append(car)

    def delete(self, index):
        self.cars.pop(index)
