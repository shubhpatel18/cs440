from typing import Tuple

class TauDBHelper:
	def __init__(self, db_name: str, db_username: str, db_password: str) -> None:
		self.db_name = db_name
		self.db_username = db_username
		self.db_password = db_password

	def check_login(self, username, password) -> Tuple[bool, bool]:
		# TODO
		login_successful = True
		error = False
		return login_successful, error

	def signup(self, username, password) -> Tuple[bool, bool, bool]:
		# TODO
		signup_successful = True
		username_taken = False
		error = False
		return signup_successful, username_taken, error

	def change_password(self, username, old_password, new_password) -> Tuple[bool, bool]:
		# TODO
		password_change_successful = True
		error = False
		return password_change_successful, error
