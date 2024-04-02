class Vehicle():

    def __init__(self, reg_num, type, owner):
        self.reg_num = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

    def view_all_vehicles(vehicles):
        print(f"Here is a list of all the vehicles in the registration system:")
        for vehicle in vehicles:
            print(f"Registration Number: {vehicle.reg_num}, Type: {vehicle.type}, Owner: {vehicle.owner}")

Honda = Vehicle(123, "coupe", "Daniel")
Toyota = Vehicle(456, "SUV", "Jim")
Ford = Vehicle(789, "truck", "Bob")
vehicles = [Honda, Toyota, Ford]

Vehicle.view_all_vehicles(vehicles)

Honda.update_owner("Beaumont")
Toyota.update_owner("Rachel")
Ford.update_owner("Zeus")

Vehicle.view_all_vehicles(vehicles)