# XSS

## Try It! Reflected XSS

`<script>alert(1)</script>` into credit card number box.

## Identify potential for DOM-Based XSS

Checking GoatRoute.js in client side code, we can see that `'test/:param': 'testRoute'`.
So, `start.mvc#test/` is the answer.

## Try It! DOM-Based XSS

Filter contain `/` to block `</script>` but we still can execute the function without close the tag:
`http://127.0.0.1:8080/WebGoat/start.mvc#test/<script>webgoat.customjs.phoneHome()` and get the information in the console.
