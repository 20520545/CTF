# Client Side

## Bypass front-end restrictions

### Field Restrictions

Just modify the parameters in the request different than the sample parameters in the form.
`select=string&radio=string&checkbox=string&shortInput=stringstrin&readOnlyInput=string`

### Validation

Send the previous answer, intercept the request and modify it for not fitting the regex pattern.
`field1=abcd&field2=1231&field3=abc+123+ABC+$$$&field4=onesss&field5=01101555&field6=90210-1111123213&field7=301-604-4881231232&error=0`

## Client side filtering

### Salary manager

Find in the client's source with `Neville` and get the information about the Neville's salary.

### ShopEndpoint

Get the `/WebGoat/lesson_js/clientSideFilteringFree.js` endpoint at the client's source, we can see some strang endpoint to check: `clientSideFiltering/challenge-store/coupons/`. Visit it and we can get the coupon discount.

```text
{
  "codes" : [ {
    "code" : "webgoat",
    "discount" : 25
  }, {
    "code" : "owasp",
    "discount" : 25
  }, {
    "code" : "owasp-webgoat",
    "discount" : 50
  }, {
    "code" : "get_it_for_free",
    "discount" : 100
  } ]
}
```

## HTML tampering

Intercept the request, reduce the cost and sent it again.
`QTY=1&Total=0`
