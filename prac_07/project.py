class Project:

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date  # datetime.date object
        self.priority = priority  # integer
        self.cost_estimate = cost_estimate  # float
        self.completion_percentage = completion_percentage  # integer

    def __str__(self):
        date_string = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {date_string}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def is_completed(self):
        return self.completion_percentage == 100

    def to_csv_format(self):
        date_string = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}\t{date_string}\t{self.priority}\t"
                f"{self.cost_estimate}\t{self.completion_percentage}")