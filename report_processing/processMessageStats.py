from os import listdir
from os.path import isfile, join

def processMessageStats(directoryPath):
	stats = []
	files = [f for f in listdir(directoryPath) if isfile(join(directoryPath, f))]
	for file in files:
		if("MessageStatsReport" in file):
			f = open(directoryPath + file, "r")
			lines = f.readlines()
			successRate = float(lines[9].split(": ")[1].strip())

			percentages = getClassPercentages(file)

			stats.append(percentages + (successRate,))
			f.close()
	return stats

def exportMessageStats(stats, name):
	f = open(name + "_stats.csv", "w")
	for stat in stats:
		f.write(str(stat[1]) + "," + str(stat[2]) + "," + str(stat[3]) + "," + str(stat[4]) + "\n")
	f.close()


def getClassPercentages(reportName):
	splitReportName = reportName.split("_")
	total = int(splitReportName[2][1:]) + int(splitReportName[3][1:]) + int(splitReportName[4][1:])
	return (total, int(splitReportName[2][1:]) / total, int(splitReportName[3][1:]) / total, int(splitReportName[4][1:]) / total)

emergencyPath = "../reports/functionOfEmergency/"
pedestrianPath = "../reports/functionOfPedestrians/"
dronePath = "../reports/functionOfDrones/"

exportMessageStats(processMessageStats(emergencyPath), "emergency")
exportMessageStats(processMessageStats(pedestrianPath), "pedestrians")
exportMessageStats(processMessageStats(dronePath), "drone")