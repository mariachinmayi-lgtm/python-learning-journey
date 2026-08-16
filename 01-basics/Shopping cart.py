item = input("What item would you like to buy?")
price = float(input("Enter the price of the item"))
quantity = int(input("What is the quantity of items you would like to buy?"))
Cost = quantity * price
print(f"{Cost} is the cost of {quantity} {item}s")
