"""
CP1404/CP5632 Practical
Data file -> lists program
"""
FILENAME = "subject_data.txt"


def main():
    data = load_data(FILENAME)
    print(data)

def load_data(filename=FILENAME):
    all_subject_data = []

    with open(filename, "r") as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')

            try:
                parts[2] = int(parts[2])
            except ValueError:
                print(f"Error: Could not convert student number for line: {line}")
                continue

            all_subject_data.append(parts)

    return all_subject_data

main()