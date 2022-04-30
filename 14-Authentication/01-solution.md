# Lab: Username enumeration via different responses
## Description
**Goal: Enumerate a valid username, brute-force this user's password, then access their account page**

1. Attempted to authenticate with username/password such as `AAAA/BBBB`. This returned returned `Invalid username`
2. Attempted to authenticate with `administrator/BBBB` returned this also returned `Invalid username`
3. To speed up the brute-force attack process, I sent the auth request to the Burp Intruder and enumerated through all the [username list](../usernames.lst). Once completed I sorted the results by HTTP Response Length to identify responses that was different from the default `Invalid username` response length. In our case, the username was identified to be `apps`
4. Then I repeated the same attack pattern as above, but instead used `apps` as the username and enumerate through the [password list ](../passwords.lst). The password was then identified to be `123456`

## Solution
```
Username: apps
Password: 123456
```
