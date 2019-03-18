import random
from team import Team
from player import Player
from match import Match

## C:\Users\Eduardo\Desktop\soccer\main.py


tournament_type = "None"
#Unpackaging tournament type
with open("/Users/Eduardo/Desktop/soccer/type.txt") as tournament_type_file:
	for line in tournament_type_file:
		if len(line) > 1:
			tournament_type = line



#Unpackaging teams from teams.txt
teams = []
with open("/Users/Eduardo/Desktop/soccer/teams.txt") as teams_f:
	for line in teams_f:
		if len(line) > 1:
			info = line.split(',')
			teams.append(Team(info[0], [], float(info[1]), int(info[2]), int(info[3])))


#Unpackaging players from players.txt
with open("/Users/Eduardo/Desktop/soccer/players.txt") as players_f:
	for line in players_f:
		if len(line) > 1:
			players = line.split(';')
			for team in teams:		
				if (team.name.lower() == players[0].lower()):
					players.pop(0)
					for items in players:
						player_info = items.split(',')
						if len(player_info) == 3:	
							team.players.append(Player(player_info[0], player_info[1], int(player_info[2])))


#Unpackaging matches from matches.txt
matches = []
with open("/Users/Eduardo/Desktop/soccer/matches.txt") as matches_f:
	for line in matches_f:
		if len(line) > 1:
			info = line.split(',')

			
			for team in teams:
				if (team.name.lower() == info[0].lower()):
					team_1 = team
				if (team.name.lower() == info[1].lower()):
					team_2 = team



			if len(info) == 4:
				matches.append(Match(team_1, team_2, None))

			else:

				matches.append(Match(team_1, team_2, [int(info[2]), int(info[3])]))


#Unpackaging schedual from schedual.txt
schedual = []

with open("/Users/Eduardo/Desktop/soccer/schedual.txt") as schedual_f:
	for line in schedual_f:
		if len(line) > 1:
			info = line.split(',')

			for match in unplayed_matches:
				if match.team_1.name.lower() == info[0].lower() and match.team_2.name.lower == info[1].lower():
					schedual.append(match)



#clasifying matches between played and unplayed
played_matches = []
unplayed_matches = []

for match in matches:
	if (match.score == None):
		unplayed_matches.append(match)
	else:
		played_matches.append(match)






#menu of all the posible operations
def menu(schedual):

	exit = False
	while (exit == False):
		print(tournament_type)

		print("Which operation do you wish to perform?")
		print("1: Register team")
		print("2: Register player")
		print("3: Update balance")
		print("4: Visualize teams´ statistics")
		print("5: Visualize matches schedual")
		print("6: Visualize team players")
		print("7: Create tournament")
		print("8: Visualize team leaderBoard")
		print("9: Visualize player leaderBoard")
		print("10: Register match score")
		print("11: Exit")
		answer = int(input())

		if (answer == 1):
			register_team()

		elif (answer == 2):
			team_name = input("What team does it belongs to: ")
			for team in teams:
				if team.name.lower() == team_name.lower():
					register_player(team)

		elif (answer == 3):
			team_name = input("Enter the team name that you want to modify: ")
			for team in teams:
				if team.name.lower() == team_name.lower():
					update_balance(team)

		elif (answer == 4):
			display_teams(teams)

		elif (answer == 5):
			print(tournament_type)
			if tournament_type == None:
				print("hi")
				create_tournament(teams, matches)
				print(unplayed_matches)

			if (len(schedual) == 0):
				print("hi joe")
				schedual = create_schedual(unplayed_matches, tournament_type)
				print("hi joe")
				print(schedual)
				display_schedual(schedual)

			else:
				display_schedual(schedual)



		elif (answer == 6):
			team_name = input("Which team´s players do you want to Visualize? ")
			for team in teams:
				if team.name.lower() == team_name.lower():
					display_team_players(team)

		elif (answer == 7):
			create_tournament(teams, matches)

		elif (answer == 8):
			display_leaderboard(teams)

		elif (answer == 9):
			display_player_leaderboard(players)

		elif (answer == 10):
			all_games_played = True
			for match in schedual:
				if match.score == None:
					all_games_played = False


			if all_games_played == True:
				create_schedual(unplayed_matches, tournament_type)

			else:
				display_schedual(schedual)
				index = int(input("Enter the number of the match you want to register: "))
				schedual[index - 1].register_score()

			refresh()





		elif (answer == 11):
			backup()
			exit = True




#team registration function
def register_team():
	team_name = input("Enter the name of the team to be registered: ")
	balance = input("Enter the initial balance of the team: ")
	teams.append(Team(team_name, [], float(balance), 0, 0))

	amt = int(input("How many players do you want to register?: "))

	for i in range(amt):
		register_player(teams[len(teams) - 1])

#player registration function
def register_player(team): 
	player_name = input("Enter the player name: ")
	number = int(input("Enter the player number: "))
	team.players.append(Player(player_name, number, 0))


#balance update function, withwdrawal and deposit
def update_balance(team):
	exit = False
	while (exit == False):
		print("{} current balance: {}".format(team.name, team.balance))
		print("Which operation do you wish to perform?")
		print("1: Withwdrawal")
		print("2: Deposit")
		print("3: Exit")
		answer = int(input())
		if (answer == 1):
			print("Enter amount to withwdrawal")
			amt = float(input())
			team.balance -= amt
			print("{} new balance: {}".format(team.name, team.balance))

		elif (answer == 2):
			print("Enter amount to deposit")
			amt = float(input())
			team.balance += amt
			print("{} new balance: {}".format(team.name, team.balance))
		elif (answer == 3):
			exit = True


#print function to display teams, name, goals, balance
def display_teams(teams):
	for team in teams:
		print("team: {} goals: {} balance: {}".format(team.name, team.goals, team.balance))


	

#print function to display players of a team, name, number and goals
def display_team_players(team):
	data = []
	for player in team.players:
		print("player: {} number: {} goals: {}".format(player.name, player.number, player.goals))



#back up function to save all the operations done after the exit is selected
def backup():
	with open("/Users/Eduardo/Desktop/soccer/players.txt", 'w') as players_file:
		for team in teams:
			info = team.name + ';'
			for player in team.players:
				info = info + player.name + ',' + str(player.number) + ',' + str(player.goals) + ';'

			info = info + '\n'

			players_file.write(info)

	with open("/Users/Eduardo/Desktop/soccer/teams.txt", 'w') as teams_file:
		for team in teams:
			info = team.name + ',' + str(team.balance) + ',' + str(team.goals) + ',' + str(team.points) + ',' + '\n'

			teams_file.write(info)


	with open("/Users/Eduardo/Desktop/soccer/matches.txt", 'w') as matches_file:
		for match in matches:
			if match.score != None:
				info = match.team_1.name + ',' + match.team_2.name + ',' + str(match.score[0]) + ',' + str(match.score[1]) + ',' + '\n'
			else:
				info = match.team_1.name + ',' + match.team_2.name + ',' + 'None' + ',' + '\n'

			matches_file.write(info)

	with open("/Users/Eduardo/Desktop/soccer/tournament type.txt", 'w') as tournament_type_file:
			tournament_type_file.write(tournament_type)

#tournament creation function, all posible matches
def create_tournament(teams, matches):

	print("what type of tournament do you want to create?")
	print("1: Round robin")
	print("2: Double Round Robin")
	print("3: Exit")
	answer = int(input("type: "))

	if (answer == 1):
		for i in range(len(teams) - 1):
			for k in range(i + 1, len(teams)):
				matches.append(Match(teams[i], teams[k], None))

		global tournament_type
		tournament_type = "rr"
		with open("/Users/Eduardo/Desktop/soccer/tournament type.txt", 'w') as tournament_type_file:
			tournament_type_file.write(tournament_type)


	if (answer == 2):
		for i in range(len(teams) - 1):
			for k in range(i + 1, len(teams)):
				matches.append(Match(teams[i], teams[k], None))
				matches.append(Match(teams[k], teams[i], None))

		tournament_type = 'drr'
		with open("/Users/Eduardo/Desktop/soccer/tournament type.txt", 'w') as tournament_type_file:
			tournament_type_file.write(tournament_type)


	refresh()

#schedual creation function, the matches that correspond to a specific day
def create_schedual(unplayed_matches, tournament_type):
	#round robin tournament
	teams_dict = {}
	for team in teams:
		teams_dict.update({team.name.lower(): False})


	c_schedual = []
	if (tournament_type == 'rr'):
		games = 0
		while games < (len(teams) / 2):
			for match in unplayed_matches:
				if (teams_dict[match.team_1.name.lower()] == False and teams_dict[match.team_2.name.lower()] == False):
					c_schedual.append(match)
					teams_dict[match.team_1.name] = True
					teams_dict[match.team_2.name] = True
					games += 1

		return c_schedual		

	#other type of tournament
	elif (create_tournament == 2):
		pass

#print function to displays the currect schedual
def display_schedual(schedual):
	i = 1
	for match in schedual:
		print("{}. {} vs {} result: {}".format(i,match.team_1.name, match.team_2.name, match.score))
		i += 1


#print function that displays the current team leaderboard
def display_leaderboard(teams):
	teams_list = teams

	for i in range(len(teams) - 1):
		for j in range(len(teams) - i - 1):
			if teams_list[j].points > teams_list[j + 1].points:
				temporal = teams_list[j]
				teams_list[j] = teams_list[j + 1]
				teams_list[j + 1] = temporal
	
	j = 1
	for i in range(len(teams) -1, -1, -1):
		print("{}, team: {} points: {} goals: {}".format(j, teams_list[i].name, teams_list[i].points, teams_list[i].goals))
		j += 1



	
#print function that displays the currect player leaderboard
def display_player_leaderboard(teams):
	players_list = []
	for team in teams:
		for player in team.players:
			players.append(player)

	for i in range(len(player_list) - 1):
		for j in range(len(players_list) - i - 1):
			if players_list[j].goals > players_list[j + 1].goals:
				temporal = players_list[j]
				players_list[j] = players_list[j + 1]
				players_list[j + 1] = temporal

	j = 1
	for i in range(len(players_list) -1, -1, -1):
		print("{}, {} goals: {}".format(j, players_list[i].name, players_list[i].goals))
		j += 1


def refresh():
	for match in matches:
		if (match.score == None):
			unplayed_matches.append(match)
		else:
			played_matches.append(match)

	backup()


menu(schedual)

#el parametro n es solo cuantos terminos de la serie quieres calcular
