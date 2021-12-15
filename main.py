from my_first_car import Vehicle, Electrical
import random

def main(run):
    while run:
        brand = input("Brand: ")
        model = input("Model: ")

        selection = int(input("Choose 1 for Petrol car or 2 for Electrical car: "))

        if selection == 1:
            t_s = int(input("Tank Size: "))
            t_q = int(random.randrange(0, t_s))
            car = Vehicle(brand, model, t_s, t_q)

            print(car.brand, car.model)
            car.quantity_of_petrol()

            print("\nChoose 1 to fill the tank.")
            print("Choose 2 for adding the amount of fuel you want.\n")

            choice = int(input("Please insert your choice: "))

            if choice == 1:
                car.fill_the_tank()
            elif choice == 2:
                car.add_petrol(int(input("\nHow much fuel whould you like to add? lt:")))
            else:
                print("\n!! WARNING !! Incorrect input!\n")
                
            car.quantity_of_petrol()

        elif selection == 2:
            charging_capacity = int(random.randrange(20, 99))
            car = Electrical
            car.charge(None, 100, charging_capacity)

        else:
            print("!! WARNING !! Incorrect input!\n")

        print("Whould you like to continue?")
        option = int(input("If Yes,press 1.If No press 0: "))

        if option != 1:
            run = False

main(True)