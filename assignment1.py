class Vehicle:
    # Base class for all vehicles
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        # Display basic vehicle information
        return f"{self.year} {self.make} {self.model}"
    
    def start_engine(self):
        return "Engine started."
    
    def stop_engine(self):
        return "Engine stopped."


class Car(Vehicle):
    # subclass for cars
    def __init__(self, make, model, year, trunk_size):
        super().__init__(make, model, year)
        self.trunk_size = trunk_size  # In cubic feet
    
    def open_trunk(self):
        return f"Trunk opened. Capacity: {self.trunk_size} cubic feet."
    
    def start_engine(self):
        return f"The car's engine roars to life!"


class Bike(Vehicle):
    # Subclass for bikes
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type  # Example: "Mountain", "Road"
    
    def pedal(self):
        return f"You are pedaling the {self.bike_type.lower()} bike."
    
    def start_engine(self):
        return "Bikes don't have engines to start!"


# Example usage
car = Car("Toyota", "Camry", 2022, 15.1)
bike = Bike("Giant", "Defy", 2023, "Road")

print(car.display_info())        # Outputs: 2022 Toyota Camry
print(car.start_engine())        # Outputs: The car's engine roars to life!
print(car.open_trunk())          # Outputs: Trunk opened. Capacity: 15.1 cubic feet.

print(bike.display_info())       # Outputs: 2023 Giant Defy
print(bike.start_engine())       # Outputs: Bikes don't have engines to start!
print(bike.pedal())              # Outputs: You are pedaling the road bike.
