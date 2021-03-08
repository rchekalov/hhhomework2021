class Car(object):
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, brand, model):
        self.model = model
        self.brand = brand
    pass

class Garage(object):
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars):
        self.cars = cars
    
    def add(self, car):
        if (type(car) == "Car"):
            self.cars.add(car)
        else:
            print("Add only car")
    def delete(self, index):
        self.cars.sli
    def indexOf(self, car):
        if (type(car) == "Car"):
            idx = self.cars.indexOf(car)
            if (idx > 0):
                return idx
            else:
                print("Значение не найдено")
                return -1
        else:
            print("Только класс Car")
            return -1
    pass