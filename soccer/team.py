class Team(object):


	def __init__(self, name, players, balance, goals, points):
		self.name = name
		self.players = players
		self.balance = balance
		self.goals = goals
		self.points = points


	def update_goals(self):
		goals = 0
		for player in self.players:
			goals += player.goals

		self.goals = goals



