import random

class Vehicle:
    def __init__(self, brand, model, tank_size, tank_quantity):
        self.brand = brand
        self.model = model
        self.tank_size = tank_size
        self.tank_quantity = tank_quantity     

    def quantity_of_petrol(self):
        print("Quantity of petrol is ", self.tank_quantity)

    def fill_the_tank(self):
        if self.tank_size > self.tank_quantity:
            self.tank_quantity = self.tank_size

    def add_petrol(self, petrol_added):
        if self.tank_size > self.tank_quantity and petrol_added + self.tank_quantity <= self.tank_size:
            self.tank_quantity += petrol_added
        else:
            print("\nQuantity asked was more than expected.")
            print(self.tank_size - self.tank_quantity, "lt added.\n")
            self.tank_quantity = self.tank_size

class Electrical(Vehicle):
    def charge(self, full_charge, charging_capacity):
        print("Charging",charging_capacity,"%\n")

        for charging_capacity in range(charging_capacity, full_charge):
            print("Charging",charging_capacity,"%")
            if full_charge >= charging_capacity:
                charging_capacity = charging_capacity + 1                

        print("Fully Charged: 100%\n")
            