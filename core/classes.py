class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор

    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def __str__(self):
        return self.model + ' ' + self.brand


class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража

    def __init__(self, cars):
        self.cars = cars

    def __iter__(self):
        return iter(self.cars)

    def __str__(self):
        return ' '.join(str(car) for car in self.cars)

    def add(self, car):
        self.cars.append(car)

    def delete(self, index):
        self.cars.pop(index)


if __name__ == '__main__':
    car1 = Car('m1', 'b1')
    car2 = Car('m2', 'b2')
    cars = [car1, car2]

    garage = Garage(cars)

    print(garage)

    car3 = Car('m3', 'b3')

    garage.add(car3)

    print(garage)

    garage.delete(1)

    print(garage)

    for car in garage:
        print(car)
