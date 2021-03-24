class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, manufacturer="", model=""):
        self._manufacturer = manufacturer
        self._model = model

    @property
    def get(self):
        print(self._manufacturer, self._model)
        return {self._manufacturer: self._model}


class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self):
        self._car_list = []

    def __iter__(self):
        return self._car_list.__iter__()

    def __next__(self):
        if self.current == len(self._car_list):
            raise StopIteration
        car = self._car_list[self.current]
        self.current += 1
        return car

    def add(self, car: Car):
        self._car_list.append(car)

    def delete(self, index: int):
        del self._car_list[index]

    @property
    def value(self):
        return self._car_list

    @value.setter
    def value(self, value):
        self._car_list = value


garage = Garage()
# car = Car('memka car', 'model 1')
# print(car.get)
for i in range(10):
    garage.add(Car('memka car', f'model {i}').get)

# garage.add(car.get)
print(garage.value)
