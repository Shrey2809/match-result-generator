from random import seed
from random import randint

def main():
	seed()
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
	teamA = input("Enter team 1's name: ")
	while (teamA not in (teams)):
		teamA = input("Invalid entry: re-enter team name: ")
	teamAScore = teamRatings[teamA]
	teamB = input("Enter team 2's name: ")
	while (teamB not in (teams)):
		teamB = input("Invalid entry: re-enter team name: ")
	teamBScore = teamRatings[teamB]
	simulationNumber = int (input("Input a number of games you want to simulate: "))
	thousandSimulation(teamA, teamB, teamAScore, teamBScore, simulationNumber)

	input ("Program ending...")


def thousandSimulation(teamA, teamB, teamAScore, teamBScore, simulationNumber):
	winCounter = [0,0];
	i = 0
	while (i < simulationNumber):
		singleGame(teamA, teamB, teamAScore, teamBScore, winCounter)
		i+=1

	print ("After ", simulationNumber, "simulations:")
	print ("Probability of ", teamA, "winning: ", (winCounter[0]/simulationNumber)*100, "%\n")
	print ("Probability of ", teamB, "winning: ", (winCounter[1]/simulationNumber)*100, "%\n")


def singleGame(teamA, teamB, teamAScore, teamBScore, winCounter):
	rndCountA = 0;
	rndCountB = 0;

	maxRounds = 12;
	maxRoundsOnOT = 15;
	roundCount = 1;
	otTrigger = False	
	
	mergedScore = teamAScore + teamBScore 
	while (roundCount <= maxRounds and rndCountB < 7 and rndCountA < 7):
		value  = randint (1, mergedScore);
		if (value >= 1 and value <= teamAScore):
			rndCountA += 1;
		elif (value > teamAScore and value <= mergedScore) :
			rndCountB += 1;
		roundCount += 1;

		if (rndCountB == 6 and rndCountA == 6):
			otTrigger = True;

 	# This is for if both teams have 6-6 at the end of regulation, 3 more rounds of OT can be simulated
	if otTrigger:
		while (roundCount <= maxRoundsOnOT and rndCountB < 8 and rndCountA < 8):
			value  = randint (1, mergedScore);
			if (value >= 1 and value <= teamAScore):
				rndCountA += 1;
			elif (value > teamAScore and value <= mergedScore) :
				rndCountB += 1;
			roundCount += 1;


	if rndCountA > rndCountB:
		#print ("Match won by: ", teamA, ": ", rndCountA, " - ", rndCountB)
		winCounter[0] += 1;
	else:
		#print ("Match won by: ", teamB, ": ", rndCountB, " - ", rndCountA)
		winCounter[1] += 1;

if __name__ == '__main__':
	main()
