import requests
import json

#extract JSON text
#r = requests.get("https://www.tranquiltestament.com/wp-json/")
r = requests.get("https://www.abcmoney.co.uk/wp-json/")
res = r.json()
print(json.dumps(res, indent = 4))

#extract contents
q = res['name']
print(q)
#keep window open & closes only if user press enter button
input("\nPress Enter to exit...")


