class Taxi:
    def __init__(self, name: str, fuel: float, price_per_km: float):
        self.name = name
        self.fuel = fuel
        self.price_per_km = price_per_km
        self.odometer = 0.0
        self.current_fare = 0.0

    def drive(self, distance: float):
        actual_distance = min(distance, self.fuel)

        self.odometer += actual_distance
        self.fuel -= actual_distance
        self.current_fare += actual_distance * self.price_per_km

        print(f"-> {self.name} drove {actual_distance:.2f} km.")
        if actual_distance < distance:
            print(f"   (Warning: Only drove {actual_distance:.2f} km due to low fuel.)")

        return actual_distance

    def start_fare(self):
        print("-> Meter reset: Starting a new fare.")
        self.current_fare = 0.0

    def __str__(self):
        return (f"{self.name}, fuel={self.fuel:.2f}, odometer={self.odometer:.2f} km, "
                f"price_per_km=${self.price_per_km:.2f}")

    def get_fare(self):
        return self.current_fare