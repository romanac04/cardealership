class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False

    def search_engine(self):
        print("Starting engine..")
        self.engine_on = True

    def make_noise(self):
        print("Beep beep!")


class Truck(Vehicle):
    def __init__(self, make, miles, price):
        super().__init__(make, miles, price)
        self.cargo_property = False

    def load_cargo(self):
        print("Loading the truck bed...")
        self.cargo_property = True


class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        super().__init__(make, miles, price)
        self.top_speed = top_speed

    def make_noise(self):
        print("Vroom! Vroom!")


bike1 = Motorcycle("Aprilia", 0, 300, 50000)
bike2 = Motorcycle('Ducati', 1000, 250, 50000)
bike3 = Motorcycle('Honda', 20000, 240, 50000)

truck1 = Truck("Chevy", 10000, 30000)
truck2 = Truck("Ram", 200000, 5000)
truck3 = Truck("Ford", 50000, 20000)
bikes = [bike1, bike2, bike3]
trucks = [truck1, truck2, truck3]
vehicles_to_compare = []
while True:
    options = input("Would you like to view bikes or trucks? b or t ")
    if options == 'b':
        vehicles = bikes
        print(f"{1}.{bike1.make} with {bike1.miles} miles and top speed of {bike1.top_speed} costs {bike1.price}")
        print(f"{2}.{bike2.make} with {bike2.miles} miles and top speed of {bike2.top_speed} costs {bike2.price}")
        print(f"{3}.{bike3.make} with {bike3.miles} miles and top speed of {bike3.top_speed} costs {bike3.price}")

    elif options == 't':
        vehicles = trucks
        print(f"{1}. {truck1.make} with {truck1.miles}  miles costs {truck1.price}.")
        print(f"{2}. {truck2.make} with {truck2.miles} miles costs {truck2.price}.")
        print(f"{3}. {truck3.make} with {truck3.miles} miles costs {truck3.price}.")

    else:
        print("invalid option.")
    while True:
        compare = input("Would you like to compare one of the vehicles today?y or n ")
        if compare == "y":
            choice = int(input("Which vehicle would you like to compare? please list a number "))
            if options == 'b':
                selected_bike = bikes[choice - 1]
                selected_vehicle = Motorcycle(selected_bike.make, selected_bike.miles, selected_bike.top_speed, selected_bike.price)
                print(f" {selected_bike.make} bike added.")
                vehicles_to_compare.append(selected_vehicle)
            elif options == 't':
                selected_truck = trucks[choice - 1]
                selected_vehicle = Truck(selected_truck.make, selected_truck.miles, selected_truck.price)
                print(f" {selected_truck.make} truck added.")
                vehicles_to_compare.append(selected_vehicle)
        elif compare == "n":
            break
    while True:
        question = input("Would you like to compare vehicles now? y or n ")
        if question == "y":
            print("Here are your vehicles to compare:")
            for vehicle in vehicles_to_compare:
                vehicle.make_noise()
                print(f"{vehicle.make} ({vehicle.miles} miles, ${vehicle.price})")
        break
        if question == "n":
            print("Thank you and goodbye!")
    break
