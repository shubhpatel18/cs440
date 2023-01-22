### publish player data ######################################################

_players_columns = [
	('id', 						'%s'),
	('name', 					'%s'),
	('position', 				'%s'),
	('college_id', 				'%s'),
	('total_yards', 			'%s'),
	('touchdowns', 				'%s'),
	('turnovers_lost', 			'%s'),
	('receptions', 				'%s'),
	('sacks', 					'%s'),
	('tackles_for_loss', 		'%s'),
	('interceptions', 			'%s'),
	('fumbles_recovered', 		'%s'),
	('punting_yards', 			'%s'),
	('field_goal_percentage', 	'%s'),
	('injury_status', 			'%s'),
]

# unpack _players_columns into the components of the insert statement
_players_column_names, _players_column_data_types, = zip(*_players_columns)
_players_column_names_str = ', '.join(_players_column_names)
_players_data_types_str = ', '.join(_players_column_data_types)

def publish_player_data(cursor, data, week):
	values = [
		data['id'],
		data['name'],
		data['position'],
		data['college_id'],
		data['total_yards'],
		data['touchdowns'],
		data['turnovers_lost'],
		data['receptions'],
		data['sacks'],
		data['tackles_for_loss'],
		data['interceptions'],
		data['fumbles_recovered'],
		data['punting_yards'],
		data['fg_percentage'],
		data['injury_status'],
	]

	# insert the data into the database
	cursor.execute(f'INSERT INTO players_2022_w{week} ({_players_column_names_str}) VALUES ({_players_data_types_str})', values)

### examples #################################################################

def main():
	import os
	from config_reader import read_config

	dir_path = os.path.dirname(os.path.realpath(__file__))
	config_file_path = os.path.join(dir_path, 'resources', 'config.yaml')
	config = read_config(config_file_path)
	db_name = config['database']['dbname']
	db_username = config['database']['username']
	db_password = config['database']['password']

	### publish player data example ##########################################

	import psycopg

	player_data = {
		'id': 1,
		'name': 'Brock Purdy',
		'position': 'QB',
		'college_id': 1,
		'total_yards': 2500,
		'touchdowns': 16,
		'turnovers_lost': 4,
		'receptions': 1,
		'sacks': 0,
		'tackles_for_loss': 0,
		'interceptions': 0,
		'fumbles_recovered': 0,
		'punting_yards': 0,
		'fg_percentage': 0,
		'injury_status': 'Healthy'
	}
	week = 1

	with psycopg.connect(f'dbname={db_name} user={db_username} password={db_password}') as conn:
		with conn.cursor() as cursor:
			publish_player_data(cursor, player_data, week)
			conn.commit()

	### ######################################################################

if __name__ == '__main__':
	main()
