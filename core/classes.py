class Car:
    """
    Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    Поля должны задаваться через конструктор
    """

    def __init__(self, brand: str, model: str):
        self.__model = model
        self.__brand = brand

    def __str__(self):
        return f"Car({self.__brand}, {self.__model})"

    def __repr__(self):
        return self.__str__()


class Garage:
    """
    Написать класс гаража Garage, у которого есть поле списка машин
    Поле должно задаваться через конструктор
    По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    Реализовать методы add и delete(удалять по индексу) машин из гаража
    """

    def __init__(self, cars):
        self.__cars = cars

    def add(self, car: Car):
        self.__cars.append(car)

    def delete(self, index: int):
        self.__cars = [car for i, car in enumerate(self.__cars) if i != index]

    def __str__(self):
        cars = [car.__str__() for car in self.__cars]
        return f"Garage({len(self.__cars)}, {', '.join(cars)})"

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        self.__current = 0
        return self

    def __next__(self):
        if self.__current == len(self.__cars):
            raise StopIteration
        car = self.__cars[self.__current]
        self.__current += 1
        return car


if __name__ == '__main__':
    car0 = Car('brand1', 'model1')
    car1 = Car('brand1', 'model2')
    car2 = Car('brand1', 'model3')
    car3 = Car('brand2', 'model1')
    car4 = Car('brand2', 'model2')
    car5 = Car('brand3', 'model1')
    car6 = Car('brand3', 'model2')
    car7 = Car('brand3', 'model3')
    car8 = Car('brand3', 'model4')
    car9 = Car('brand4', 'model1')

    garage = Garage([car0, car1, car2, car4, car5, car7, car8])

    print(garage)
    garage.add(car3)
    print(garage)
    garage.delete(2)
    print(garage)
    cars = [car for car in garage]
    print(cars)
