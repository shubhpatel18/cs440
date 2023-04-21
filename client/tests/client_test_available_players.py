#!python3.8

import os
import requests

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

	server_cert = os.path.join(client_path, server_cert_rel_path)

	### test login ###########################################################

	url = f'{server_address}:{server_port}/available_players'
	post_data = {
		'team_name': 'Test Team',
		'year': 2022,
		'week': 5
	}

	r = requests.post(url=url, json=post_data, verify=server_cert)
	data = r.json()
	print(data)

if __name__ == '__main__':
	main()
