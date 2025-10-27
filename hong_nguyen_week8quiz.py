class Car:
    """A class to represent a car with year model, make, and speed."""
    
    def __init__(self, year_model, make):
        """
        Constructor to initialize a Car object.
        
        Args:
            year_model (int): The car's year model
            make (str): The make of the car
        """
        self.yearModel = year_model
        self.make = make
        self.speed = 0
    
    # Accessor methods
    def get_year_model(self):
        """Returns the car's year model."""
        return self.yearModel
    
    def get_make(self):
        """Returns the car's make."""
        return self.make
    
    def get_speed(self):
        """Returns the car's current speed."""
        return self.speed
    
    def accelerate(self):
        """Increases the car's speed by 5."""
        self.speed += 5
    
    def brake(self):
        """Decreases the car's speed by 5."""
        self.speed -= 5


# Demonstration program
def main():
    # Create a Car object
    my_car = Car(2024, "Toyota")
    
    print(f"Car: {my_car.get_year_model()} {my_car.get_make()}")
    print(f"Initial speed: {my_car.get_speed()} mph\n")
    
    # Accelerate 5 times
    print("Accelerating...")
    for i in range(5):
        my_car.accelerate()
        print(f"Current speed: {my_car.get_speed()} mph")
    
    print()
    
    # Brake 5 times
    print("Braking...")
    for i in range(5):
        my_car.brake()
        print(f"Current speed: {my_car.get_speed()} mph")


if __name__ == "__main__":
    main()