# CodeAlpha Task 2 - Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total = 0

print("📈 Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or type 'done'): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        quantity = int(input("Enter quantity: "))
        investment = stocks[stock] * quantity
        total += investment
        print(f"Investment for {stock}: ${investment}")
    else:
        print("❌ Stock not found!")

print("\n💰 Total Investment Value:", total)