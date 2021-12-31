# Broken Access Control

## IDOR

### Authenticate First, Abuse Authorization Later

Login with given credentials.

### Guessing & Predicting Patterns

WebGoat/IDOR/profile/2342384

### Playing with the Patterns

Edit Another Profile:

Get userID by brute force to find appropriate one.

```text
PUT http://localhost:8080/WebGoat/IDOR/profile/2342388 HTTP/1.1
Host: vernjan:8080
Content-Type: application/json
Content-Length: 77
Cookie: JSESSIONID=DTDJnkBwts-f_6uXV8AJ0iTSvX8zolnBkQR0xLuF

{"role":1, "color":"red", "size":"small", "name":"Tom Cat", "userId":2342388}
```

## Missing Function Level Access Control

### Relying on Obscurity

Inspect the website, we can see that `Users` and `Config` have been hidden.

### Just Try It

With the description of using hidden menu items and GET methods, we can try to modify the URL of the website. Found A Whitelable Error Page with 500 Response at `/WebGoat/users`. Add "Content-Type: application/json" header to the request to get the hash.
