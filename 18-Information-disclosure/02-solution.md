# Lab: Information disclosure on debug page
## Description
This lab contains a debug page that discloses sensitive information about the application. To solve the lab, obtain and submit the SECRET_KEY environment variable.

## Solution
Found `/cgi-bin` with directory listing enabled. The folder contained `/cgi-bin/phpinfo.php` that discloses the `SECRET_KEY` environment variable.
