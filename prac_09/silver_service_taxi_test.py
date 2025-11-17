from silver_service_taxi import SilverServiceTaxi


def main():
    BASE_PRICE = 1.23

    print("--- 1. Testing __str__ and Initial State ---")
    hummer = SilverServiceTaxi(
        name="Hummer",
        fuel=200,
        price_per_km=BASE_PRICE,
        fanciness=4.0
    )
    print(hummer)
    print(f"Expected price/km: ${BASE_PRICE * 4.0:.2f}")  # Should be 4.92
    print("-" * 40)
    print("--- 2. Testing Specific Fare Calculation (18 km, Fanciness 2) ---")


    test_taxi = SilverServiceTaxi(
        name="Fancy Sedan",
        fuel=100,
        price_per_km=BASE_PRICE,
        fanciness=2.0
    )

    distance_driven = test_taxi.drive(18)
    fare = test_taxi.get_fare()
    EXPECTED_FARE = 48.78

    print(f"Distance driven: {distance_driven:.2f} km")
    print(f"Calculated Fare: ${fare:.2f}")
    print(f"Expected Fare: ${EXPECTED_FARE:.2f}")

    assert fare == EXPECTED_FARE, f"Fare mismatch: Expected {EXPECTED_FARE}, got {fare}"
    print("\nASSERTION PASSED: The fare calculation is correct ($48.78).")

    print("-" * 40)

    print("--- 3. Testing Short Trip (1 km, Fanciness 3) ---")
    short_trip_taxi = SilverServiceTaxi(
        name="Quick Commuter",
        fuel=10,
        price_per_km=BASE_PRICE,
        fanciness=3.0
    )
    short_trip_taxi.drive(1)
    print(f"Total Fare for 1 km: ${short_trip_taxi.get_fare():.2f}")
    assert short_trip_taxi.get_fare() == 8.19, "Short trip fare calculation failed."


if __name__ == "__main__":
    main()