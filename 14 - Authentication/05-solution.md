# Lab: Broken brute-force protection, IP block
## Description

1. Used the Burp Repeater to evaluate the brute-force protection. After 3 invalid login attempts the source IP would be blocked for 1 minute.
2. To bypass the brute-force protection and reset the lockout timer, a valid authentication attempt must be made every 3 request.
3. WROTE THE PYTHON SCRIPT
4. Used the Burp Intruder, using a single thread with the following payload:
```
POST /login HTTP/1.1
Host: ace01f2d1ed4815ac08aa11f0041000f.web-security-academy.net
Content-Length: 30

username=§wiener§&password=peter
```
After evaluating the response times from all the requests, only 5 usernames had a response time higher than 270 seconds:
```
admin
appserver
arlington
mysql
al
```


## Solution

