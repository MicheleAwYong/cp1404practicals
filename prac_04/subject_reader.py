"""
CP1404/CP5632 Practical
Data file -> lists program
"""
FILENAME = "subject_data.txt"

def main():
    subject_lists = get_subject_lists(FILENAME)
    display_subject_details(subject_lists)

def get_subject_lists(filename=FILENAME):
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


def display_subject_details(subject_lists):
    print("\n--- Subject Details ---")
    for subject in subject_lists:
        subject_code = subject[0]
        lecturer_name = subject[1]
        num_students = subject[2]

        print(f"{subject_code} is taught by {lecturer_name:<15} and has {num_students:>3} students")


main()