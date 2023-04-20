from typing import Dict, Tuple, List 

import hashlib

import psycopg

#!python3.8

class TauDBHelper:
	def __init__(self, db_name: str, db_username: str, db_password: str) -> None:
		self.db_name = db_name
		self.db_username = db_username
		self.db_password = db_password

	def check_login(self, username, password) -> Tuple[bool, bool]:
		hashed_password = hashlib.md5(password.encode()).hexdigest()

		with psycopg.connect(f'dbname={self.db_name} user={self.db_username} password={self.db_password}') as conn:
			with conn.cursor() as curs:
				# check if credentials are correct
				curs.execute("SELECT * FROM users WHERE username=%s and password=%s", (username, hashed_password))
				login_successful = curs.rowcount > 0

		error = False
		return login_successful, error

	def signup(self, username, name, password) -> Tuple[bool, bool, bool]:
		hashed_password = hashlib.md5(password.encode()).hexdigest()

		with psycopg.connect(f'dbname={self.db_name} user={self.db_username} password={self.db_password}') as conn:
			with conn.cursor() as curs:
				# check if username is taken
				curs.execute("SELECT * FROM users WHERE username=%s", [username])
				if curs.rowcount:
					# username taken
					signup_successful = False
					username_taken = True

				# sign up user
				else:
					curs.execute("INSERT INTO users (username, name, password) VALUES (%s, %s, %s);",
						(username, name, hashed_password)
					)
					signup_successful = True
					username_taken = False

			conn.commit()  # commit changes after data has been processed

		error = False
		return signup_successful, username_taken, error

	def change_password(self, username, old_password, new_password) -> Tuple[bool, bool]:
		hashed_old_password = hashlib.md5(old_password.encode()).hexdigest()
		hashed_new_password = hashlib.md5(new_password.encode()).hexdigest()

		with psycopg.connect(f'dbname={self.db_name} user={self.db_username} password={self.db_password}') as conn:
			with conn.cursor() as curs:
				# check if credentials are correct
				curs.execute("SELECT * FROM users WHERE username=%s and password=%s", (username, hashed_old_password))
				if curs.rowcount:
					# credentials correct
					curs.execute("UPDATE users SET password=%s WHERE username=%s and password=%s;",
						(hashed_new_password, username, hashed_old_password)
					)
					password_change_successful = True

				# credentials incorrect
				else:
					password_change_successful = False

		error = False
		return password_change_successful, error

	def create_fantasy_team(self, team_name: str, user: str) -> Tuple[bool, bool]:
		# TODO: Shubh
		create_team_successful = False
		error = True
		return create_team_successful, error

	def view_fantasy_team(self, username: str) -> Tuple[List[Dict], bool]:
		# TODO: Kate
		fantasy_team = []
		error = True
		return fantasy_team, error

	def add_player_to_fantasy_team(self, player_name: str, team_name: str) -> Tuple[bool, bool]:
		# TODO: Shubh
		add_player_successful = False
		error = True
		return add_player_successful, error

	def get_players_available_to_user(self, username: str, year:int, week: int) -> Tuple[List[Dict], bool]:
		# TODO: Shubh
		available_players = []
		error = True
		return available_players, error
