# Crypto Basics

## Solution for Lesson 6


### Get private key and save as private.key

Something like this:
```
-----BEGIN PRIVATE KEY-----
...
-----END PRIVATE KEY-----
```
### Get RSA nodulus and save as modulus.txt
```
openssl rsa -in private.key -modulus -noout
```
Ps: In modulus.txt, just get the modulus value.

### Sign RSA modulus and encode with base64
```
openssl dgst -sha256 -sign private.key modulus.txt | base64 --wrap=0 > sign.sha256.base64
```

