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
    def __init__(self, list = []):
        self.cars = list
    
    def add(self, car):
        self.cars.append(car)
    
    def delete(self, index):
        length = len(self.cars)
        if length == 0:
            print('в гараже нет машин для удаления')
            return
        elif index > length - 1 or index < 0:
            print('нет машины с таким индексом')
            return         
        self.cars.pop(index)
    
    def __iter__(self):
        return iter(self.cars)