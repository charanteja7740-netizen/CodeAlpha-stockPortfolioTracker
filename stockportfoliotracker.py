stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190,
    "MSFT": 420
}

total_investment = 0

while True:
    stock_name = input("Enter stock name: ").upper()

    if stock_name not in stock_prices:
        print("Stock not available. Please choose from the available stocks.")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock_name] * quantity
    total_investment += investment

    print("Investment value:", investment)

    another = input("Do you want to add another stock? (yes/no): ").lower()

    if another != "yes":
        break

print("Total investment:", total_investment)

with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Report\n")
    file.write("----------------------\n")
    file.write(f"Total Investment: {total_investment}\n")

print("Portfolio saved to portfolio.txt")