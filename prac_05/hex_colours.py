COLOUR_TO_HEX = {
    "ALICEBLUE": "#f0f8ff",
    "ANTIQUEWHITE": "#faebd7",
    "AZURE": "#f0ffff",
    "BEIGE": "#f5f5dc",
    "BLACK": "#000000",
    "BLUEVIOLET": "#8a2be2",
    "BROWN": "#a52a2a",
    "CORAL": "#ff7f50",
    "DARKGREEN": "#006400",
    "FIREBRICK": "#b22222",
}



def main():
    colour_name = input("Enter colour name: ").upper()

    while colour_name != "":
        if colour_name in COLOUR_TO_HEX:
            hex_code = COLOUR_TO_HEX[colour_name]
            print(f"The code for {colour_name.capitalize()} is {hex_code}")
        else:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").upper()

    print("Goodbye.")


if __name__ == "__main__":
    main()