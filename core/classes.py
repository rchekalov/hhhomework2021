class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return 'brand = {}, model = {}'.format(self.brand, self.model)


class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars):
        self.cars = cars

    def add(self, car):
        self.cars.append(car)

    def delete(self, i):
        del self.cars[i]

    def __iter__(self):
        self.iter_number = 0
        return self

    def __next__(self):
        if self.iter_number < len(self.cars):
            result = self.cars[self.iter_number]
            self.iter_number += 1
            return result
        else:
            raise StopIteration


def print_garage(garage):
    for it in garage:
        print(it)
    print('')


if __name__ == '__main__':
    garage = Garage([Car('b1', 'm1'), Car('b2', 'm2'), Car('b3', 'm3')])
    print_garage(garage)
    garage.add(Car('b4', 'm4'))
    print_garage(garage)
    garage.delete(1)
    print_garage(garage)
