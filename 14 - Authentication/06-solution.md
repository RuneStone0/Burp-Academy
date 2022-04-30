# Lab: Username enumeration via account lock
## Description

1. Attempted to brute-force usernames, by simply running through the list. I noticed two requests had a slightly higher response time than others: `root` and `carlos`
2. I tried to brute force above users and failed. Repeating above returned different response times so timeing attacks seems not to be an issue here.
3. I tried to brute force all usernames against a small set of passwords (10) using Burp Intruder (Cluster Bomb). This triggered the following message to be returned from a single user: `You have made too many incorrect login attempts. Please try again in 1 minute(s).`. In retrospect, the password list could have been reduced to 4
4. Next step would be to brute force the password. One option would be to simply use Burp Intruder and brute force the username against the password list, while having a Resource Pool configured to a single thread with 1 min. delay between requests. It could potentially take up to 100 minutes because Burp Intruder doesn't have any easy way of firing x simultaneous requests and then wait x time before sending next batch.


## Solution
1. Enumerate the username. Use Burp Intruder (Cluster Bomb) using [usernames.lst](../usernames.lst) and a small passwords list such as: [111111,222222,333333,444444]
```
POST /login HTTP/1.1
Host: acac1f4d1ed59af7c0422e7800ea00f2.web-security-academy.net
Content-Length: 27

username=§usernames§&password=§passwords§
```
Sort results by HTTP response length to find responses with `You have made too many incorrect login attempts. Please try again in 1 minute(s).`

2. Brute force the password. Use Burp Intruder (Simple Attack Mode) with [passwords.lst](../passwords.lst) 
```
POST /login HTTP/1.1
Host: acac1f4d1ed59af7c0422e7800ea00f2.web-security-academy.net
Content-Length: 35

username=as&password=§testasdasd§
```