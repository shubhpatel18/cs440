#!python3.8

import os
from datetime import datetime as dt

import psycopg
import yaml

from common.config_reader import read_config
from helpers.cfbd_collector import CFBDCollector
from helpers.db_helper import publish_player_data, publish_college_data

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
	conference = 'B12'
	colleges = {
		'Baylor': 1,
		'Iowa State': 2,
		'Kansas': 3,
		'Kansas State': 4,
		'Oklahoma': 5,
		'Oklahoma State': 6,
		'TCU': 7,
		'Texas': 8,
		'Texas Tech': 9,
		'West Virginia': 10,
	}
	college_names = ', '.join(colleges.keys())
	weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

	formatted_time_str = dt.now().strftime('%Y_%m_%d-T%H_%M_%S')
	data_logs_folder_path = os.path.join(dir_path, 'data_logs', formatted_time_str)
	players_log_file_name_fmt = 'big12-players-week-{week}.txt'
	colleges_log_file_name_fmt = 'big12-colleges-year-{year}.txt'

	### collect and publish data #############################################

	# ensure session data log folder exists
	if not os.path.exists(data_logs_folder_path):
		os.makedirs(data_logs_folder_path)

	# get college data
	print(f'Collecting {year} team record data for {college_names}')
	colleges_data = get_conference_data(apikey, year, conference, colleges)

	print(f'Publishing {year} team record data for {college_names}')
	colleges_log_file_name = colleges_log_file_name_fmt.format(year=year)
	colleges_log_file_path = os.path.join(data_logs_folder_path, colleges_log_file_name)
	write_colleges_data(colleges_data, colleges_log_file_path)
	publish_colleges_data(db_name, db_username, db_password, colleges_data)

	# get data for each week, publish, and log
	for week in weeks:
		print(f'Collecting {year} week {week} player data for {college_names}')
		players_data = get_players_data(apikey, colleges, year, week)

		print(f'Publishing {year} week {week} player data for {college_names}')
		players_log_file_name = players_log_file_name_fmt.format(week=week)
		players_log_file_path = os.path.join(data_logs_folder_path, players_log_file_name)
		write_players_data(players_data, players_log_file_path)
		publish_players_data(db_name, db_username, db_password, players_data, year, week)

### helper functions #########################################################

def get_players_data(apikey, colleges, year, week):
	collector = CFBDCollector(apikey)
	players_data = collector.get_player_data(colleges, year, week, week)
	return players_data

def write_players_data(players_data, file_path):
	formatted_data = yaml.dump(players_data, default_flow_style=False)
	with open(file_path, 'w') as file:
		file.write(formatted_data)

def publish_players_data(db_name, db_username, db_password, players_data, year, week):
	with psycopg.connect(f'dbname={db_name} user={db_username} password={db_password}') as conn:
		with conn.pipeline():
			with conn.cursor() as cursor:
				for player_data in players_data.values():
					publish_player_data(cursor, player_data, year, week)
		conn.commit()  # commit changes after all data has been processed

def get_conference_data(apikey, year, conference, college_to_id):
	collector = CFBDCollector(apikey)
	conference_data = collector.get_conference_data(year, conference, college_to_id)
	return conference_data

def write_colleges_data(college_data, file_path):
	formatted_data = yaml.dump(college_data, default_flow_style=False)
	with open(file_path, 'w') as file:
		file.write(formatted_data)

def publish_colleges_data(db_name, db_username, db_password, colleges_data):
	with psycopg.connect(f'dbname={db_name} user={db_username} password={db_password}') as conn:
		with conn.pipeline():
			with conn.cursor() as cursor:
				for college_data in colleges_data:
					publish_college_data(cursor, college_data)
		conn.commit()  # commit changes after all data has been processed

if __name__ == '__main__':
	main()
