#!python3.8

import os
import requests

from config_reader import read_config

def main():
	dir_path = os.path.dirname(os.path.realpath(__file__))

	### read config ##########################################################

	config_file_path = os.path.join(dir_path, 'resources', 'config.yaml')
	config = read_config(config_file_path)
	server_address = config['server']['address']
	server_port = config['server']['port']
	server_cert_rel_path = config['server']['certfile']

	file_path = os.path.dirname(__file__)
	server_cert = os.path.join(file_path, server_cert_rel_path)

	### test login ###########################################################

	url = f'{server_address}:{server_port}/change_password'
	post_data = {
		'username':'test',
		'old_password':'password',
		'new_password':'new_password',
	}

	r = requests.post(url=url, json=post_data, verify=server_cert)
	data = r.json()
	print(data)

if __name__ == '__main__':
	main()
