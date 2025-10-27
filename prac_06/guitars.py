CURRENT_YEAR = 2017
VINTAGE_AGE = 50

class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost


    def __str__(self):
        cost_formatted = f"${self.cost:,.2f}"
        return f"{self.name} ({self.year}) : {cost_formatted}"


    def get_age(self):
        return CURRENT_YEAR - self.year


    def is_vintage(self):
        return self.get_age() >= 50
