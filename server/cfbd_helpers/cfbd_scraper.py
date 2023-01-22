import cfbd
from cfbd.rest import ApiException

class CFBDScraper:
	def __init__(self, apikey: str):
		configuration = cfbd.Configuration()
		configuration.api_key['Authorization'] = apikey
		configuration.api_key_prefix['Authorization'] = 'Bearer'

		self.teams_api = cfbd.TeamsApi(cfbd.ApiClient(configuration))
		self.players_api = cfbd.PlayersApi(cfbd.ApiClient(configuration))

	def get_team_roster(self, team, year):
		try:
			response = self.teams_api.get_roster(
				year=year,
				team=team
			)
			return response
		except ApiException as e:
			print("Exception when calling TeamsApi->get_roster: %s\n" % e)

	def get_player_stats(self, team, year, start_week, end_week):
		try:
			response = self.players_api.get_player_season_stats(
				year=year,
				team=team,
				start_week=start_week,
				end_week=end_week,
			)
			return response
		except ApiException as e:
			print("Exception when calling PlayersApi->get_player_season_stats: %s\n" % e)
