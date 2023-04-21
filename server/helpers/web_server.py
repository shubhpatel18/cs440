#!python3.8

import json
from enum import IntEnum
from typing import Tuple, Dict

from http.server import BaseHTTPRequestHandler, HTTPServer

from server_helpers.db_helper import TauDBHelper

class HTTPReturnCode(IntEnum):
	OK = 200
	BAD_REQUEST = 400
	SERVICE_UNAVAILABLE = 503

	def __str__(self):
		return str(self.value)

class TauHTTPServer(HTTPServer):
	def __init__(self, ip_address: str, port: int, db_helper: TauDBHelper) -> None:
		request_handler = TauHTTPRequestHandler(db_helper)
		super().__init__((ip_address, port), request_handler)

class TauHTTPRequestHandler(BaseHTTPRequestHandler):
	def __init__(self, db_helper: TauDBHelper):
		self.db_helper = db_helper

	def __call__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def _set_headers(self, return_code: int):
		self.send_response(return_code)
		self.send_header('Content-type', 'application/json')
		self.end_headers()

	def _parse_path(self) -> Tuple[str, Dict[str, str], bool]:
		try:
			path_split = self.path.split('?')
			path = path_split[0]
			param_dict = {}
			if len(path_split) > 1:
				param_str = path_split[1]
				param_pairs = param_str.split('&')
				for pair in param_pairs:
					k, v = pair.split('=')
					param_dict[k] = v
			print(path)
			return path, param_dict, False
		except ValueError as e:
			return '', {}, True

	# this function must be named this to override parent class
	def do_HEAD(self):
		self._set_headers()

	### get ##################################################################

	# this function must be named this to override parent class
	def do_GET(self):
		base_path, param_dict, error = self._parse_path()
		if base_path == '/example': get_handler = self._get_example
		elif base_path == '/login': get_handler = self._get_login
		elif base_path == '/fantasy_team': get_handler = self._get_fantasy_team
		elif base_path == '/available_players': get_handler = self._get_available_players
		else: get_handler = self._get_default
		return_code, json_response = get_handler(param_dict)

		self._set_headers(return_code)
		self.wfile.write(json.dumps(json_response).encode())

	def _get_default(self, param_dict: Dict) -> Tuple[int, Dict]:
		return HTTPReturnCode.OK, {'valid_request': False}

	def _get_example(self, param_dict: Dict) -> Tuple[int, Dict]:
		param_dict['valid_request'] = True
		return HTTPReturnCode.OK, param_dict

	def _get_login(self, param_dict: Dict) -> Tuple[int, Dict]:
		username = param_dict.get('username', None)
		password = param_dict.get('password', None)
		if not (username and password):
			return HTTPReturnCode.BAD_REQUEST, {
				'login_successful': False,
				'valid_request': False,
			}

		login_successful, error = self.db_helper.check_login(username, password)
		if error: return_code = HTTPReturnCode.SERVICE_UNAVAILABLE
		else: return_code = HTTPReturnCode.OK
		return return_code, {
			'login_successful': login_successful,
			'valid_request': True,
		}

	def _get_fantasy_team(self, param_dict: Dict) -> Tuple[int, Dict]:
		# TODO Kate
		return HTTPReturnCode.OK, {'valid_request': False}

	def _get_available_players(self, param_dict: Dict) -> Tuple[int, Dict]:
		username = param_dict.get('username', None)
		year = param_dict.get('year', None)
		week = param_dict.get('week', None)
		if not (username and year and week):
			return HTTPReturnCode.BAD_REQUEST, {
				'available_players': [],
				'valid_request': False,
			}

		available_players, error = self.db_helper.get_players_available_to_user(username, year, week)
		if error: return_code = HTTPReturnCode.SERVICE_UNAVAILABLE
		else: return_code = HTTPReturnCode.OK
		return return_code, {
			'available_players': available_players,
			'valid_request': True,
		}

	### post #################################################################

	# this function must be named this to override parent class
	def do_POST(self):
		if self.headers['Content-Type'] != 'application/json':
			self._set_headers(HTTPReturnCode.BAD_REQUEST)
			self.wfile.write(json.dumps({'valid_request': 'false'}).encode())
			return

		# read the json data and convert it into a dictionary
		length = int(self.headers['Content-Length'])
		post_data = self.rfile.read(length)
		try:
			post_dict = json.loads(post_data)
		except json.JSONDecodeError:
			self._set_headers(HTTPReturnCode.BAD_REQUEST)
			self.wfile.write(json.dumps({'valid_request': 'false'}).encode())
			return

		base_path, param_dict, error = self._parse_path()
		if base_path == '/example': post_handler = self._post_example
		elif base_path == '/signup': post_handler = self._post_signup
		elif base_path == '/change_password': post_handler = self._post_change_password
		elif base_path == '/create_fantasy_team': post_handler = self._post_create_fantasy_team
		elif base_path == '/add_player': post_handler = self._post_add_player
		else: post_handler = self._post_default
		return_code, json_response = post_handler(param_dict, post_dict)

		self._set_headers(return_code)
		self.wfile.write(json.dumps(json_response).encode())

	def _post_default(self, param_dict: Dict, post_dict: Dict) -> Tuple[int, Dict]:
		return HTTPReturnCode.OK, {'valid_request': 'false'}

	def _post_example(self, param_dict: Dict, post_dict: Dict) -> Tuple[int, Dict]:
		result = {}
		result['params'] = param_dict
		result['post'] = post_dict
		result['valid_request'] = True
		return HTTPReturnCode.OK, result

	def _post_signup(self, param_dict: Dict, post_dict: Dict) -> Tuple[int, Dict]:
		username = post_dict.get('username', None)
		name = post_dict.get('name', None)
		password = post_dict.get('password', None)
		if not (username and name and password):
			return HTTPReturnCode.BAD_REQUEST, {
				'signup_successful': False,
				'username_taken': False,
				'valid_request': False,
			}

		signup_successful, username_taken, error = self.db_helper.signup(username, name, password)
		if error: return_code = HTTPReturnCode.SERVICE_UNAVAILABLE
		elif username_taken: return_code = HTTPReturnCode.BAD_REQUEST
		else: return_code = HTTPReturnCode.OK
		return return_code, {
			'signup_successful': signup_successful,
			'username_taken': username_taken,
			'valid_request': True,
		}

	def _post_change_password(self, param_dict: Dict, post_dict: Dict) -> Tuple[int, Dict]:
		username = post_dict.get('username', None)
		old_password = post_dict.get('old_password', None)
		new_password = post_dict.get('new_password', None)
		if not (username and old_password and new_password):
			return HTTPReturnCode.BAD_REQUEST, {
				'password_change_successful': False,
				'valid_request': False,
			}

		password_change_successful, error = self.db_helper.change_password(username, old_password, new_password)
		if error: return_code = HTTPReturnCode.SERVICE_UNAVAILABLE
		else: return_code = HTTPReturnCode.OK
		return return_code, {
			'password_change_successful': password_change_successful,
			'valid_request': True,
		}

	def _post_create_fantasy_team(self, param_dict: Dict, post_dict: Dict) -> Tuple[int, Dict]:
		team_name = post_dict.get('team_name', None)
		username = post_dict.get('username', None)
		if not (team_name and username):
			return HTTPReturnCode.BAD_REQUEST, {
				'create_team_successful': False,
				'valid_request': False,
			}

		create_team_successful, error = self.db_helper.create_fantasy_team(team_name, username)
		if error: return_code = HTTPReturnCode.SERVICE_UNAVAILABLE
		else: return_code = HTTPReturnCode.OK
		return return_code, {
			'create_team_successful': create_team_successful,
			'valid_request': True,
		}

	def _post_add_player(self, param_dict: Dict, post_dict: Dict) -> Tuple[int, Dict]:
		player_name = post_dict.get('player_name', None)
		team_name = post_dict.get('team_name', None)
		if not (player_name and team_name):
			return HTTPReturnCode.BAD_REQUEST, {
				'add_player_successful': False,
				'valid_request': False,
			}

		add_player_successful, error = self.db_helper.add_player_to_fantasy_team(player_name, team_name)
		if error: return_code = HTTPReturnCode.SERVICE_UNAVAILABLE
		else: return_code = HTTPReturnCode.OK
		return return_code, {
			'add_player_successful': add_player_successful,
			'valid_request': True,
		}
