import requests
import json
url = 'http://localhost:80'
myobj = json.dumps({"test": "test"})

x = requests.post(url, data = myobj)

print(x.text)