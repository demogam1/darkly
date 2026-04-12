# File Upload Bypass

The upload page only expected image files (`jpg`, `jpeg`, `png`).

We uploaded a non-image payload and intercepted the request with Burp Suite.

By changing the header to `Content-Type: image/jpeg`, we bypassed the server-side file type check and obtained the flag.

## Vulnerability
The upload check trusted only the `Content-Type` header.

## Mitigation
Check the real file type on the server and store uploads outside the public folder.