Number_of_Items = int(input("Number of items: "))
while Number_of_Items < 0:
    print("Invalid number of items!")
    Number_of_Items = int(input("Number of items: "))
total_price = 0
for i in range(Number_of_Items):
    price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    discount = total_price * 0.10
    total_price -= discount
print(f"Total price for {Number_of_Items} items is ${total_price:,.2f}")