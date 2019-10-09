import requests
import json

base = raw_input("Convert from: ")
to = raw_input("Convert to: ")
amount = float(raw_input("Amount: "))

url = "https://api.exchangeratesapi.io/latest?base=" + base

response = requests.get(url)
data = response.text
parsed = json.loads(data)
rates = parsed["rates"]


for currency, rate in rates.items():
    if currency == to:
        conversion = rate * amount
        print("1", base, "=", currency, rate)
        print(amount, base, "=", currency, conversion)
