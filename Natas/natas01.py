import requests 
import base64

info= (base64.b64encode(b'natas1::gtVrDuiDfck831PqWsLEZy5gyDz1clto')).decode("utf-8")[:-2]

url= "http://natas1.natas.labs.overthewire.org"
s= requests.Session()
s.auth = ('natas1', 'gtVrDuiDfck831PqWsLEZy5gyDz1clto')
r = s.get(url)

print(r.text)

