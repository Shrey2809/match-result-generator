#--------------------------------------------------------------------------------------------
# Round-by-round win/loss predictor program
# Developed by: Shrey Mandol
#
# Description: 
# The idea is it simulates a game of Rainbow Six
# You give it two team names and a number associated with each team
# The program then generates a random number between 1 and the sum of the two team numbers
# and that dictates the winner of a specific round
# Then it repeats until a team has 7 rounds (or 8 depending on if score becomes 6-6)
#
# Sample Run:
# so if you give it SSG-5 and Empire-8, it would generate a number from 1-13, 
# where 1-5 means SSG win the round, and 6-13 mean Empire win the round
# --------------------------------------------------------------------------------------------

# Import statements
from random import seed
from random import randint

# Main program
def main() :
	seed()
	endProgram = False
	while (not endProgram):
		matchGenerator()
		endProg = input("Generate another game? (Y/N) ")
		if endProg == 'Y' or endProg == 'y':
			endProgram = False;
		else:
			endProgram = True;
	input ("Program ending...")

def matchGenerator():
	teams = ["DZ",
		"ELEVATE",
		"Furia",
		"OXG",
		"Liquid",
		"oNe",
		"CAG",
		"AST",
	    	"XSET",
	    	"W7M",
	    	"Heroic",
	    	"LFO",
	   	"G2",
	    	"DW",
	    	"Chiefs", "BDS"]
	# Change values for team names (in quotes) and skill ratings
	teamRatings = {
		"DZ"       : 2083,
		"ELEVATE"  : 2062,
		"Furia"    : 2013,
		"OXG"      : 2090,
		"Liquid"   : 2110,
		"oNe"      : 2052,
		"CAG"      : 2075,
		"AST"      : 2111,
	    	"XSET"     : 2081,
	    	"W7M"      : 2136,
	    	"Heroic"   : 2150,
	    	"LFO"      : 2064,
	   	"G2"       : 2043,
	    	"DW"       : 2119,
	    	"Chiefs"   : 2041,
		"BDS"      : 2188,
	}

	print ("---------------------------------------")
	print ("|        Match result geneator        |")
	print ("---------------------------------------")
	teamA = input("Enter team 1's name: ")
	while (teamA not in (teams)):
		teamA = input("Invalid entry: re-enter team name: ")
	teamAScore = teamRatings[teamA]
	print ("---------------------------------------")
	teamB = input("Enter team 2's name: ")
	while (teamB not in (teams)):
		teamB = input("Invalid entry: re-enter team name: ")
	teamBScore = teamRatings[teamB]

	regenGame = True

	while (regenGame):
		regenerateMatch(teamA, teamAScore, teamB, teamBScore)
		regGame = input("Generate another match WITH SAME TEAMS AND SCORES? (Y/N) ")
		if regGame == 'Y' or regGame == 'y':
			regenGame = True;
		else:
			regenGame = False;


def regenerateMatch(teamA, teamAScore, teamB, teamBScore):
	rndCountA = 0;
	rndCountB = 0;

	maxRounds = 12;
	maxRoundsOnOT = 15;
	roundCount = 1;
	otTrigger = False	
	
	print ("---------------------------------------")
	stepByStep = input("Go round by round? (Y/N) ")
	mergedScore = teamAScore + teamBScore 

	if stepByStep == 'Y' or stepByStep == 'y':
		stepByStepBool = True;
	else:
		stepByStepBool = False;
	
	print ("---------------------------------------")

	while (roundCount <= maxRounds and rndCountB < 7 and rndCountA < 7):
		
		
		print ("Round ", str(roundCount),": " )

		value  = randint (1, mergedScore);
		if (value >= 1 and value <= teamAScore):
			print ("Round winner: ", teamA)
			rndCountA += 1;
		elif (value > teamAScore and value <= mergedScore) :
			print ("Round winner: ", teamB,)
			rndCountB += 1;

		print ("Current score" , teamA, ": ", str(rndCountA) , " - ", str(rndCountB), " :" , teamB);
		roundCount += 1;

		if (rndCountB == 6 and rndCountA == 6):
			otTrigger = True;

		if stepByStepBool:
			input("Hit enter to generate next round")
		print ("---------------------------------------")


 	# This is for if both teams have 6-6 at the end of regulation, 3 more rounds of OT can be simulated
	if otTrigger:
		print ("Overtime triggered")
		print ("---------------------------------------")
		while (roundCount <= maxRoundsOnOT and rndCountB < 8 and rndCountA < 8):
			
			print ("Round ", str(roundCount),": " )

			value  = randint (1, mergedScore);
			if (value >= 1 and value <= teamAScore):
				print ("Round winner: ", teamA)
				rndCountA += 1;
			elif (value > teamAScore and value <= mergedScore) :
				print ("Round winner: ", teamB,)
				rndCountB += 1;

			print ("Current score ->" , teamA, ": ", str(rndCountA) , " - ", str(rndCountB), " :" , teamB);
			roundCount += 1;

			if stepByStepBool:
				input("Hit enter to generate next round")
			print ("---------------------------------------")


	if rndCountA > rndCountB:
		print ("Match won by: ", teamA, ": ", rndCountA, " - ", rndCountB)
	else:
		print ("Match won by: ", teamB, ": ", rndCountB, " - ", rndCountA)

	print ("---------------------------------------")


if __name__ == '__main__':
	main()
