# Lab: Broken brute-force protection, IP block
## Description
Goal: This lab is vulnerable due to a logic flaw in its password brute-force protection. To solve the lab, brute-force the victim's password, then log in and access their account page.

1. After 3 invalid login attempts, the source IP is blocked for 1 minute. To bypass this and reset the invalid login attempt counter on the server-side one can perform a valid auth request for ever 2 failed attempts like so:
```
invalid-login
invalid-login
successful-login
invalid-login
invalid-login
successful-login
...
```
2. There was no easy way to perform above actions easily with Burp Intruder. So I ended up writing a custom [python script](04-generate-payloads.py) to build the payload sets.
3. Use Burp Intruder in Simple attack mode using the generated [payloads](04-generated-payloads.lst).
```
POST /login HTTP/1.1
Host: ac6e1fdb1ecc8695c04767ae00a60087.web-security-academy.net
Content-Length: 30

§username=wiener&password=petera§
```

## Solution

See description

