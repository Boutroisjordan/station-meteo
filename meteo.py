
from machine import Pin
from time import sleep
import dht
import urequests as requests
import json



sensor = dht.DHT11(Pin(0)) 

while True:
  try:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    data = {'temp': temp, 'hum': hum}
    r = requests.post("http://192.168.237.176:5001/datarecept", json = data)
    json_body= json.loads(r.text)
    print(json_body)
    print('Temperature: %3.1f C' %temp)
    print('Humidity: %3.1f %%' %hum)
    sleep(10)
  except OSError as e:
    print('Failed')
    