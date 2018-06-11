import pandas as pd
import numpy as np
import os

# read in actual scores
# add column of team1-team2
# write function to
	# read in player's predictions
	# add player's name to dict as a key, value 0
	# add column of team1-team2
	# for each game
		# compare player's team1-team2 values to actual team1-team2
		# if result called correctly (based on >0, 0 or <0), add 1 to value for that player
		# if score called correctly, add 3 to value for that player
