#!/usr/bin/env python3
import requests

def log (file, message):
	with open(file + '.log', 'a') as currentLog:
		currentLog.write(message + '\n')

with open('urls.txt', 'r') as file:
	urls = file.read().splitlines()
	print('\n Checking URLs... \n')

for url in urls:
	try:
		if len(url) > 0:
			request = requests.get(url)
			status = request.status_code
			if status >= 200 and status < 300:
				log ('success', url)
			elif status >= 300 and status < 400:
				log ('redirect', url)
			elif status >= 400 and status < 500:
				log ('error-client', url)
			elif status >= 500:
				log ('error-server', url)
	except requests.exceptions.RequestException as ex:
		log('error-request', url + ' >> ' + str(ex))


print('\n Check complete \n')
