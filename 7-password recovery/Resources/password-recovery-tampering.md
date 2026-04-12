# Password Recovery Tampering

We clicked the password recovery button and intercepted the POST request with Burp Suite.

Then we changed the destination email address to our own address.

This manipulation exposed the flag.

## Vulnerability
The recovery email came from the request and could be changed.

## Mitigation
Always use the email saved in the user account.