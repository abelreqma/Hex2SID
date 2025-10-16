
### **1. Query DB for Interactive Users/Groups**
```sql
SELECT r.name AS role,
  m.name AS name,
  m.type_desc AS descript,
  master.dbo.fn_varbintohexstr(m.sid) AS sid_hex
FROM sys.server_principals m
  LEFT JOIN sys.server_role_members rm
    ON m.principal_id = rm.member_principal_id
  LEFT JOIN sys.server_principals r
    ON rm.role_principal_id = r.principal_id
WHERE (m.name NOT LIKE '#%' AND m.name NOT LIKE 'NT %')
  AND (m.is_disabled != 1)
  AND (m.type_desc IN ('WINDOWS_GROUP','WINDOWS_LOGIN'))
```
#### **Sample Output:**
```sql
role       name                  descript        sid_hex                                                      
--------   -------------------   -------------   ----------------------------------------------------------   
sysadmin   DOMAIN\Group          WINDOWS_GROUP   0x0105000000000005150000005b7bb0f398aa2245ad4a1ca451040000   

NULL       DOMAIN\Domain Users   WINDOWS_GROUP   0x0105000000000005150000005b7bb0f398aa2245ad4a1ca401020000 
```

### **2. Convert Hex SID to ASCII**
```console
blkbrd@foo:~$ python3 hex2SID.py
Enter Hex String: 0x0105000000000005150000005b7bb0f398aa2245ad4a1ca451040000

Domain SID: S-1-5-21-4088429403-1159899800-2753317549
RID: 1105
```
