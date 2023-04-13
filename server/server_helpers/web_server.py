import json
from enum import IntEnum
from typing import Tuple, Dict

from http.server import BaseHTTPRequestHandler, HTTPServer

from server_helpers.db_server_helper import TauDBHelper

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

	def do_HEAD(self):
		self._set_headers()

	### get ##################################################################

	def do_GET(self):
		path, param_dict, error = self._parse_path()
		if path == '/example': get_handler = self._get_example
		elif path == '/login': get_handler = self._get_login
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

	### post #################################################################

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

		path, param_dict, error = self._parse_path()
		if path == '/example': post_handler = self._post_example
		elif path == '/signup': post_handler = self._post_signup
		elif path == '/change_password': post_handler = self._post_change_password
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
