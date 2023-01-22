import os
from datetime import datetime as dt

import psycopg
import yaml

from config_reader import read_config
from cfbd_helpers.cfbd_collector import CFBDCollector
from db_helper import publish_player_data

def main():
	dir_path = os.path.dirname(os.path.realpath(__file__))

	### read config ##########################################################

	config_file_path = os.path.join(dir_path, 'resources', 'config.yaml')
	config = read_config(config_file_path)
	db_name = config['database']['dbname']
	db_username = config['database']['username']
	db_password = config['database']['password']
	apikey = config['collegefootballstats']['apikey']

	### parameters for data collection #######################################

	year = 2022
	colleges = [
		(1,  'Baylor'),
		(2,  'Iowa State'),
		(3,  'Kansas'),
		(4,  'Kansas State'),
		(5,  'Oklahoma'),
		(6,  'Oklahoma State'),
		(7,  'TCU'),
		(8,  'Texas'),
		(9,  'Texas Tech'),
		(10, 'West Virginia'),
	]
	weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

	formatted_time_str = dt.now().strftime('%Y_%m_%d-T%H_%M_%S')
	data_logs_folder_path = os.path.join(dir_path, 'data_logs', formatted_time_str)
	log_file_name_fmt = 'big12-week-{week}.txt'

	### collect and publish data #############################################

	# ensure session data log folder exists
	if not os.path.exists(data_logs_folder_path):
		os.makedirs(data_logs_folder_path)

	# get data for each week, publish, and log
	for week in weeks:
		players_data = get_players_data(apikey, colleges, year, week)

		log_file_name = log_file_name_fmt.format(week=week)
		log_file_path = os.path.join(data_logs_folder_path, log_file_name)
		write_players_data(players_data, log_file_path)

		publish_players_data(db_name, db_username, db_password, players_data, week)

### helper functions #########################################################

def get_players_data(apikey, colleges, year, week):
	collector = CFBDCollector(apikey)
	players_data = collector.get_player_data(colleges, year, week, week)
	return players_data

def write_players_data(players_data, file_path):
	formatted_data = yaml.dump(players_data, default_flow_style=False)
	with open(file_path, 'w') as file:
		file.write(formatted_data)

def publish_players_data(db_name, db_username, db_password, players_data, week):
	with psycopg.connect(f'dbname={db_name} user={db_username} password={db_password}') as conn:
		with conn.pipeline():
			with conn.cursor() as cursor:
				for player_data in players_data.values():
					publish_player_data(cursor, player_data, week)
		conn.commit()  # commit changes after all data has been processed

if __name__ == '__main__':
	main()
