"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()

main()

#How do you add a list?
#income = []

#We need a counter variable (int) for the month number. Remember that list indexes start at 0, but we want to print from 1.
#income = incomes[month - 1]

#How many loops will we need? What kind of loops?
#We need two loops and they both have to be for loops.

#We need a cumulative total to update as we loop through the list to display the incomes.
#total = 0 inside the first for loop and total += income for the second one