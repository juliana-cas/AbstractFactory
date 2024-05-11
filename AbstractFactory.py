from abc import ABC, abstractmethod

# Abstract Factory
class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

# Concrete Factories
class MazdaFactory(CarFactory):
    def create_car(self, car_type):
        if car_type == "sedan":
            return MazdaSedan()
        elif car_type == "hatchback":
            return MazdaHatchback()
        elif car_type == "suv":
            return MazdaSUV()
        else:
            return None

class NissanFactory(CarFactory):
    def create_car(self, car_type):
        if car_type == "sedan":
            return NissanSedan()
        elif car_type == "hatchback":
            return NissanHatchback()
        elif car_type == "suv":
            return NissanSUV()
        else:
            return None

class RenaultFactory(CarFactory):
    def create_car(self, car_type):
        if car_type == "sedan":
            return RenaultSedan()
        elif car_type == "hatchback":
            return RenaultHatchback()
        elif car_type == "suv":
            return RenaultSUV()
        else:
            return None

# Abstract Products
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

# Concrete Products
class MazdaSedan(Car):
    def drive(self):
        return "Driving Mazda Sedan"

class MazdaHatchback(Car):
    def drive(self):
        return "Driving Mazda Hatchback"

class MazdaSUV(Car):
    def drive(self):
        return "Driving Mazda SUV"

class NissanSedan(Car):
    def drive(self):
        return "Driving Nissan Sedan"

class NissanHatchback(Car):
    def drive(self):
        return "Driving Nissan Hatchback"

class NissanSUV(Car):
    def drive(self):
        return "Driving Nissan SUV"

class RenaultSedan(Car):
    def drive(self):
        return "Driving Renault Sedan"

class RenaultHatchback(Car):
    def drive(self):
        return "Driving Renault Hatchback"

class RenaultSUV(Car):
    def drive(self):
        return "Driving Renault SUV"

# Client
def main():
    mazda_factory = MazdaFactory()
    nissan_factory = NissanFactory()
    renault_factory = RenaultFactory()

    for factory in [mazda_factory, nissan_factory, renault_factory]:
        print(f"Factory: {factory.__class__.__name__}")
        for car_type in ["sedan", "hatchback", "suv"]:
            car = factory.create_car(car_type)
            print(car.drive())

if __name__ == "__main__":
    main()