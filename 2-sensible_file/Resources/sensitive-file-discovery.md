# Sensitive File Discovery

We used directory brute-forcing to discover hidden resources:

```bash
dirb http://172.26.91.121
```

The scan revealed `http://172.26.91.121/whatever/`, which exposed an `htpasswd` file.

After cracking the MD5 hash, we recovered the credentials:

- Username: `root`
- Password: `qwerty123@`

Using these credentials on `http://172.26.91.121/admin` provided access to the flag.

## Vulnerability
An important file was public, and the password hash was easy to crack.

## Mitigation
Block access to internal files, disable directory listing, and use strong password hashing.