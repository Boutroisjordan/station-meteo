import urequests as requests
import json

data = """{
'temp': 18.5,
'hum': 70
}"""

#r = requests.post('https://httpbin.org/get', data=payload)
r = requests.post("http://172.20.10.13:5000/datarecept", data = data)
#print(payload)
json_body= json.loads(r.text)
print(json_body)