# Parameter Tampering

Using Burp Suite, we intercepted the request sent by the survey form.

We modified the body parameters (`value` and `subject`), then set `value` to a number greater than `10`.

The server accepted the tampered request and returned the flag.

## Vulnerability
The server trusted values sent by the browser.

## Mitigation
Check all limits and allowed fields on the server.
