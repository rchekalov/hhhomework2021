class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model

    def out(self):
        return [self.mark,self.model]

class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars=[]):
        self.cars = cars

    def add(self,car,index):
        self.cars.insert(index,car)

    def delete(self, index):
        self.cars.pop(index)

    def out(self):
        garage = [car.out() for car in self.cars]
        return garage

if __name__ == '__main__':
    car1 = Car('Mark A','model 1')
    car2 = Car('Mark B', 'model 2')
    car3 = Car('Mark B', 'model 5')
    car4 = Car('Mark C', 'model 1')
    car5 = Car('Mark A', 'model 4')

    print(car1.out(),car2.out(),car5.out())
    print(car4.mark,car4.model)

    garage = Garage([car2,car4,car5])

    print(garage.out())

    garage.add(car3,2)
    garage.delete(1)

    print(garage.out())