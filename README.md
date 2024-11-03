# Burp Academy Solutions
My solutions for the Burp Academy labs.

* 🟡 01 - SQL injection
* 🟡 02 - Cross-site scripting
* 🟡 03 - Cross-site request forgery (CSRF)
* 🟡 04 - Clickjacking
* 🔴 05 - DOM-based vulnerabilities
* 🟡 06 - Cross-origin resource sharing (CORS)
* 🟢 07 - XML external entity (XXE) injection
* 🔴 08 - Server-side request forgery (SSRF)
* 🔴 09 - HTTP request smuggling
* 🟡 10 - OS command injection
* 🔴 11 - Server-side template injection
* 🟡 12 - Directory traversal
* 🟡 13 - Access control vulnerabilities
* 🟢 14 - Authentication
* 🔴 15 - WebSockets
* 🔴 16 - Web cache poisoning
* 🔴 17 - Insecure deserialization
* 🟡 18 - Information disclosure
* 🟡 19 - Business logic vulnerabilities
* 🔴 20 - HTTP Host header attacks
* 🔴 21 - OAuth authentication
* 🔴 22 - File upload vulnerabilities
* 🔴 23 - JWT
* 🔴 24 - Essential skills
* 🔴 25 - Prototype pollution
* 🔴 26 - GraphQL API vulnerabilities
* 🔴 27 - Race conditions
* 🔴 28 - NoSQL injection

Above list is based on [deepfryd.com](https://www.deepfryd.com/burp-academy-apprentice/)


# Feedback to PortSwigger
* Add unique IDs for each lab, so its easier to reference a specific lab. Currently, the only unique identifier is the lab title (e.g. `Blind SQL injection with time delays`)
* Add NoSQL Labs
* SQL injection attack, querying the database type and version on MySQL and Microsoft  will not get solved using this `'+UNION+SELECT+@@version,NULL%23asdasd`
* The lab `Blind SQL injection with time delays` works for all 4 DBMS types which is somewhat unrealistic. Perhaps it should just work with one?
* When viewing a lab from the built-in chrome browser the page doesn't load properly.
* Add Open Redirect labs
