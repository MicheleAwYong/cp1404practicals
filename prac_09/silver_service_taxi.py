from taxi import Taxi


class SilverServiceTaxi(Taxi):
    FLAGFALL = 4.50

    def __init__(self, name: str, fuel: float, price_per_km: float, fanciness: float):
        super().__init__(name, fuel, price_per_km)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self) -> float:
        distance_cost = self.current_fare
        return distance_cost + self.FLAGFALL

    def __str__(self) -> str:
        return f"{super().__str__()} plus flagfall of ${self.FLAGFALL:.2f}"