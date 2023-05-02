#!python3.8

import json
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
	params = {
		'team_name': 'Test Team',
		'username': 'test',
		'team_role': 'all',
		'year': 2022,
		'week': 14,
		'receptions_multiplier': 1,
		'total_yards_multiplier': 1,
		'touchdowns_multiplier': 1,
		'turnovers_lost_mulitplier': 1,
		'sacks_multiplier': 1,
		'tackles_for_loss_multiplier': 1,
		'interceptions_multiplier': 1,
		'fumbles_recovered_multiplier': 1,
		'punting_yards_multiplier': 1,
		'fg_percentage_multiplier': 1,
	}

	r = requests.get(url=url, params=params, verify=server_cert)
	data = r.json()
	print(json.dumps(data, indent=4))

if __name__ == '__main__':
	main()
