class Car:
    def __init__(self, release_year: int, producer: str, brand: str,
                 fuel_mileage: float):
        self.year = release_year
        self.producer = producer
        self.brand = brand
        self.way = 0
        self.fuel = fuel_mileage
    def drive(self):
        print("Я авто марки", self.brand, "їду по справам господаря")
    @property
    def cost_of_service(self):
        return self.way * 7.6

car1 = Car(2011, 'Volkswagen Group', 'Audi', 10.5)
car2 = Car(2018, 'Honda', 'Civic', 8.2)
car3 = Car(2004, 'Mercedes-Benz', 'Mercedes', 12.4)

car1.way = 120
print('Cost of service car1 -', car1.cost_of_service)
car3.drive()
