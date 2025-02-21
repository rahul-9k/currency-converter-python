def currency_converter():
    exchange_rates = {
        "USD": 1.0,
        "EUR": 0.89,  # 1 USD = 0.89 EUR
        "GBP": 0.76,  # 1 USD = 0.76 GBP
        "JPY": 150.32,  # 1 USD = 150.32 JPY
        "INR": 82.85   # 1 USD = 82.85 INR
    }

    print("Welcome to the Currency Converter!")
    print("Available currencies:", ", ".join(exchange_rates.keys()))

    while True:
        try:
            amount = float(input("\nEnter the amount to convert: "))
            if amount < 0:
                print("Amount cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    from_currency = input("Enter the source currency (e.g., USD): ").upper()
    to_currency = input("Enter the target currency (e.g., EUR): ").upper()

    # Validate currencies
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Error: One or both currencies are not supported.")
        return

    # Convert amount: First to USD, then to target currency
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]

    # Display result
    print(f"\n{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    currency_converter()
    