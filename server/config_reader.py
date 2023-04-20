#!python3.8

import yaml

def read_config(file_path):
	with open(file_path, 'r') as config_file:
		try:
			config = yaml.safe_load(config_file)
		except yaml.YAMLError as e:
			print(e)

	return config
