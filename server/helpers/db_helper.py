#!python3.8

import hashlib
from collections import defaultdict
from typing import Dict, Tuple, List 

import psycopg

from common.translations import TEAM_ROLES, ROLE_TO_POSITIONS

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

	def remove_fantasy_team(self, team_name: str, username: str) -> Tuple[bool, bool, bool, bool]:
		"""returns remove_team_successful, user_exists, team_exists, error"""

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

				# check if team exists
				curs.execute("SELECT * FROM fantasy_teams WHERE team_name=%s AND user_id=%s",
					(team_name, user_id))
				team_exists = curs.rowcount > 0
				if not team_exists:
					return False, True, False, False

				# create team
				curs.execute("DELETE FROM fantasy_teams WHERE team_name=%s AND user_id=%s;",
					(team_name, user_id))
				conn.commit()
				return True, True, True, False

	def rename_fantasy_team(self, team_name: str, new_team_name: str, username: str) -> Tuple[bool, bool, bool, bool, bool]:
		"""returns rename_team_successful, user_exists, team_exists, user_already_using_team_name, error"""

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

				# check if team exists
				curs.execute("SELECT * FROM fantasy_teams WHERE team_name=%s AND user_id=%s",
					(team_name, user_id))
				team_exists = curs.rowcount > 0
				if not team_exists:
					return False, True, False, False, False

				# check if user already using new team name
				curs.execute("SELECT * FROM fantasy_teams WHERE team_name=%s AND user_id=%s",
					(new_team_name, user_id))
				user_already_using_team_name = curs.rowcount > 0
				if user_already_using_team_name:
					return False, True, True, True, False

				# create team
				curs.execute("UPDATE fantasy_teams SET team_name=%s WHERE team_name=%s AND user_id=%s;",
					(new_team_name, team_name, user_id))
				conn.commit()
				return True, True, True, False, False

	def view_fantasy_teams(self, username: str, year: int, week: int,
			receptions_multiplier: float, total_yards_multiplier: float, touchdowns_multiplier: float, turnovers_lost_mulitplier: float, sacks_multiplier: float, tackles_for_loss_multiplier: float, interceptions_multiplier: float, fumbles_recovered_multiplier: float, punting_yards_multiplier: float, fg_percentage_multiplier: float
		) -> Tuple[Dict[str, Dict[str, List]], bool, bool, bool]:
		"""returns fantasy_teams, user_exists, team_exists, error"""

		with psycopg.connect(f'dbname={self.db_name} user={self.db_username} password={self.db_password}') as conn:
			with conn.cursor() as curs:
				# check if user exists
				curs.execute("SELECT * FROM users WHERE username=%s", (username,))
				user_exists = curs.rowcount > 0
				if not user_exists:
					return {}, False, False, False

				# get user id
				user_info = curs.fetchone()
				user_id = int(user_info[0])

				# get team roster for each team associated with user
				curs.execute(
					"""
					SELECT
						team_name, qb_id, rb_id, wr1_id, wr2_id, te_id, flex_id, center_id, lg_id, rg_id, punter_id, de1_id, de2_id, dt1_id, dt2_id, lb1_id, lb2_id, lb3_id, cb1_id, cb2_id, s1_id, s2_id, kicker_id
					FROM fantasy_teams
					WHERE user_id=%s
					""",
					(user_id,)
				)
				team_exists = curs.rowcount > 0
				if not team_exists:
					return {}, True, False, False

				# make dictionary of team ids
				fantasy_team_ids = {}
				rows = curs.fetchall()
				for row in rows:
					team_name = row[0]
					player_ids = row[1:]
					fantasy_team_ids[team_name] = player_ids

				# look up players stats for each fantasy team
				this_week_year, this_week_week = year, week
				prev_week_year = year     if week > 0 else year - 1
				prev_week_week = week - 1 if week > 0 else 14
				fantasy_teams = defaultdict(dict)
				for team_name, player_ids in fantasy_team_ids.items():
					for player_id, role in zip(player_ids, TEAM_ROLES):
						player_stats = []  # default to no stats
						if player_id:
							curs.execute(
								"""
								SELECT player_info.player_id, player_name, position, receptions, total_yards, touchdowns, turnovers_lost, sacks, tackles_for_loss, interceptions, fumbles_recovered, punting_yards, fg_percentage, injury_status, college_name, ROUND(actual_score::numeric, 2)::float AS actual_score,
									COALESCE (ROUND(projected_score::numeric, 2)::float, 0.0) AS projected_score
								FROM
									(SELECT player_id, player_name, position, receptions, total_yards, touchdowns, turnovers_lost, sacks, tackles_for_loss, interceptions, fumbles_recovered, punting_yards, fg_percentage, injury_status, college_name,
									(%s*receptions + %s*total_yards + %s*touchdowns + %s*turnovers_lost + %s*sacks + %s*tackles_for_loss + %s*interceptions + %s*fumbles_recovered + %s*punting_yards + %s*fg_percentage) AS actual_score
									FROM players join colleges
										ON players.college_id=colleges.college_id
									WHERE player_id=%s AND year=%s AND week=%s)
									AS player_info
								LEFT JOIN
									(SELECT player_id, (%s*receptions + %s*total_yards + %s*touchdowns + %s*turnovers_lost + %s*sacks + %s*tackles_for_loss + %s*interceptions + %s*fumbles_recovered + %s*punting_yards + %s*fg_percentage) * (wins::float / (wins::float + ties::float + losses::float)) AS projected_score
									FROM players join colleges
										ON players.college_id=colleges.college_id
									WHERE player_id=%s AND year=%s AND week=%s)
									AS projected_scores
								ON player_info.player_id=projected_scores.player_id
								""",
								(
									receptions_multiplier, total_yards_multiplier, touchdowns_multiplier, turnovers_lost_mulitplier, sacks_multiplier, tackles_for_loss_multiplier, interceptions_multiplier, fumbles_recovered_multiplier, punting_yards_multiplier, fg_percentage_multiplier,
									player_id, this_week_year, this_week_week,
									receptions_multiplier, total_yards_multiplier, touchdowns_multiplier, turnovers_lost_mulitplier, sacks_multiplier, tackles_for_loss_multiplier, interceptions_multiplier, fumbles_recovered_multiplier, punting_yards_multiplier, fg_percentage_multiplier,
									player_id, prev_week_year, prev_week_week
								)
							)
							player_stats = curs.fetchone()
						fantasy_teams[team_name][role] = player_stats

		return fantasy_teams, True, True, False

	def set_player_in_fantasy_team(self, player_name: str, player_position: str, team_role: str, team_name: str, username: str) -> Tuple[bool, bool, bool, bool, bool]:
		"""returns add_player_successful, user_exists, team_exists, player_exists, valid_role, error"""

		with psycopg.connect(f'dbname={self.db_name} user={self.db_username} password={self.db_password}') as conn:
			with conn.cursor() as curs:
				# check if user exists
				curs.execute("SELECT * FROM users WHERE username=%s", (username,))
				user_exists = curs.rowcount > 0
				if not user_exists:
					return False, False, False, False, False, False

				# get user id
				user_info = curs.fetchone()
				user_id = int(user_info[0])

				# make sure team exists
				curs.execute("SELECT * FROM fantasy_teams WHERE team_name=%s AND user_id=%s",
					(team_name, user_id))
				team_exists = curs.rowcount > 0
				if not team_exists:
					return False, True, False, False, False, False

				# get player id
				curs.execute("SELECT DISTINCT player_id FROM players WHERE player_name=%s AND position=%s",
					(player_name, player_position))
				player_exists = curs.rowcount > 0
				if not player_exists:
					return False, True, True, False, False, False
				player_data = curs.fetchone()
				player_id = player_data[0]

				if team_role not in TEAM_ROLES:
					return False, True, True, True, False, False

				# add player to team
				curs.execute(f"UPDATE fantasy_teams SET {team_role}_id=%s WHERE team_name=%s AND user_id=%s;",
					(player_id, team_name, user_id))
				conn.commit()
				return True, True, True, True, True, False

	def clear_role_in_fantasy_team(self, team_role: str, team_name: str, username: str) -> Tuple[bool, bool, bool, bool, bool]:
		"""returns clear_role_successful, user_exists, team_exists, valid_role, error"""

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
				
				if team_role not in TEAM_ROLES:
					return False, True, True, False, False

				# remove player from team
				curs.execute(f"UPDATE fantasy_teams SET {team_role}_id=null WHERE team_name=%s AND user_id=%s;",
					(team_name, user_id))
				conn.commit()
				return True, True, True, True, False

	def get_players_available_to_team(self, team_name: str, username: str, team_role: str, year:int, week: int, count: int,
			receptions_multiplier: float, total_yards_multiplier: float, touchdowns_multiplier: float, turnovers_lost_mulitplier: float, sacks_multiplier: float, tackles_for_loss_multiplier: float, interceptions_multiplier: float, fumbles_recovered_multiplier: float, punting_yards_multiplier: float, fg_percentage_multiplier: float
		) -> Tuple[List[Dict], bool, bool, bool]:
		"""returns players_available_to_team, user_exists, team_exists, valid_role, error"""

		with psycopg.connect(f'dbname={self.db_name} user={self.db_username} password={self.db_password}') as conn:
			with conn.cursor() as curs:
				# check if user exists
				curs.execute("SELECT * FROM users WHERE username=%s", (username,))
				user_exists = curs.rowcount > 0
				if not user_exists:
					return [], False, False, False, False

				# get user id
				user_info = curs.fetchone()
				user_id = int(user_info[0])

				# get team roster
				curs.execute(
					"""
					SELECT
						qb_id, rb_id, wr1_id, wr2_id, te_id, flex_id, center_id, lg_id, rg_id, punter_id, de1_id, de2_id, dt1_id, dt2_id, lb1_id, lb2_id, lb3_id, cb1_id, cb2_id, s1_id, s2_id, kicker_id
					FROM fantasy_teams
					WHERE team_name=%s AND user_id=%s
					""",
					(team_name, user_id)
				)
				team_exists = curs.rowcount > 0
				if not team_exists:
					return [], True, False, False, False

				team_player_ids = set(curs.fetchone()) - set((None,))

				if team_role not in ROLE_TO_POSITIONS:
					return [], True, True, False, False

				positions = ROLE_TO_POSITIONS[team_role]
				str_positions = (f"'{position}'" for position in positions)
				joined_positions = ', '.join(str_positions)
				positions_str = f'({joined_positions})'

				str_team_player_ids = (f"'{team_player_id}'" for team_player_id in team_player_ids)
				joined_team_player_ids = ', '.join(str_team_player_ids)
				team_player_ids_str = f'({joined_team_player_ids})'

				# look up players stats for year and week
				this_week_year, this_week_week = year, week
				prev_week_year = year     if week > 0 else year - 1
				prev_week_week = week - 1 if week > 0 else 14
				curs.execute(
					f"""
					SELECT player_info.player_id, player_name, position, receptions, total_yards, touchdowns, turnovers_lost, sacks, tackles_for_loss, interceptions, fumbles_recovered, punting_yards, fg_percentage, injury_status, college_name, ROUND(actual_score::numeric, 2)::float AS actual_score,
						COALESCE (ROUND(projected_score::numeric, 2)::float, 0.0) AS projected_score
					FROM
						(SELECT player_id, player_name, position, receptions, total_yards, touchdowns, turnovers_lost, sacks, tackles_for_loss, interceptions, fumbles_recovered, punting_yards, fg_percentage, injury_status, college_name,
						(%s*receptions + %s*total_yards + %s*touchdowns + %s*turnovers_lost + %s*sacks + %s*tackles_for_loss + %s*interceptions + %s*fumbles_recovered + %s*punting_yards + %s*fg_percentage) AS actual_score
						FROM players join colleges
							ON players.college_id=colleges.college_id
						WHERE position IN {positions_str} AND year=%s AND week=%s)
						AS player_info
					LEFT JOIN
						(SELECT player_id, (%s*receptions + %s*total_yards + %s*touchdowns + %s*turnovers_lost + %s*sacks + %s*tackles_for_loss + %s*interceptions + %s*fumbles_recovered + %s*punting_yards + %s*fg_percentage) * (wins::float / (wins::float + ties::float + losses::float)) AS projected_score
						FROM players join colleges
							ON players.college_id=colleges.college_id
						WHERE position IN {positions_str} AND year=%s AND week=%s)
						AS projected_scores
					ON player_info.player_id=projected_scores.player_id
					WHERE player_info.player_id NOT IN {team_player_ids_str}
					ORDER BY projected_score DESC
					LIMIT {count if count >= 0 else 'ALL'}
					""",
					(
						receptions_multiplier, total_yards_multiplier, touchdowns_multiplier, turnovers_lost_mulitplier, sacks_multiplier, tackles_for_loss_multiplier, interceptions_multiplier, fumbles_recovered_multiplier, punting_yards_multiplier, fg_percentage_multiplier,
						this_week_year, this_week_week,
						receptions_multiplier, total_yards_multiplier, touchdowns_multiplier, turnovers_lost_mulitplier, sacks_multiplier, tackles_for_loss_multiplier, interceptions_multiplier, fumbles_recovered_multiplier, punting_yards_multiplier, fg_percentage_multiplier,
						prev_week_year, prev_week_week,
					)
				)
				players_available_to_team = curs.fetchall()

		return players_available_to_team, True, True, True, False
