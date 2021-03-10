class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model
    pass

class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # ??? НЕ НАШЕЛ -> не понял что нужно сделать
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, car_list):
        self.car_list = car_list
    def add(self, new_car):
        self.car_list.append(new_car)
    def delete(self, n):
        self.car_list.pop(n)
    pass