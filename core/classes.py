from typing import List


class Car:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        super().__init__()


class Garage:
    def __init__(self, car_list: List[Car]):
        self.car_list = car_list
        super().__init__()

    def __iter__(self):
        return iter(self.car_list)

    def add(self, car: Car):
        self.car_list.append(car)

    def delete(self, car_index: int):
        self.car_list.pop(car_index)
