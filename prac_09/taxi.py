"""
CP1404/CP5632 Practical
Car class
"""
from prac_09.car import Car


class Taxi(Car):

    def __init__(self, name, fuel, price_per_km):
        super().__init__(name, fuel)
        self.price_per_km = price_per_km
        self.current_fare_distance = 0

    def __str__(self):
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        self.current_fare_distance = 0

    def drive(self, distance):
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven