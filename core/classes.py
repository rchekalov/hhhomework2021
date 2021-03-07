class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструкто
    
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
        
    def add(self, car):
        self.cars.append(car)

    def delete(self, index):
        self.cars.pop(index)

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index == len(self.cars) - 1:
            raise StopIteration
        self.index +=1
        return self.cars[self.index]
        