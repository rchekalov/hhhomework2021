class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model

class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars):
        self.cars = cars

    def add(self, car):
        self.cars.append(car)

    def delete(self, index):
        del self.cars[index]

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current == len(self.cars):
            raise StopIteration
        car = self.cars[self.current]
        self.current += 1
        return car
