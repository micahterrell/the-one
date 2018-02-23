import random

xBound = 4500
yBound = 3400

def generateStaticNodes():
	f = open("nodelist.txt", "w")

	for i in range(40):
		prefix = "Group" + str(i + 8)
		groupString = "# " + prefix + " (static node " + str(i + 5) + ") settings\n"
		groupString = groupString + prefix + ".groupID = static" + str(i + 5) + "\n"
		groupString = groupString + prefix + ".movementModel = StationaryMovement\n"
		groupString = groupString + prefix + ".nodeLocation = " + str(random.randint(300, xBound - 300)) + ", " + str(random.randint(400, yBound - 400)) + "\n"
		groupString = groupString + prefix + ".nrofHosts = 1\n"
		groupString = groupString + prefix + ".nrofInterfaces = 1\n"
		groupString = groupString + prefix + ".interface1 = wifi\n\n"
		f.write(groupString)

	f.close()

generateStaticNodes()