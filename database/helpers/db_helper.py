#!python3.8

### publish player data ######################################################

_player_data_columns = [
	('player_id', 			'%s'),
	('receptions', 			'%s'),
	('total_yards', 		'%s'),
	('touchdowns', 			'%s'),
	('turnovers_lost', 		'%s'),
	('sacks', 				'%s'),
	('tackles_for_loss', 	'%s'),
	('interceptions', 		'%s'),
	('fumbles_recovered', 	'%s'),
	('punting_yards', 		'%s'),
	('fg_percentage', 		'%s'),
	('injury_status', 		'%s'),
	('college_id', 			'%s'),
	('year', 				'%s'),
	('week', 				'%s'),
]

# unpack _players_columns into the components of the insert statement
_player_data_column_names, _player_data_column_data_types, = zip(*_player_data_columns)
_player_data_column_names_str = ', '.join(_player_data_column_names)
_player_data_data_types_str = ', '.join(_player_data_column_data_types)

def publish_player_data(cursor, data, year, week):
	player_data_values = [
		data['id'],
		data['receptions'],
		data['total_yards'],
		data['touchdowns'],
		data['turnovers_lost'],
		data['sacks'],
		data['tackles_for_loss'],
		data['interceptions'],
		data['fumbles_recovered'],
		data['punting_yards'],
		data['fg_percentage'],
		data['injury_status'],
		data['college_id'],
		year,
		week
	]

	# insert the data into the database
	cursor.execute(f'INSERT INTO players (player_id, player_name, position) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING',
		(data['id'], data['name'], data['position']))
	cursor.execute(f'INSERT INTO player_data ({_player_data_column_names_str}) VALUES ({_player_data_data_types_str})',
		(player_data_values))

### publish college data #####################################################

_college_columns = [
	('college_id', 			'%s'),
	('college_name', 		'%s'),
	('wins', 				'%s'),
	('ties', 				'%s'),
	('losses', 				'%s'),
]

# unpack _college_columns into the components of the insert statement
_college_column_names, _college_column_data_types, = zip(*_college_columns)
_college_column_names_str = ', '.join(_college_column_names)
_college_data_types_str = ', '.join(_college_column_data_types)

def publish_college_data(cursor, data):
	values = [
		data['college_id'],
		data['college_name'],
		data['wins'],
		data['ties'],
		data['losses'],
	]

	# insert the data into the database
	cursor.execute(f'INSERT INTO colleges ({_college_column_names_str}) VALUES ({_college_data_types_str}) ON CONFLICT DO NOTHING',
		values)

### examples #################################################################

def main():
	import os
	import psycopg
	from common.config_reader import read_config

	dir_path = os.path.dirname(os.path.realpath(__file__))
	config_file_path = os.path.join(dir_path, 'resources', 'config.yaml')
	config = read_config(config_file_path)
	db_name = config['database']['dbname']
	db_username = config['database']['username']
	db_password = config['database']['password']

	### publish player data example ##########################################

	player_data = {
		'player_id': 1,
		'name': 'Brock Purdy',
		'position': 'QB',
		'receptions': 1,
		'total_yards': 2500,
		'touchdowns': 16,
		'turnovers_lost': 4,
		'sacks': 0,
		'tackles_for_loss': 0,
		'interceptions': 0,
		'fumbles_recovered': 0,
		'punting_yards': 0,
		'fg_percentage': 0,
		'injury_status': 'Healthy',
		'college_id': 1,
	}
	week = 1

	with psycopg.connect(f'dbname={db_name} user={db_username} password={db_password}') as conn:
		with conn.cursor() as cursor:
			publish_player_data(cursor, player_data, week)
			conn.commit()

	### ######################################################################

	college_data = {
		'college_id': 1,
		'college_name': 'Baylor',
		'wins': 7,
		'ties': 1,
		'losses': 6,
	}

	with psycopg.connect(f'dbname={db_name} user={db_username} password={db_password}') as conn:
		with conn.cursor() as cursor:
			publish_college_data(cursor, college_data)
			conn.commit()

	### ######################################################################

if __name__ == '__main__':
	main()
