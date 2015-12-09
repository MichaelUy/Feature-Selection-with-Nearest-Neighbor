#Michael Uy SID: 861064409 Feature Selection with Nearest Neighbor
import math
# Import Dataset
dataSet = []
#temp = ""

with open('cs_170_small27.txt') as f:
	for i in f.readlines():
		try:
			temp= i.lstrip("  ")
			temp = [float(j) for j in temp.split()]
			temp[0] = int(temp[0])
			dataSet.append(temp)
		except ValueError, e:
			print "error",e,"on line", i

# Normalize
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
print len(dataSet[0])

for i in range(len(dataSet)):
	for j in range (1,(len(dataSet[0]))):
		dataSet[i][j] = (dataSet[i][j] - average[j-1])/ stds[j-1]
# Calculate similarity


# Locate neighbors


# Generate a response


# Calculate accuracy


# Main
print "averages"
for i in average:
	print i
print "stds"
for i in stds:
	print i
print "normalized"
for i in range (10):
	print dataSet[i]
