#Michael Uy SID: 861064409 Feature Selection with Nearest Neighbor
import math
# Import Dataset
def mkDataSet(fileName):
	dataSet = []
	with open(fileName) as f:
		for i in f.readlines():
			try:
				temp= i.lstrip("  ")
				temp = [float(j) for j in temp.split()]
				temp[0] = int(temp[0])
				dataSet.append(temp)
			except ValueError, e:
				print "error",e,"on line", i
	return dataSet

# Normalize
def normalize(activeDataSet):
	dataSet = activeDataSet
	average = [0.00]*(len(dataSet[0])-1)
	stds = [0.00]*(len(dataSet[0])-1)
	#	get averages
	for i in dataSet:
		for j in range (1,(len(i))):
			average[j-1] +=  i[j]
	for i in range(len(average)):
		average[i] = (average[i]/len(dataSet))
	#	get std's sqrt((sum(x-mean)^2)/n)
	for i in dataSet:
		for j in range (1,(len(i))):
			stds[j-1] +=  pow((i[j] - average[j-1]),2)
	for i in range(len(stds)):
		stds[i] = math.sqrt(stds[i]/len(dataSet))
	#	calculate new values (x-mean)/std
	for i in range(len(dataSet)):
		for j in range (1,(len(dataSet[0]))):
			dataSet[i][j] = (dataSet[i][j] - average[j-1])/ stds[j-1]
	return dataSet

# Calculate similarity
def distance(a,b,params): 	#params is a list of 0's/1's for all true flags
	dis = 0
	for i in range (len(params)):
		if params[i]:
			dis += pow((a[i]-b[i]),2)
	return math.sqrt(dis)

# Locate neighbors
import operator 
def getNeighbor(trainingSet, testInstance, k, params):
	dis = []
	for x in range(len(trainingSet)):
		dist = distance(testInstance, trainingSet[x], params)
		dis.append((trainingSet[x], dist))
	dis.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(dis[x][0])
	return neighbors

# Calculate accuracy
def getAccuracy(dataSet,flags):
	accuracy = 0.00
	for i in range(len(dataSet)):
		trainingSet = list(dataSet)
		testInstance = trainingSet.pop(i) 
		neighbors = getNeighbor(trainingSet,testInstance,1, flags)
		if (len(neighbors) == 1):
			if (neighbors[0][0] == testInstance[0]):
				accuracy +=1
	accuracy = (accuracy/len(dataSet))* 100
	return accuracy

# Forward selection
# in:(flags, featureSet,best accuracy) out:(feature set and accuracy)
def getFeatureSet(dataSet,possibleFlags,currFeatures, bestAccuracy):
	accuracy = 0.0
	#featureSet = currFeatures
	flagsLeft = [i for i in possibleFlags if i not in currFeatures]
	#print "flags left: ", flagsLeft
	flagScores = [0.0]* len(flagsLeft)
	currIndex=0
	for i in flagsLeft:
		flags = [0]* (len(possibleFlags)+1)
		flags[i] = 1
		for j in currFeatures:
			flags[j] = 1
		accuracy = getAccuracy(dataSet,flags)
		flagScores[currIndex] = accuracy
		featureSet = list(currFeatures)
		featureSet.append(i)
		print "Using feature(s) {",
		if (len(featureSet)== 1):
			print featureSet[0],
		else:
			print ','.join(str(i) for i in featureSet),
		print"} accuracy is ",flagScores[currIndex],"%"
		currIndex += 1
	featureSet = list(currFeatures)
	y = max(flagScores)
	for i in range(len(flagsLeft)-1):
		if (flagScores[i]== y):
			featureSet.append(flagsLeft.pop(i))
	if(y < bestAccuracy):
		print "\n(Warning, Accuracy has decreased!",
		print " Continuing search in case of local maxima)",
	print "\nFeature set{",
	if (len(featureSet)== 1):
		print featureSet[0],
	else:
		print ','.join(str(i) for i in featureSet),
	print "} was best, accuracy is ", y,"%\n"
	return (featureSet, y)




def forward(fileName):
	dataSet = mkDataSet(fileName)
	instances = len(dataSet)
	features = len(dataSet[0])-1
	print "This dataset has ",features," features (not including the class attribute), with "\
	,instances," instances.\n"
	print "Please wait while I normalize the data...",
	#call normalize
	dataSet = normalize(dataSet)
	print "Done!"
	flags = [0,1,1,1,1,1,1,1,1,1,1]
	accuracy = getAccuracy(dataSet,flags)
	print "Running nearest neighbor with all "\
	 ,features," features, using \"leaving-one-out\" evaluation, I get an accuracy of "\
	 ,accuracy,"%\n"
	print "Beginning search.\n"
	posFlags = [i for i in range(1,features)]
	featureSet = []
	bestFeatureSet = []
	bestAccuracy = 0.0
	for i in range(1,features):
		retValue  = getFeatureSet(dataSet,posFlags,featureSet,bestAccuracy)
		featureSet =retValue[0]
		accuracy = retValue[1]
		if (accuracy > bestAccuracy):
			bestAccuracy = accuracy
			bestFeatureSet = list(featureSet) 
	print "Finished search!! The best feature subset is {",
	print ','.join(str(i) for i in bestFeatureSet),
	print "},which has an accuracy of ",bestAccuracy,"%"


# Main
fileName = ""
algorithm = 0
print "Welcome to Michael Uy\'s Feature Selection Algorithm"
while(1):	
	try:
		fileName = raw_input('Type in the name of the file to test: ')
		open(fileName)
	except EnvironmentError :
		print "Error: Cannot find ",fileName,"."
		continue
	else:
		break
print "Type in the number of the algorithm you want to test: "
print "1) Forward Selection"
print "2) Backward Elimination"
print "3) Original Algorithm"
algorithm = input()
if (algorithm == 1):
	forward(fileName)
elif (algorithm == 2):
	forward(fileName)
elif (algorithm == 3):
	forward(fileName)	

'''
dataSet = mkDataSet(fileName)
instances = len(dataSet)
features = len(dataSet[0])-1
print "This dataset has ",features," features (not including the class attribute), with "\
,instances," instances.\n"
print "Please wait while I normalize the data...",
#call normalize
dataSet = normalize(dataSet)
print "Done!"
flags = [0,1,1,1,1,1,1,1,1,1,1]
accuracy = getAccuracy(dataSet,flags)
print "Running nearest neighbor with all "\
 ,features," features, using \"leaving-one-out\" evaluation, I get an accuracy of "\
 ,accuracy,"%\n"
print "Beginning search.\n"
posFlags = [i for i in range(1,features)]
featureSet = []
bestFeatureSet = []
bestAccuracy = 0.0
for i in range(features):
	retValue  = getFeatureSet(posFlags,featureSet,bestAccuracy)
	featureSet =retValue[0]
	accuracy = retValue[1]
	if (accuracy > bestAccuracy):
		bestAccuracy = accuracy
		bestFeatureSet = list(featureSet) 
print "Finished search!! The best feature subset is {",
print ','.join(str(i) for i in bestFeatureSet),
print "},which has an accuracy of ",bestAccuracy,"%"
'''