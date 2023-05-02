#!python3.8

import json
import urllib
from enum import IntEnum
from typing import Tuple, Dict

from http.server import BaseHTTPRequestHandler, HTTPServer

from common.translations import POSITION_TO_ROLES

from helpers.db_helper import TauDBHelper

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
			url = self.path
			decoded_url = urllib.parse.unquote_plus(url)
			path_split = decoded_url.split('?')
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
		elif base_path == '/fantasy_teams': get_handler = self._get_fantasy_teams
		elif base_path == '/available_players': get_handler = self._get_available_players
		else: get_handler = self._get_default
		return_code, json_response = get_handler(param_dict)

		self._set_headers(return_code)
		self.wfile.write(json.dumps(json_response).encode())

	def _get_default(self, param_dict: Dict) -> Tuple[int, Dict]:
		return HTTPReturnCode.SERVICE_UNAVAILABLE, {'valid_request': False}

	def _get_example(self, param_dict: Dict) -> Tuple[int, Dict]:
		param_dict['valid_request'] = True
		return HTTPReturnCode.OK, param_dict

	def _get_login(self, param_dict: Dict) -> Tuple[int, Dict]:
		username = param_dict.get('username', '')
		password = param_dict.get('password', '')
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

	def _get_fantasy_teams(self, param_dict: Dict) -> Tuple[int, Dict]:
		username = param_dict.get('username', '')
		year = param_dict.get('year', None)
		week = param_dict.get('week', None)
		receptions_multiplier = param_dict.get('receptions_multiplier', 0)
		total_yards_multiplier = param_dict.get('total_yards_multiplier', 0)
		touchdowns_multiplier = param_dict.get('touchdowns_multiplier', 0)
		turnovers_lost_mulitplier = param_dict.get('turnovers_lost_mulitplier', 0)
		sacks_multiplier = param_dict.get('sacks_multiplier', 0)
		tackles_for_loss_multiplier = param_dict.get('tackles_for_loss_multiplier', 0)
		interceptions_multiplier = param_dict.get('interceptions_multiplier', 0)
		fumbles_recovered_multiplier = param_dict.get('fumbles_recovered_multiplier', 0)
		punting_yards_multiplier = param_dict.get('punting_yards_multiplier', 0)
		fg_percentage_multiplier = param_dict.get('fg_percentage_multiplier', 0)
		if not (
			username and year and week
			and receptions_multiplier and total_yards_multiplier and touchdowns_multiplier and turnovers_lost_mulitplier and sacks_multiplier and tackles_for_loss_multiplier and interceptions_multiplier and fumbles_recovered_multiplier and punting_yards_multiplier and fg_percentage_multiplier
		):
			return HTTPReturnCode.BAD_REQUEST, {
				'fantasy_teams': {},
				'user_exists': False,
				'team_exists': False,
				'valid_request': False,
			}
		
		try:
			year = int(year)
			week = int(week)
			receptions_multiplier = float(receptions_multiplier)
			total_yards_multiplier = float(total_yards_multiplier)
			touchdowns_multiplier = float(touchdowns_multiplier)
			turnovers_lost_mulitplier = float(turnovers_lost_mulitplier)
			sacks_multiplier = float(sacks_multiplier)
			tackles_for_loss_multiplier = float(tackles_for_loss_multiplier)
			interceptions_multiplier = float(interceptions_multiplier)
			fumbles_recovered_multiplier = float()
			punting_yards_multiplier = float(fumbles_recovered_multiplier)
			fg_percentage_multiplier = float(fg_percentage_multiplier)
		except:
			return HTTPReturnCode.BAD_REQUEST, {
				'fantasy_teams': {},
				'user_exists': False,
				'team_exists': False,
				'valid_role': False,
				'valid_request': False,
			}

		fantasy_teams, user_exists, team_exists, error = self.db_helper.view_fantasy_teams(
			username, year, week,
			receptions_multiplier, total_yards_multiplier, touchdowns_multiplier, turnovers_lost_mulitplier, sacks_multiplier, tackles_for_loss_multiplier, interceptions_multiplier, fumbles_recovered_multiplier, punting_yards_multiplier, fg_percentage_multiplier
		)
		if error: return_code = HTTPReturnCode.SERVICE_UNAVAILABLE
		else: return_code = HTTPReturnCode.OK
		return return_code, {
			'fantasy_teams': fantasy_teams,
			'user_exists': user_exists,
			'team_exists': team_exists,
			'valid_request': True,
		}

	def _get_available_players(self, param_dict: Dict) -> Tuple[int, Dict]:
		team_name = param_dict.get('team_name', '')
		username = param_dict.get('username', '')
		team_role = param_dict.get('team_role', '').lower()
		year = param_dict.get('year', None)
		week = param_dict.get('week', None)
		receptions_multiplier = param_dict.get('receptions_multiplier', 0)
		total_yards_multiplier = param_dict.get('total_yards_multiplier', 0)
		touchdowns_multiplier = param_dict.get('touchdowns_multiplier', 0)
		turnovers_lost_mulitplier = param_dict.get('turnovers_lost_mulitplier', 0)
		sacks_multiplier = param_dict.get('sacks_multiplier', 0)
		tackles_for_loss_multiplier = param_dict.get('tackles_for_loss_multiplier', 0)
		interceptions_multiplier = param_dict.get('interceptions_multiplier', 0)
		fumbles_recovered_multiplier = param_dict.get('fumbles_recovered_multiplier', 0)
		punting_yards_multiplier = param_dict.get('punting_yards_multiplier', 0)
		fg_percentage_multiplier = param_dict.get('fg_percentage_multiplier', 0)
		if not (
			team_name and username and team_role and year and week
			and receptions_multiplier and total_yards_multiplier and touchdowns_multiplier and turnovers_lost_mulitplier and sacks_multiplier and tackles_for_loss_multiplier and interceptions_multiplier and fumbles_recovered_multiplier and punting_yards_multiplier and fg_percentage_multiplier
		):
			return HTTPReturnCode.BAD_REQUEST, {
				'available_players': [],
				'user_exists': False,
				'team_exists': False,
				'valid_role': False,
				'valid_request': False,
			}
		
		try:
			year = int(year)
			week = int(week)
			receptions_multiplier = float(receptions_multiplier)
			total_yards_multiplier = float(total_yards_multiplier)
			touchdowns_multiplier = float(touchdowns_multiplier)
			turnovers_lost_mulitplier = float(turnovers_lost_mulitplier)
			sacks_multiplier = float(sacks_multiplier)
			tackles_for_loss_multiplier = float(tackles_for_loss_multiplier)
			interceptions_multiplier = float(interceptions_multiplier)
			fumbles_recovered_multiplier = float()
			punting_yards_multiplier = float(fumbles_recovered_multiplier)
			fg_percentage_multiplier = float(fg_percentage_multiplier)
		except:
			return HTTPReturnCode.BAD_REQUEST, {
				'fantasy_teams': {},
				'user_exists': False,
				'team_exists': False,
				'valid_role': False,
				'valid_request': False,
			}

		available_players, user_exists, team_exists, valid_role, error = self.db_helper.get_players_available_to_team(
			team_name, username, team_role, year, week,
			receptions_multiplier, total_yards_multiplier, touchdowns_multiplier, turnovers_lost_mulitplier, sacks_multiplier, tackles_for_loss_multiplier, interceptions_multiplier, fumbles_recovered_multiplier, punting_yards_multiplier, fg_percentage_multiplier
		)
		if error: return_code = HTTPReturnCode.SERVICE_UNAVAILABLE
		else: return_code = HTTPReturnCode.OK
		return return_code, {
			'available_players': available_players,
			'user_exists': user_exists,
			'team_exists': team_exists,
			'valid_role': valid_role,
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
		elif base_path == '/remove_fantasy_team': post_handler = self._post_remove_fantasy_team
		elif base_path == '/rename_fantasy_team': post_handler = self._post_rename_fantasy_team
		elif base_path == '/set_player': post_handler = self._post_set_player
		elif base_path == '/clear_role': post_handler = self._post_clear_role
		else: post_handler = self._post_default
		return_code, json_response = post_handler(param_dict, post_dict)

		self._set_headers(return_code)
		self.wfile.write(json.dumps(json_response).encode())

	def _post_default(self, param_dict: Dict, post_dict: Dict) -> Tuple[int, Dict]:
		return HTTPReturnCode.SERVICE_UNAVAILABLE, {'valid_request': 'false'}

	def _post_example(self, param_dict: Dict, post_dict: Dict) -> Tuple[int, Dict]:
		result = {}
		result['params'] = param_dict
		result['post'] = post_dict
		result['valid_request'] = True
		return HTTPReturnCode.OK, result

	def _post_signup(self, param_dict: Dict, post_dict: Dict) -> Tuple[int, Dict]:
		username = post_dict.get('username', '')
		name = post_dict.get('name', '')
		password = post_dict.get('password', '')
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
		username = post_dict.get('username', '')
		old_password = post_dict.get('old_password', '')
		new_password = post_dict.get('new_password', '')
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
		team_name = post_dict.get('team_name', '')
		username = post_dict.get('username', '')
		if not (team_name and username):
			return HTTPReturnCode.BAD_REQUEST, {
				'create_team_successful': False,
				'user_exists': False,
				'user_already_using_team_name': False,
				'valid_request': False,
			}

		create_team_successful, user_exists, user_already_using_team_name, error = self.db_helper.create_fantasy_team(team_name, username)
		if error: return_code = HTTPReturnCode.SERVICE_UNAVAILABLE
		else: return_code = HTTPReturnCode.OK
		return return_code, {
			'create_team_successful': create_team_successful,
			'user_exists': user_exists,
			'user_already_using_team_name': user_already_using_team_name,
			'valid_request': True,
		}

	def _post_remove_fantasy_team(self, param_dict: Dict, post_dict: Dict) -> Tuple[int, Dict]:
		team_name = post_dict.get('team_name', '')
		username = post_dict.get('username', '')
		if not (team_name and username):
			return HTTPReturnCode.BAD_REQUEST, {
				'remove_team_successful': False,
				'user_exists': False,
				'team_exists': False,
				'valid_request': False,
			}

		remove_team_successful, user_exists, team_exists, error = self.db_helper.remove_fantasy_team(team_name, username)
		if error: return_code = HTTPReturnCode.SERVICE_UNAVAILABLE
		else: return_code = HTTPReturnCode.OK
		return return_code, {
			'remove_team_successful': remove_team_successful,
			'user_exists': user_exists,
			'team_exists': team_exists,
			'valid_request': True,
		}

	def _post_rename_fantasy_team(self, param_dict: Dict, post_dict: Dict) -> Tuple[int, Dict]:
		team_name = post_dict.get('team_name', '')
		new_team_name = post_dict.get('new_team_name', '')
		username = post_dict.get('username', '')
		if not (team_name and new_team_name and username):
			return HTTPReturnCode.BAD_REQUEST, {
				'rename_team_successful': False,
				'user_exists': False,
				'team_exists': False,
				'user_already_using_team_name': False,
				'valid_request': False,
			}

		rename_team_successful, user_exists, team_exists, user_already_using_team_name, error = self.db_helper.rename_fantasy_team(team_name, new_team_name, username)
		if error: return_code = HTTPReturnCode.SERVICE_UNAVAILABLE
		else: return_code = HTTPReturnCode.OK
		return return_code, {
			'rename_team_successful': rename_team_successful,
			'user_exists': user_exists,
			'team_exists': team_exists,
			'user_already_using_team_name': user_already_using_team_name,
			'valid_request': True,
		}

	def _post_set_player(self, param_dict: Dict, post_dict: Dict) -> Tuple[int, Dict]:
		player_name = post_dict.get('player_name', '')
		player_position = post_dict.get('player_position', '')
		team_role = post_dict.get('team_role', '').lower()
		team_name = post_dict.get('team_name', '')
		username = post_dict.get('username', '')
		if not (player_name and player_position and team_role and team_name and username):
			return HTTPReturnCode.BAD_REQUEST, {
				'valid_position': False,
				'add_player_successful': False,
				'user_exists': False,
				'team_exists': False,
				'player_exists': False,
				'valid_role': False,
				'valid_request': False,
			}
		
		position_exists = player_position in POSITION_TO_ROLES
		position_allowed = position_exists and team_role in POSITION_TO_ROLES[player_position]
		if not position_allowed:
			return HTTPReturnCode.BAD_REQUEST, {
				'valid_position': False,
				'add_player_successful': False,
				'user_exists': False,
				'team_exists': False,
				'player_exists': False,
				'valid_role': False,
				'valid_request': True,
			}

		response = self.db_helper.set_player_in_fantasy_team(player_name, player_position, team_role, team_name, username)
		add_player_successful, user_exists, team_exists, player_exists, valid_role, error = response
		if error: return_code = HTTPReturnCode.SERVICE_UNAVAILABLE
		else: return_code = HTTPReturnCode.OK
		return return_code, {
			'valid_position': True,
			'add_player_successful': add_player_successful,
			'user_exists': user_exists,
			'team_exists': team_exists,
			'player_exists': player_exists,
			'valid_role': valid_role,
			'valid_request': True,
		}

	def _post_clear_role(self, param_dict: Dict, post_dict: Dict) -> Tuple[int, Dict]:
		team_role = post_dict.get('team_role', '').lower()
		team_name = post_dict.get('team_name', '')
		username = post_dict.get('username', '')
		if not (team_role and team_name and username):
			return HTTPReturnCode.BAD_REQUEST, {
				'clear_role_successful': False,
				'user_exists': False,
				'team_exists': False,
				'valid_role': False,
				'valid_request': False,
			}

		response = self.db_helper.clear_role_in_fantasy_team(team_role, team_name, username)
		remove_player_successful, user_exists, team_exists, valid_role, error = response
		if error: return_code = HTTPReturnCode.SERVICE_UNAVAILABLE
		else: return_code = HTTPReturnCode.OK
		return return_code, {
			'clear_role_successful': remove_player_successful,
			'user_exists': user_exists,
			'team_exists': team_exists,
			'valid_role': valid_role,
			'valid_request': True,
		}
