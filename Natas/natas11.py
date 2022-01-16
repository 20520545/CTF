import requests
import json
import base64

url= 'http://natas11.natas.labs.overthewire.org/'

s= requests.Session()
s.auth= ('natas11', 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK')

def xor_encrypt(key, cookie):
    data = ""
    for i in range(len(key)):
        data += str(chr(cookie[i] ^ key[i % len(key)]))

    data = base64.encodebytes(data.encode('utf-8'))
    return data

def xor_decrypt(plaintext, ciphertext):
    secret= ""
    for i in range(len(plaintext)):
        secret += str(chr(ciphertext[i] ^ plaintext[i % len(plaintext)]))
    return secret

ciphertext = b"ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw="
ciphertext = base64.decodebytes(ciphertext)
plaintext = {"showpassword":"no", "bgcolor":"#ffffff"}
plaintext = json.dumps(plaintext).encode('utf-8').replace(b" ", b"")
key= xor_decrypt(ciphertext, plaintext)
key=key.encode("utf-8")
key = b"qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw"
new_cookie = {"showpassword":"yes", "bgcolor":"#ffffff"}
new_cookie = json.dumps(new_cookie).encode('utf-8').replace(b" ", b"")
data= xor_encrypt(key,new_cookie)
data= data.replace(b'\n', b'')
cookies= {'data':data.decode('utf-8')}

r= s.get(url+'/?bgcolor=#ffffff', cookies=cookies)
print(r.text)