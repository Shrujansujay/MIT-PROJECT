import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency.upper()}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Failed to retrieve exchange rates.")
    
    data = response.json()
    rates = data.get("rates", {})
    
    if target_currency.upper() not in rates:
        raise ValueError("Invalid target currency.")
    
    return rates[target_currency.upper()]

def convert_currency(amount, base_currency, target_currency):
    try:
        rate = get_exchange_rate(base_currency, target_currency)
        converted_amount = amount * rate
        return converted_amount
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    base = input("Enter base currency (e.g., USD): ")
    target = input("Enter target currency (e.g., EUR): ")
    amount = float(input("Enter amount: "))
    
    result = convert_currency(amount, base, target)
    
    if result is not None:
        print(f"{amount} {base.upper()} = {result:.2f} {target.upper()}")
