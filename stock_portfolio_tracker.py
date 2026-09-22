# CodeAlpha - Stock Portfolio Tracker

# Manually defined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Please choose from the available stocks.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(f"{stock}: {quantity} × ${stock_prices[stock]} = ${investment}")
        print(f"Current total investment: ${total_investment}")

    except ValueError:
        print("Please enter a valid whole number for quantity.")

print("\n===== Portfolio Summary =====")
print(f"Total Investment Value: ${total_investment}")
print("Thank you for using Stock Portfolio Tracker!")
