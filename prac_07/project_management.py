from prac_07 import project
from datetime import datetime

DEFAULT_FILENAME = "projects.txt"
DATE_FORMAT = "%d/%m/%Y"
MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit")


def main():
    print("Welcome to Project Management Program")

    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").upper()

        if choice == "L":
            filename = input("Enter filename to load from (e.g., projects.txt): ")
            new_projects = load_projects(filename)
            projects.extend(new_projects)
            print(f"Loaded {len(new_projects)} projects from {filename}.")

        elif choice == "S":
            filename = input("Enter filename to save to (e.g., projects.txt): ")
            save_projects(projects, filename)
            print(f"Saved {len(projects)} projects to {filename}.")

        elif choice == "D":
            display_projects(projects)

        elif choice == "F":
            filter_projects_by_date(projects)

        elif choice == "A":
            add_new_project(projects)

        elif choice == "U":
            update_project(projects)

        elif choice == "Q":
            print("Thank you for using Project Management.")
            if input(f"Would you like to save current projects to {DEFAULT_FILENAME}? (y/n): ").upper() == "Y":
                save_projects(projects, DEFAULT_FILENAME)
                print(f"Projects saved to {DEFAULT_FILENAME}.")

        else:
            print("Invalid menu choice.")

    print("Goodbye.")


def load_projects(filename):
    projects = []
    try:
        with open(filename, 'r', encoding='utf-8') as in_file:
            in_file.readline()
            for line in in_file:
                parts = line.strip().split('\t')
                if len(parts) == 5:
                    try:
                        name = parts[0]
                        date = datetime.strptime(parts[1], DATE_FORMAT).date()
                        priority = int(parts[2])
                        cost = float(parts[3])
                        completion = int(parts[4])

                        projects.append(project(name, date, priority, cost, completion))
                    except ValueError as e:
                        print(f"Skipping line due to data error: {e}")
                else:
                    print(f"Skipping line due to incorrect format: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    return projects


def save_projects(projects, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as out_file:
            out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
            for project in projects:
                out_file.write(f"{project.to_csv_format()}\n")
    except Exception as e:
        print(f"Error saving file: {e}")


def display_projects(projects):
    if not projects:
        print("No projects to display.")
        return

    projects.sort()

    incomplete_projects = [p for p in projects if not p.is_completed()]
    completed_projects = [p for p in projects if p.is_completed()]

    print("\nIncomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in completed_projects:
        print(f"  {project}")


def get_valid_date(prompt):
    is_valid_date = False
    date_string = ""
    while not is_valid_date:
        date_string = input(prompt)
        try:
            date = datetime.strptime(date_string, DATE_FORMAT).date()
            is_valid_date = True
        except ValueError:
            print("Invalid date format. Please use DD/MM/YYYY.")
    return date


def filter_projects_by_date(projects):
    if not projects:
        print("No projects to filter.")
        return

    print("\nFilter projects by start date:")
    filter_date = get_valid_date("Show projects that start after date (DD/MM/YYYY): ")
    filtered_projects = [p for p in projects if p.start_date > filter_date]

    if not filtered_projects:
        print(f"No projects found starting after {filter_date.strftime(DATE_FORMAT)}")
        return

    filtered_projects.sort(key=lambda p: p.start_date)

    print(f"\nProjects starting after {filter_date.strftime(DATE_FORMAT)} (sorted by date):")
    for project in filtered_projects:
        print(f"  {project}")


def get_valid_int(prompt, minimum=0, maximum=100, can_be_blank=False, current_value=None):
    while True:
        raw_input = input(prompt)

        if can_be_blank and raw_input == "":
            return current_value

        try:
            value = int(raw_input)
            if minimum <= value <= maximum:
                return value
            else:
                print(f"Input must be between {minimum} and {maximum}.")
        except ValueError:
            print("Invalid input. Must be an integer.")


def add_new_project(projects):
    print("\n--- Add New Project ---")
    name = input("Name: ")
    start_date = get_valid_date("Start date (DD/MM/YYYY): ")
    priority = get_valid_int("Priority (1-10): ", minimum=1, maximum=10, can_be_blank=False)
    cost = get_valid_float("Cost estimate: $")
    completion = get_valid_int("Percent complete: ", minimum=0, maximum=100, can_be_blank=False)

    new_project = project(name, start_date, priority, cost, completion)
    projects.append(new_project)
    print(f"Project '{name}' added.")


def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Must be a number.")


def update_project(projects):
    if not projects:
        print("No projects to update.")
        return

    print("\n--- Update Project ---")
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    index = get_valid_int(f"Project choice: ", minimum=0, maximum=len(projects) - 1, can_be_blank=False)
    project_to_update = projects[index]

    print(f"Updating: {project_to_update}")

    new_completion_percent = get_valid_int(
        f"New Percentage (leave blank to retain {project_to_update.completion_percentage}%): ",
        minimum=0, maximum=100, can_be_blank=True, current_value=project_to_update.completion_percentage)

    new_priority = get_valid_int(
        f"New Priority (leave blank to retain {project_to_update.priority}): ",
        minimum=1, maximum=10, can_be_blank=True, current_value=project_to_update.priority)

    project_to_update.completion_percentage = new_completion_percent
    project_to_update.priority = new_priority

    print(f"Project updated: {project_to_update}")


if __name__ == "__main__":
    main()