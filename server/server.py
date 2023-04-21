#!python3.8

import os
import ssl

from common.config_reader import read_config

from server_helpers.web_server import TauHTTPServer
from server_helpers.db_helper import TauDBHelper

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
	server_cert_rel_path = config['server']['certfile']
	server_key_rel_path = config['server']['keyfile']
	server_password = config['server']['cert_password']

	file_path = os.path.dirname(__file__)
	server_cert = os.path.join(file_path, server_cert_rel_path)
	server_key = os.path.join(file_path, server_key_rel_path)

	### web server ###########################################################

	ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
	ssl_context.load_cert_chain(server_cert, server_key, server_password)

	db_helper = TauDBHelper(db_name, db_username, db_password)
	httpd = TauHTTPServer(server_address, int(server_port), db_helper)
	httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

	print(f'Starting httpd on port {server_port}...')
	httpd.serve_forever()

if __name__ == '__main__':
	main()
