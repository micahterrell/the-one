import scenarioGenerationStrings

def generateScenario(pedestrians, vehicles, drones):
	writeString = ""
	scenarioName = "disaster_scenario_p" + str(pedestrians) + "_v" + str(vehicles) + "_d" + str(drones)
	f = open("generated_scenario_" + scenarioName + ".txt", "w")

	writeString = writeString + scenarioGenerationStrings.firstStringPreScenarioName
	writeString = writeString + scenarioName + "\n"
	writeString = writeString + scenarioGenerationStrings.firstStringPostScenarioName
	writeString = writeString + str(pedestrians) + "\n"
	writeString = writeString + scenarioGenerationStrings.secondString
	writeString = writeString + str(vehicles) + "\n"
	writeString = writeString + scenarioGenerationStrings.thirdString
	writeString = writeString + str(pedestrians) + "\n"
	writeString = writeString + scenarioGenerationStrings.fourthString

	f.write(writeString)

# scenarioParameters = [
# (50, 125, 125),
# (100, 100, 100),
# (150, 75, 75),
# (200, 50, 50),
# (125, 50, 125),
# (100, 100, 100),
# (75, 150, 75),
# (50, 200, 50),
# (125, 125, 50),
# (100, 100, 100),
# (75, 75, 150),
# (50, 50, 200)
# ]

scenarioParameters = [(100,100,100)]
def generateMultipleRunScenario(params):
	writeString = ""
	f = open("generated_scenario.txt", "w")

	writeString = writeString + scenarioGenerationStrings.firstStringPreScenarioName + "["

	#Write the scenario names
	for i in range(len(params)):
		scenarioName = "d_scenario_p" + str(params[i][0]) + "_v" + str(params[i][1]) + "_d" + str(params[i][2])
		if(i != len(params) - 1):
			scenarioName = scenarioName + ";"

		writeString = writeString + scenarioName

	writeString = writeString + "]\n"
	
	writeString = writeString + scenarioGenerationStrings.firstStringPostScenarioName

	#Write the pedestrians
	writeString = writeString + "["
	for i in range(len(params)):
		writeString = writeString + str(params[i][0])
		if(i != len(params) - 1):
			writeString = writeString + ";"

	writeString = writeString + "]\n"

	writeString = writeString + scenarioGenerationStrings.secondString

	#Write the vehicles
	writeString = writeString + "["
	for i in range(len(params)):
		writeString = writeString + str(params[i][1])
		if(i != len(params) - 1):
			writeString = writeString + ";"

	writeString = writeString + "]\n"

	writeString = writeString + scenarioGenerationStrings.thirdString

	#Write the drones
	writeString = writeString + "["
	for i in range(len(params)):
		writeString = writeString + str(params[i][2])
		if(i != len(params) - 1):
			writeString = writeString + ";"

	writeString = writeString + "]\n"

	writeString = writeString + scenarioGenerationStrings.fourthString

	f.write(writeString)
	f.close()

generateMultipleRunScenario(scenarioParameters)