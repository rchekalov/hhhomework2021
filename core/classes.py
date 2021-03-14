class Car(object):
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, brand, model):
        self.model = model
        self.brand = brand


class Garage(object):
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars=None):
        if (cars == None):
            self.cars = []
        else:
            self.cars = cars

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current == len(self.cars):
            raise StopIteration
        car = self.cars[self.current]
        self.current += 1
        return car
    def __prev__(self):
        if self.current == 0:
            raise StopIteration
        car = self.cars[self.current]
        self.current -= 1
        return car 
    def add(self, car):
        if (type(car) == "Car"):
            self.cars.append(car)
        else:
            print("Add only car")

    def delete(self, index):
        return self.cars.pop(index)

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
