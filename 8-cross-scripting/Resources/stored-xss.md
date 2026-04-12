# Stored XSS

The feedback page allows users to submit a name and a comment.

We tested stored cross-site scripting by injecting script tags in both fields.

Once the payload was processed and rendered by the application, the flag was revealed.

## Vulnerability
The app saved and displayed user text without cleaning it.

## Mitigation
Clean user input, escape output, and add a Content Security Policy (CSP).