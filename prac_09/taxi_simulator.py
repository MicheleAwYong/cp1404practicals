from taxi import Taxi

def main():
    print("--- 1. Creating Taxi Object ---")
    my_taxi = Taxi(name="Prius 1", fuel=100, price_per_km=1.23)
    print(my_taxi)
    print("-" * 30)

    print("--- 2. First Trip (40 km) ---")
    my_taxi.drive(40)
    print("-" * 30)

    print("--- 3. State After First Trip ---")
    print(my_taxi)
    print(f"Current Fare: ${my_taxi.get_fare():.2f}")
    print("-" * 30)

    print("--- 4. Reset Meter and Second Trip (100 km) ---")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print("-" * 30)

    print("--- 5. State After Second Trip ---")
    print(my_taxi)
    print(f"Current Fare: ${my_taxi.get_fare():.2f}")
    print("-" * 30)

if __name__ == "__main__":
    main()