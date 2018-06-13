import pandas as pd
import numpy as np
import os

# read in actual scores
game_results = pd.read_table("group_stage_scores.tsv")
# add column of team1-team2
game_results["team1-team2"] = game_results["Team 1 score"] - game_results["Team 2 score"]
# extract team1 scores, team2 scores, and team1-team2 column as lists
team1_scores = list(game_results["Team 1 score"])
team2_scores = list(game_results["Team 2 score"])
team_differences = list(game_results["team1-team2"])

# write function to
def prediction_reader(player, prediction_file):
	# set player score to 0
	score = 0
	# read in player's predictions
	predictions = pd.read_table(prediction_file)	
	# add player's name to list
	names.append(player)
	# add column of team1-team2
	predictions["team1-team2"] = list(predictions["Team 1 score"] - predictions["Team 2 score"])
	# extract team1 scores, team2 scores, and team1-team2 column as lists
	predicted_team1_scores = list(predictions["Team 1 score"])
	predicted_team2_scores = list(predictions["Team 2 score"])
	predicted_team_differences = list(predictions["team1-team2"])
	# for each game
	for game in range(len(team_differences)):
		# skip unplayed games
		played = np.isnan(team_differences[game])
		if played == False:
			# compare player's team1-team2 values to actual team1-team2
			# if result called correctly (based on >0, 0 or <0), add 1 to value for that player
			if team_differences[game] > 0 and predicted_team_differences[game] > 0:
				score += 1
			elif team_differences[game] == 0 and predicted_team_differences[game] == 0:
				score += 1
			elif team_differences[game] < 0 and predicted_team_differences[game] < 0:
				score +=1
			# if score called correctly, add 3 to value for that player
			if predicted_team1_scores[game] == team1_scores[game] and predicted_team2_scores[game] == team2_scores[game]:
				score += 3
	# add score to list
	scores.append(score)
	return()

# empty list of player names
names = []
# empty list of player scores
scores = []

# calculate score for each player
prediction_reader(player = "player1", prediction_file = "player1.tsv")
prediction_reader(player = "player2", prediction_file = "player2.tsv")
prediction_reader(player = "player3", prediction_file = "player3.tsv")
print(names)
print(scores)

# make leaderboard
leaderboard = pd.DataFrame()
leaderboard["Player"] = names
leaderboard["Score"] = scores
# sort leaderboard in descending order
leaderboard.sort_values(by="Score", ascending=False, inplace=True)
print(leaderboard)
# extract players and scores to new lists
players_sorted = list(leaderboard["Player"])
scores_sorted = list(leaderboard["Score"])

# write leaderboard in readme format
leaderboard_readme_format = ""

