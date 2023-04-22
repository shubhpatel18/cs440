#!python3.8

import hashlib
from typing import Dict, Tuple, List 

import psycopg

##############################################################################
# ERROR HANDLING NOT YET IMPLEMENTED, ALL FUNCTIONS RETURN ERROR = FALSE
##############################################################################

class TauDBHelper:
	def __init__(self, db_name: str, db_username: str, db_password: str) -> None:
		self.db_name = db_name
		self.db_username = db_username
		self.db_password = db_password

	def check_login(self, username, password) -> Tuple[bool, bool]:
		"""returns login_successful, error"""

		hashed_password = hashlib.md5(password.encode()).hexdigest()

		with psycopg.connect(f'dbname={self.db_name} user={self.db_username} password={self.db_password}') as conn:
			with conn.cursor() as curs:
				# check if credentials are correct
				curs.execute("SELECT * FROM users WHERE username=%s AND password=%s",
					(username, hashed_password))
				credentials_correct = curs.rowcount > 0
				return credentials_correct, False

	def signup(self, username, name, password) -> Tuple[bool, bool, bool]:
		"""returns signup_successful, username_taken, error"""

		hashed_password = hashlib.md5(password.encode()).hexdigest()

		with psycopg.connect(f'dbname={self.db_name} user={self.db_username} password={self.db_password}') as conn:
			with conn.cursor() as curs:
				# check if username is taken
				curs.execute("SELECT * FROM users WHERE username=%s", (username,))
				username_taken = curs.rowcount > 0
				if username_taken:
					return False, True, False

				# sign up user
				curs.execute("INSERT INTO users (username, name, password) VALUES (%s, %s, %s);",
					(username, name, hashed_password))
				conn.commit()
				return True, False, False

	def change_password(self, username, old_password, new_password) -> Tuple[bool, bool]:
		"""returns password_change_successful, error"""

		hashed_old_password = hashlib.md5(old_password.encode()).hexdigest()
		hashed_new_password = hashlib.md5(new_password.encode()).hexdigest()

		with psycopg.connect(f'dbname={self.db_name} user={self.db_username} password={self.db_password}') as conn:
			with conn.cursor() as curs:
				# check if credentials are correct
				curs.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, hashed_old_password))
				credentials_correct = curs.rowcount > 0
				if not credentials_correct:
					return False, False

				# update password
				curs.execute("UPDATE users SET password=%s WHERE username=%s AND password=%s;",
					(hashed_new_password, username, hashed_old_password))
				conn.commit()
				return True, False

	def create_fantasy_team(self, team_name: str, username: str) -> Tuple[bool, bool, bool]:
		"""returns create_team_successful, user_exists, user_already_using_team_name, error"""

		with psycopg.connect(f'dbname={self.db_name} user={self.db_username} password={self.db_password}') as conn:
			with conn.cursor() as curs:
				# check if user exists
				curs.execute("SELECT * FROM users WHERE username=%s", (username,))
				user_exists = curs.rowcount > 0
				if not user_exists:
					return False, False, False, False

				# get user id
				user_info = curs.fetchone()
				user_id = int(user_info[0])

				# check if team name already being used by user
				curs.execute("SELECT * FROM fantasy_teams WHERE team_name=%s AND user_id=%s",
					(team_name, user_id))
				team_name_taken = curs.rowcount > 0
				if team_name_taken:
					return False, True, True, False

				# create team
				curs.execute("INSERT INTO fantasy_teams (team_name, user_id) VALUES (%s, %s);",
					(team_name, user_id))
				conn.commit()
				return True, True, False, False

	def view_fantasy_teams(self, username: str) -> Tuple[Dict[str, Dict[str, List]], bool]:
		# TODO: Kate
		# position info for each team associated with a user
		# {
		#     team_name1: {
		#         qb: [qb player stats],
		#         ...
		#         kicker: [kicker player stats],
		#     },
		#     team_name2: {
		#         qb: [qb player stats],
		#         ...
		#         kicker: [kicker player stats],
		#     },
		# }
		fantasy_teams = {}
		error = True
		return fantasy_teams, error

	def set_player_in_fantasy_team(self, player_name: str, player_position: str, team_role: str, team_name: str, username: str) -> Tuple[bool, bool, bool, bool, bool]:
		"""returns add_player_successful, user_exists, team_exists, player_exists, error"""

		# TODO incorporate username in request handler and test client

		with psycopg.connect(f'dbname={self.db_name} user={self.db_username} password={self.db_password}') as conn:
			with conn.cursor() as curs:
				# check if user exists
				curs.execute("SELECT * FROM users WHERE username=%s", (username,))
				user_exists = curs.rowcount > 0
				if not user_exists:
					return False, False, False, False, False

				# get user id
				user_info = curs.fetchone()
				user_id = int(user_info[0])

				# make sure team exists
				curs.execute("SELECT * FROM fantasy_teams WHERE team_name=%s AND user_id=%s",
					(team_name, user_id))
				team_exists = curs.rowcount > 0
				if not team_exists:
					return False, True, False, False, False

				# get player id
				curs.execute("SELECT * FROM players WHERE player_name=%s AND position=%s",
					(player_name, player_position))
				player_exists = curs.rowcount > 0
				if not player_exists:
					return False, True, True, False, False
				player_data = curs.fetchone()
				player_id = player_data[1]

				# add player to team
				curs.execute(f"UPDATE fantasy_teams SET {team_role}_id=%s WHERE team_name=%s AND user_id=%s;",
					(player_id, team_name, user_id))
				conn.commit()
				return True, True, True, True, False

	def get_players_available_to_team(self, team_name: str, username: str, year:int, week: int) -> Tuple[List[Dict], bool]:
		"""returns players_available_to_team, user_exists, team_exists, error"""

		with psycopg.connect(f'dbname={self.db_name} user={self.db_username} password={self.db_password}') as conn:
			with conn.cursor() as curs:
				# check if user exists
				curs.execute("SELECT * FROM users WHERE username=%s", (username,))
				user_exists = curs.rowcount > 0
				if not user_exists:
					return [], False, False, False

				# get user id
				user_info = curs.fetchone()
				user_id = int(user_info[0])

				# get team roster
				positions = "qb_id, rb_id, wr1_id, wr2_id, te_id, flex_id, center_id, lg_id, rg_id, punter_id, de1_id, de2_id, dt1_id, dt2_id, lb1_id, lb2_id, lb3_id, cb1_id, cb2_id, s1_id, s2_id, kicker_id"
				curs.execute(f"SELECT {positions} FROM fantasy_teams WHERE team_name=%s AND user_id=%s",
					(team_name, user_id))
				team_exists = curs.rowcount > 0
				if not team_exists:
					return [], True, False, False

				team_player_ids = set(curs.fetchone())

				# look up players stats for year and week
				player_info = "player_name, position, receptions, total_yards, touchdowns, turnovers_lost, sacks, tackles_for_loss, interceptions, fumbles_recovered, punting_yards, fg_percentage, injury_status, college_name"
				curs.execute(
					f"""SELECT {player_info}
						FROM players join colleges
							ON players.college_id=colleges.college_id
						WHERE year=%s AND week=%s
					""",
					(year, week)
				)
				all_available_players = curs.fetchall()

		# filter players available to team
		def available_to_team(player_data):
			player_id = player_data[1]
			return player_id not in team_player_ids
		players_available_to_team = list(filter(available_to_team, all_available_players))
		return players_available_to_team, True, True, False
