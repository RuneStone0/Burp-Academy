# Lab: Username enumeration via subtly different responses
## Description
**Goal: enumerate a valid username, brute-force this user's password, then access their account page.**

1. Similarly to previous Lab, I took the auth request. Sent it to Burp Intruder and enumerated through the [username list](../usernames.lst) while setting the password to `BBBB` (which later proved to be a big mistake) and analyzed the HTTP response length. The username `auto` had a slightly different response length, indicating that it might be a valid username.
2. Repeated the same attack as above, but using the username `auto` and enumerated through the [passwords list](../passwords.lst).
3. Above didn't really work, so I had to go back to enumerating usernames...
4. Enumerating the usernames again using Burp Intruder, I extracted all usernames where the following `<!-- -->` HTML comment was embedded in the HTTP responses, indicating valid usernames. This resulted in a list of +50 usernames, which seemed off.
5. Then, I noticed that `<!-- -->` was added to the responses depending on the username and password input. For example:

```
AAAA		Returned no HTML comment
aaaa		Returned a HTML <!-- --> comment
```
This could indicate that when `<!-- -->` is returned, the auth request either passed or failed some initial validation checks.

After spending some time trying to extract all username and passwords where `<!-- -->` was returned and then running them through a Burp Intruder (Cluster Bomb) brute-force attack without getting any sensible results I started all over again.. I must have missed something....

6. I started to enum usernames again - and by pure luck I attempted to filter all Intruder results after `Invalid username or password.` and noticed that other requests returned `Invalid username or password` (missing the period sign). I must have missed this very subtle difference when reviewing various HTTP responses using the Burp Comparer. I could finally enum usernames! The valid usernames returned `Invalid username or password`  (without period).

7. To find the valid password I used Burp Intruder, brute-forcing the username `adm` against the password list and identified the correct password looking for a response code `302 Found`


## Solution
```
Username: adm
Password: princess
```