import os

from config_reader import read_config

from server_helpers.web_server import TauHTTPServer
from server_helpers.db_server_helper import TauDBHelper

def main():
	dir_path = os.path.dirname(os.path.realpath(__file__))

	### read config ##########################################################

	config_file_path = os.path.join(dir_path, 'resources', 'config.yaml')
	config = read_config(config_file_path)
	db_name = config['database']['dbname']
	db_username = config['database']['username']
	db_password = config['database']['password']
	server_address = config['server']['address']
	server_port = config['server']['port']

	### web server ###########################################################

	db_helper = TauDBHelper(db_name, db_username, db_password)
	httpd = TauHTTPServer(server_address, int(server_port), db_helper)
	
	print(f'Starting httpd on port {server_port}...')
	httpd.serve_forever()

if __name__ == '__main__':
	main()
