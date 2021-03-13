class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'Car(brand={self.brand}, model={self.model})'

class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars):
        self.cars = cars

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1

        if self.index >= len(self.cars):
            raise StopIteration
        
        car = self.cars[self.index]
        return car

    def __str__(self):
        res = ""
        for car in self:
            res += str(car) + "\n"
        return res

    def add(self, car):
        self.cars.append(car)
    
    def delete(self, i):
        del self.cars[i]
