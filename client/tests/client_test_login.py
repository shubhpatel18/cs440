import os
import requests

#!python3.8

from common.config_reader import read_config

def main():
	tests_path = os.path.dirname(os.path.realpath(__file__))
	client_path = os.path.join(tests_path, os.path.pardir)

	### read config ##########################################################

	config_file_path = os.path.join(client_path, 'resources', 'config.yaml')
	config = read_config(config_file_path)
	server_address = config['server']['address']
	server_port = config['server']['port']
	server_cert_rel_path = config['server']['certfile']

	file_path = os.path.dirname(__file__)
	server_cert = os.path.join(file_path, server_cert_rel_path)

	### test login ###########################################################

	url = f'{server_address}:{server_port}/login'
	params = {
		'username':'test',
		'password':'password',
	}

	r = requests.get(url=url, params=params, verify=server_cert)
	data = r.json()
	print(data)

if __name__ == '__main__':
	main()
