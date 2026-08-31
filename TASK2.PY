stocks = {
    "TCS": [2, 3000, 3200],
    "Infosys": [3, 1500, 1400],
    "Reliance": [2, 2500, 2700]
}

total_investment = 0
total_value = 0

for stock in stocks:
    quantity = stocks[stock][0]
    buy_price = stocks[stock][1]
    current_price = stocks[stock][2]

    investment = quantity * buy_price
    value = quantity * current_price
    profit_loss = value - investment

    print("\nStock:", stock)
    print("Investment:", investment)
    print("Current Value:", value)
    print("Profit/Loss:", profit_loss)

    total_investment += investment
    total_value += value

print("\nTotal Investment:", total_investment)
print("Total Current Value:", total_value)
print("Total Profit/Loss:", total_value - total_investment)