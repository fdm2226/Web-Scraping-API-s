import requests
import json

url = "http://data.fixer.io/api/latest?access_key=d3f8f36733b36b8655a89430e2c9bcfa&format=1"
response = requests.get(url)
data = response.text
parsed = json.loads(data)
date = parsed["date"]

gbp_rate = parsed["rates"]["GBP"]
usd_rate = parsed["rates"]["USD"]
print("On " + date + " EUR equals " + str(gbp_rate) + " GBP")
print("On " + date + " EUR equals " + str(usd_rate) + " USD")
