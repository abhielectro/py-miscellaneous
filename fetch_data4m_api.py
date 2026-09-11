import requests, json

url = input("API URL: ")
r = requests.get(url, timeout=5)
data = r.json() if r.status_code == 200 else {}
print(json.dumps(data, indent=2)[:500])
