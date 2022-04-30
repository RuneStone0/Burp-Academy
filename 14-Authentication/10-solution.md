# Lab: 2FA bypass using a brute-force attack (Expert)
## Description

After investigating the auth flow for a while, it was clear the application is using CSRF-token that must be updated upon every POST request (attempt to guess the OTP). Further more, on invalid OTP attempts the user's session is invalidated. But because the OTP code is relatively easy to guess its not impossible to chain the full auth flow and perform a single OTP guess per session.

I ended up writing a [script](10-brute-force.py) to perform the the sequence authenticating to the application and trying one OTP code at a time..

## Solution
Run [script](10-brute-force.py) :-) 

