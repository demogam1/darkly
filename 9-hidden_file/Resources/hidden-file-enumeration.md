# Hidden File Enumeration

From a previous step, we discovered `robots.txt` using directory brute force.

That file referenced paths including `.hidden`, which contains many nested folders with `README` files.

Because there are thousands of `README` files, we used a Python scraper to recursively crawl directories and identify the file containing the flag pattern.

```bash
python3 script.py
```

## Vulnerability
Sensitive files were reachable in public hidden folders.

## Mitigation
Do not keep sensitive files in public paths, and protect access with authentication.