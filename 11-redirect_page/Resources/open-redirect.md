# Open Redirect

Social media links use a redirect endpoint like:

`href="index.php?page=redirect&site=instagram"`

By modifying the `site` parameter to another destination, we confirmed an open redirect and obtained the flag.

## Vulnerability
The site let users choose any redirect destination.

## Mitigation
Allow redirects only to a fixed list of trusted sites.