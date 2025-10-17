import csv

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def load_data(filename: str) -> list[list[str]]:
    extracted_data = []
    try:
        with open(filename, "r", encoding="utf-8-sig") as in_file:
            reader = csv.reader(in_file)
            next(reader)  # Skip the header row
            for row in reader:
                country = row[COUNTRY_INDEX]
                champion = row[CHAMPION_INDEX]
                extracted_data.append([country, champion])
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except IndexError:
        print(f"Error: Data in '{filename}' is not in the expected format (missing columns).")
        return []
    return extracted_data


def process_data(data: list[list[str]]) -> tuple[dict[str, int], set[str]]:
    champion_to_count = {}
    countries = set()

    for country, champion in data:
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
        countries.add(country)

    return champion_to_count, countries


def display_results(champion_to_count: dict[str, int], countries: set[str]):
    print("Wimbledon Champions:")
    for champion, count in sorted(champion_to_count.items()):
        print(f"{champion} {count}")

    sorted_countries = sorted(countries)
    countries_string = ", ".join(sorted_countries)

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(countries_string)


def main():
    print(f"Attempting to read data from {FILENAME}...")

    data = load_data(FILENAME)

    if not data:
        return
    champion_to_count, countries = process_data(data)
    display_results(champion_to_count, countries)

if __name__ == '__main__':
    main()

