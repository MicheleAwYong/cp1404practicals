BONUS_THRESHOLD = 1000
LOW_BONUS_RATE = 0.10
HIGH_BONUS_RATE = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < BONUS_THRESHOLD:
        bonus = sales * LOW_BONUS_RATE
    else:
        bonus = sales * HIGH_BONUS_RATE
    print(f"Bonus is: ${bonus:,.2f}")
    sales = float(input("Enter sales: $"))
print("Thank you for using the program. Goodbye!")