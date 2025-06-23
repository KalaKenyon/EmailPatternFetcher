import requests

API_KEY = "YOUR_API_KEY"
domain = "targetcompany.com"

url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={API_KEY}"
response = requests.get(url)

data = response.json()
pattern = data['data']['pattern']
print(f"Email format for {domain} appears to be: {pattern}")
