import pandas as pd
import numpy as np
import os

# read in actual scores
game_results = pd.read_table("Actual Scores.tsv")
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
prediction_reader(player = "Alex", prediction_file = "Alex Leitao.tsv")
prediction_reader(player = "Alfonso", prediction_file = "Alfonso Martinez-Arias.tsv")
prediction_reader(player = "Amir", prediction_file = "Amir Daniel Hay.tsv")
prediction_reader(player = "Anne", prediction_file = "Anne Ferguson-Smith.tsv")
prediction_reader(player = "Arun", prediction_file = "Arunkumar Ramesh.tsv")
prediction_reader(player = "Aylwyn", prediction_file = "Aylwyn Scally.tsv")
prediction_reader(player = "Casper", prediction_file = "Casper Lumby.tsv")
prediction_reader(player = "Chris", prediction_file = "Chris Lilley.tsv")
prediction_reader(player = "Daniel F", prediction_file = "Daniel Fabian.tsv")
prediction_reader(player = "Daniel J", prediction_file = "Daniel Jordan.tsv")
prediction_reader(player = "Felipe", prediction_file = "Felipe Karam Teixeira.tsv")
prediction_reader(player = "Frank", prediction_file = "Frank Jiggins.tsv")
prediction_reader(player = "Gaspar", prediction_file = "Gaspar Bruner.tsv")
prediction_reader(player = "Helena", prediction_file = "Helena Valle.tsv")
prediction_reader(player = "Hui", prediction_file = "Hui Shi.tsv")
prediction_reader(player = "Jon", prediction_file = "Jon Day.tsv")
prediction_reader(player = "Juanjo", prediction_file = "Juanjo Perez-Moreno.tsv")
prediction_reader(player = "Mitsu", prediction_file = "Mitsu Ito.tsv")
prediction_reader(player = "Osama", prediction_file = "Osama Brosh.tsv")
prediction_reader(player = "Roberto", prediction_file = "Roberto Bandiera.tsv")
prediction_reader(player = "Sam", prediction_file = "Samuel Lewis.tsv")
prediction_reader(player = "Steve", prediction_file = "Steve Russell.tsv")
prediction_reader(player = "Sylvain", prediction_file = "Sylvain Delaunay.tsv")
prediction_reader(player = "Tariq", prediction_file = "Tariq Desai.tsv")

# make leaderboard
leaderboard = pd.DataFrame()
leaderboard["Player"] = names
leaderboard["Score"] = scores
# sort leaderboard in descending order
leaderboard.sort_values(by="Score", ascending=False, inplace=True)
# extract players and scores to new lists
players_sorted = list(leaderboard["Player"])
scores_sorted = list(leaderboard["Score"])
# add new column for position (to account for joint positions)
current_position = 1
current_score = scores_sorted[0]
positions = []
for i in scores_sorted:
	if i < current_score:
		current_score = i
		current_position += 1
	positions.append(current_position)

# write leaderboard in readme format
leaderboard_readme_format = "# World Cup 2018\nPosition | Player | Points\n---------|------|-------\n"
for i in range(len(players_sorted)):
	leaderboard_readme_format += str(positions[i]) + "|" + players_sorted[i] + "|" + str(scores_sorted[i]) + "\n"
readme_output = open("README.md", "wt")
readme_output.write(leaderboard_readme_format)
readme_output.close()
print("Leaderboard updated")

