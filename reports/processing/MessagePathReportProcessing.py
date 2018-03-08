numbers = "0123456789"

def getReportLines(reportPath):
	f = open(reportPath, "r")
	lines = f.readlines()
	f.close()

	# Return the lines without the header
	return lines[1:]


def countDeliveredMessages(lines):
	count = 0
	for line in lines:
		if(wasDelivered(line)):
			count = count + 1
		
	return count

def countTotalMessages(lines):
	messages = {}
	for line in lines:
		messages[line.strip().split(",")[0]] = 1

	return len(messages.keys())

# Counts hops between specific classes, this function assumes that the only numbers in
# class names are the id numbers 
def countHopsByClass(lines):
	# Place the count for each interation in interactions[source][destination]
	interactions = {}

	for line in lines:
		splitLine = line.strip().split(",")
		path = splitLine[3].split(">")

		for i in range(len(path) - 1):
			source = getClass(path[i])
			destination = getClass(path[i + 1])

			if(source in interactions):
				if(destination in interactions[source]):
					interactions[source][destination] += 1
				else:
					interactions[source][destination] = 1
			else:
				interactions[source] = {}
				interactions[source][destination] = 1
	return interactions

def countHopsOfDeliveredMessagesByClass(lines):
	# Place the count for each interation in interactions[source][destination]
	interactions = {}

	for line in lines:
		if(wasDelivered(line)):
			splitLine = line.strip().split(",")
			path = splitLine[3].split(">")

			for i in range(len(path) - 1):
				source = getClass(path[i])
				destination = getClass(path[i + 1])

				if(source in interactions):
					if(destination in interactions[source]):
						interactions[source][destination] += 1
					else:
						interactions[source][destination] = 1
				else:
					interactions[source] = {}
					interactions[source][destination] = 1
	return interactions

def countHopsOfUndeliveredMessagesByClass(lines):
	# Place the count for each interation in interactions[source][destination]
	interactions = {}

	for line in lines:
		if(not wasDelivered(line)):
			splitLine = line.strip().split(",")
			path = splitLine[3].split(">")

			for i in range(len(path) - 1):
				source = getClass(path[i])
				destination = getClass(path[i + 1])

				if(source in interactions):
					if(destination in interactions[source]):
						interactions[source][destination] += 1
					else:
						interactions[source][destination] = 1
				else:
					interactions[source] = {}
					interactions[source][destination] = 1
	return interactions

def countDropsByClass(lines):
	classDrops = {}

	for line in lines:
		if(not wasDelivered(line)):
			splitLine = line.strip().split(",")
			splitPath = splitLine[3].split(">")

			c = getClass(splitPath[len(splitPath) - 1])
			if(c in classDrops):
				classDrops[c] += 1
			else:
				classDrops[c] = 1
	return classDrops


def wasDelivered(messageLine):
	splitLine = messageLine.strip().split(",")
	splitPath = splitLine[3].split(">")
	return splitLine[2] == splitPath[len(splitPath) - 1]

def getClass(nodeName):
	c = ""
	for char in nodeName:
		if(char not in numbers):
			c = c + char
		else:
			return c
	return c

def countSourceDestinationPercentage(lines):
	hopCounts = countHopsByClass(lines)
	pairs = {}

	hops = 0

	for sKey in hopCounts:
		for dKey in hopCounts[sKey]:
			hops += hopCounts[sKey][dKey]
			pairs[sKey + "_" + dKey] = hopCounts[sKey][dKey]

	for key in pairs:
		pairs[key] /= hops

	return pairs

def countDeliveredSourceDestinationPercentage(lines):
	hopCounts = countHopsOfDeliveredMessagesByClass(lines)
	pairs = {}

	hops = 0

	for sKey in hopCounts:
		for dKey in hopCounts[sKey]:
			hops += hopCounts[sKey][dKey]
			pairs[sKey + "_" + dKey] = hopCounts[sKey][dKey]

	for key in pairs:
		pairs[key] /= hops

	return pairs

def countUndeliveredSourceDestinationPercentage(lines):
	hopCounts = countHopsOfUndeliveredMessagesByClass(lines)
	pairs = {}

	hops = 0

	for sKey in hopCounts:
		for dKey in hopCounts[sKey]:
			hops += hopCounts[sKey][dKey]
			pairs[sKey + "_" + dKey] = hopCounts[sKey][dKey]

	for key in pairs:
		pairs[key] /= hops

	return pairs

def processReport(path):
	lines = getReportLines(path)

	totalPairPercentages = countSourceDestinationPercentage(lines)
	undeliveredPairPercentages = countUndeliveredSourceDestinationPercentage(lines) 
	deliveredPairPercentages = countDeliveredSourceDestinationPercentage(lines)

	tppKeys = sorted(totalPairPercentages.keys())
	uppKeys = sorted(undeliveredPairPercentages.keys())
	dppKeys = sorted(deliveredPairPercentages.keys())

	tppHeader = ""
	tppData = ""
	uppHeader = ""
	uppData = ""
	dppHeader = ""
	dppData = ""

	for i in range(len(tppKeys)):
		tppHeader += tppKeys[i]
		tppData += str(totalPairPercentages[tppKeys[i]])
		if(i + 1 != len(tppKeys)):
			tppHeader += ","
			tppData += ","
		else:
			tppHeader += "\n"
			tppData += "\n"

	for i in range(len(uppKeys)):
		uppHeader += uppKeys[i]
		uppData += str(undeliveredPairPercentages[uppKeys[i]])
		if(i + 1 != len(uppKeys)):
			uppHeader += ","
			uppData += ","
		else:
			uppHeader += "\n"
			uppData += "\n"

	for i in range(len(dppKeys)):
		dppHeader += dppKeys[i]
		dppData += str(deliveredPairPercentages[dppKeys[i]])
		if(i + 1 != len(dppKeys)):
			dppHeader += ","
			dppData += ","
		else:
			dppHeader += "\n"
			dppData += "\n"

	f = open("ProcessedMessagePathReport.csv", "w")
	f.write(tppHeader + tppData)
	f.write(uppHeader + uppData)
	f.write(dppHeader + dppData)
	f.close()

def getReportLines(reportPath):
	f = open(reportPath, "r")
	lines = f.readlines()
	f.close()

	# Return the lines without the header
	return lines[1:]


def countDeliveredMessages(lines):
	count = 0
	for line in lines:
		if(wasDelivered(line)):
			count = count + 1
		
	return count

def countTotalMessages(lines):
	messages = {}
	for line in lines:
		messages[line.strip().split(",")[0]] = 1

	return len(messages.keys())

lines = getReportLines("../d_scenario_p100_v100_d100_MessagePathReport.txt")

#processReport("../d_scenario_p100_v100_d100_MessagePathReport.txt")

totalMessages = countTotalMessages(lines)
deliveredMessages = countDeliveredMessages(lines)
droppedMessages = totalMessages - deliveredMessages

print("Delivered: " + str(deliveredMessages) + " Dropped: " + str(droppedMessages) + " Total: " + str(totalMessages))
print(deliveredMessages / totalMessages)

# hopCounts = countHopsByClass(lines)
# print(hopCounts)

# hops = 0

# for sKey in hopCounts:
# 	for dKey in hopCounts[sKey]:
# 		hops += hopCounts[sKey][dKey]

# print(hops)

# deliveredHopCounts = countHopsOfDeliveredMessagesByClass(lines)
# print(deliveredHopCounts)

# deliveredHops = 0

# for sKey in deliveredHopCounts:
# 	for dKey in deliveredHopCounts[sKey]:
# 		deliveredHops += deliveredHopCounts[sKey][dKey]

# print(deliveredHops)

# classDrops = countDropsByClass(lines)

# print(classDrops)