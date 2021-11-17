import requests 
import base64


info= base64.b64encode(b'natas0:natas0').decode("utf-8")

url= "http://natas0.natas.labs.overthewire.org"
s= requests.Session()
r= requests.get(url, headers= {
    'Authorization': f'Basic {info}'
})
print(r.text)
#Or just auth with credential natas0:natas0 and view-source
