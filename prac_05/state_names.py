STATE_CODES_TO_NAMES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia",
}
print(STATE_CODES_TO_NAMES)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in STATE_CODES_TO_NAMES:
        print(f"{state_code} is {STATE_CODES_TO_NAMES[state_code]}")
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()