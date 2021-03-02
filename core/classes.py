class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __repr__(self):
        return f"Car[model={self.model}, brand={self.brand}]"

class CarIterator():

    def __init__(self, car_list):
        self.car_list = car_list
        self.counter = -1

    def __next__(self):
        while self.counter < len(self.car_list) - 1:
            self.counter += 1
            return self.car_list[self.counter]
        raise StopIteration

class Garage:

    def __init__(self, car_list):
        self.car_list = [car for car in car_list if type(car) == Car]

    def __iter__(self):
        return  CarIterator(self.car_list)

    def add(self, car):
        if type(car) == Car:
            self.car_list.append(car)
        else:
            print("Only cars are allowed in Garage")

    def delete(self, index):
        try:
            del self.car_list[int(index)]
        except  Exception as e:
            print("Invalid index")
