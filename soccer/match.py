class Match(object):

	def __init__(self, team_1, team_2, score):
		self.team_1 = team_1
		self.team_2 = team_2
		self.score = score




	def register_score(self):
		self.score = [0, 0]
		goals = int(input("how many goals did {} score?: ".format(self.team_1.name)))
		print(goals)
		self.score[0] = goals
		self.team_1.goals += goals
		while (goals > 0):
			player_name = input("Enter the name of the scorer: ")
			for player in self.team_1.players:
				if player_name.lower() == player.name.lower():
					player_goals = int(input("how many goals did the player score?: "))
					player.goals += player_goals
					goals -= player_goals
					
		goals = int(input("how many goals did {} score?: ".format(self.team_2.name)))
		self.score[1] = goals
		self.team_2.goals += goals
		while (goals > 0):
			player_name = input("Enter the name of the scorer: ")
			for player in self.team_2.players:
				if player_name.lower() == player.name.lower():
					player_goals = int(input("how many goals did the player score?: "))
					player.goals += player_goals
					goals -= player_goals

		if (self.score[0] > self.score[1]):
			self.team_1.points += 3
		if (self.score[0] < self.score[1]):
			self.team_2.points += 3
		else:
			self.team_1.points += 1
			self.team_2.points += 1
