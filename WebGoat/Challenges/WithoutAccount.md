# Without Account

Try to vote, we get response for login first before voting. Checking for Headers and Responses but nothing strange. So, change the request method to OPTIONS. We see that the request allow for 3 methods: `Allow: GET,HEAD,OPTIONS`. So, try with HEAD method and luckily, we get the flag.
