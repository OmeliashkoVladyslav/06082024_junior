class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"Brand: {self.brand}, Model: {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def info(self):
        return f"{super().info()}, Number of doors: {self.num_doors}"

class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type

    def info(self):
        return f"{super().info()}, Bike type: {self.bike_type}"

class Truck(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def info(self):
        return f"{super().info()}, Capacity: {self.capacity} tons"

car = Car("Mercedes-Benz", "G", 4)
bike = Bike("Trek", "X-Caliber", "Mountain")
truck = Truck("Volvo", "FMX", 12)

print(car.info())
print(bike.info())
print(truck.info())
