# Lab: Username enumeration via response timing
## Description
Goal: enumerate a valid username, brute-force this user's password, then access their account page.

I spent a ton of time failing during this lab... getting locked out. Writing useless python scripts attempting to bypass the lockout, until I looked at the lab hints and found that it could be bypassed with `X-Forwarded-For: 127.0.0.1`.

I spent some more time trying to make Burp Intruder randomize the `X-Forwarded-For` IP, until I found the Burp Extension [Random IP Address Header](https://portswigger.net/bappstore/3a656c1be14148c6bf95642af42eb854) that could do the job much much easier.

## Solution
1. Install [Random IP Address Header](https://portswigger.net/bappstore/3a656c1be14148c6bf95642af42eb854) and configure it to apply `X-Forwarded-For` using e.g. `127.0.0.0/16`
2. Enum usernames using Burp Intruder (`Simple` attack type) with the following payload:
```
POST /login HTTP/1.1
Host: ac901f741eac19e9c0874d0600a2006d.web-security-academy.net
Content-Length: 37

username=§carlos§&password=peterpeterpeterpeterpeter
```
3. Sort results by highest response time. You'll find a request with response time ~100ms higher, compared to the others. This is the valid username.
4. Take the identified username and use Burp Intruder to brute-force the passwords for that account.



