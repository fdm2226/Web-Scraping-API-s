import requests
import json

url = "https://api.exchangeratesapi.io/latest?symbols=USD,GBP"

response = requests.get(url)

data = response.text

parsed = json.loads(data)
print(json.dumps(parsed, indent=4))

date = parsed["date"]
print(date)

gbp_rate = parsed["rates"]["GBP"]

usd_rate = parsed["rates"]["USD"]

print("On " + date + " EUR equals " + str(gbp_rate) + " GBP")
print("On " + date + " EUR equals " + str(usd_rate) + " USD")
