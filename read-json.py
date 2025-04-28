import requests
import json

#extract JSON text
r = requests.get("https://www.tranquiltestament.com/wp-json/")
res = r.json()
print(json.dumps(res, indent = 4))

#extract contents
q = res['name']
print(q)


