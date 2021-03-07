class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars = []):
        self.cars = cars

    def __iter__(self):
        return self.cars.__iter__()

    def add(self, car):
        self.cars.append(car)

    def delete(self, index):
        self.cars.pop(index)

    def __iter__(self):
        self.num = -1
        return self

    def __next__(self):
        if(self.num == len(self.cars) - 1):
            raise StopIteration
        self.num += 1
        return self.cars[self.num]