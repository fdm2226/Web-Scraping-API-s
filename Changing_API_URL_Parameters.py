import requests
import json

bases = ["USD", "EUR", "GBP"]

for base in bases:

    #Extracts URL
    url = "https://api.exchangeratesapi.io/latest?base=" + base

    #converts url data into json
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)

    rates = parsed["rates"]

    print("--------------- Rates in", base, "---------------")
    for currency, rate in rates.iteritems():
        print(base, "=", currency, rate)
        
