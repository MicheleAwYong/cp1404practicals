from prac_09.unreliable_car import unreliable_car


def main():
    good_car = unreliable_car("Mostly Good", 100, 90)
    bad_car = unreliable_car("Dodgy", 100, 9)

    # attempt to drive the cars many times
    # output what distance they drove
    for i in range(1, 12):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")

    # print the final states of the cars
    print(good_car)
    print(bad_car)