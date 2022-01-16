import requests
import binascii
import base64 

url= "http://natas8.natas.labs.overthewire.org"

s= requests.Session()
s.auth=('natas8','DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe')
r= s.get(url+'/index-source.html')
string= '3d3d516343746d4d6d6c315669563362'

#Get the string from encodedSecret and the function given
secret= base64.b64decode(binascii.unhexlify(string)[::-1]).decode("utf-8")
#
headers= {'Content-Type': 'application/x-www-form-urlencoded'}
r= s.post(url, headers= headers, data=f'secret={secret}&submit=Submit')
print(secret)
print(r.text)
