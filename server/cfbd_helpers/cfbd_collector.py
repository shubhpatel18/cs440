from collections import defaultdict

from cfbd_helpers import CFBDScraper

# used to translate stat names from the API to stat names for our database
_stat_translation_dict = {
	# yards
	'kickReturnsYDS':'total_yards',
	'receivingYDS':'total_yards',
	'rushingYDS':'total_yards',
	'passingYDS':'total_yards',
	'puntReturnsYDS':'total_yards',
	'interceptionsYDS':'total_yards',

	# touchdowns
	'passingTD':'touchdowns',
	'rushingTD':'touchdowns',
	'receivingTD':'touchdowns',
	'defensiveTD':'touchdowns',
	'kickReturnsTD':'touchdowns',
	'puntReturnsTD':'touchdowns',
	'interceptionsTD':'touchdowns',

	# turnovers
	'fumblesLOST':'turnovers_lost',
	'passingINT':'turnovers_lost',

	# misc
	'receivingREC':'receptions',
	'defensiveSACKS':'sacks',
	'defensiveTFL':'tackles_for_loss',
	'interceptionsINT':'interceptions',
	'fumblesREC':'fumbles_recovered',
	'puntingYDS':'punting_yards',
	'kickingPCT':'fg_percentage',
	# TODO: should we add kickingXPM?
	'':'injury_status' # TODO:
}

def _player_dict():
	"""create default player dict"""
	return {
		# required fields (no defaults)
		'id': None,
		'name': None,
		'position': None,
		'college_id': None,
		
		# optional fields (defaults)
		'total_yards': 0,
		'touchdowns': 0,
		'turnovers_lost': 0,
		'receptions': 0,
		'sacks': 0,
		'tackles_for_loss': 0,
		'interceptions': 0,
		'fumbles_recovered': 0,
		'punting_yards': 0,
		'fg_percentage': 0,
		'injury_status': 'Healthy'
	}

class CFBDCollector:
	def __init__(self, apikey):
		self.scraper = CFBDScraper(apikey)

	def get_player_data(self, colleges, year, start_week, end_week):
		# prepare players dictionary
		players_data = defaultdict(_player_dict)

		# populate roster information from each team
		for id, college in colleges:
			for player in self.scraper.get_team_roster(college, year):
				# make sure the minimum identification information is present in the data
				if player.first_name and player.last_name and player.position:
					players_data[player.id]['id'] = player.id
					players_data[player.id]['name'] = f'{player.first_name} {player.last_name}'
					players_data[player.id]['position'] = player.position
					players_data[player.id]['college_id'] = id
					players_data[player.id]['injury_status'] = 'Healthy'

		# populate player stats
		for _, college in colleges:
			for player in self.scraper.get_player_stats(college, year, start_week, end_week):
				stat = f'{player.category}{player.stat_type}'

				# keep stats we care about
				if stat in _stat_translation_dict:
					player_stat = _stat_translation_dict[stat]

					# make sure the player's id is in the roster
					if player.player_id in players_data:
						players_data[player.player_id][player_stat] += player.stat
					# Team stats are expected not to be in the roster
					elif player.player != ' Team':
						print(f'year: {year}, start_week: {start_week}, end_week: {end_week}')
						print(player)  # print the data of players who are not in the roster

		return players_data
