from typing import Tuple

import hashlib

import psycopg

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
