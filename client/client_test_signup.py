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

	### test login ###########################################################

	url = f'http://{server_address}:{server_port}/signup'
	post_data = {
		'username':'test',
		'password':'password',
	}

	r = requests.post(url=url, json=post_data)
	data = r.json()
	print(data)

if __name__ == '__main__':
	main()
