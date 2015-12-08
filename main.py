#Michael Uy SID: 861064409 Feature Selection with Nearest Neighbor

# Import Dataset
dataSet = []
temp = ""

with open('cs_170_small27.txt') as f:
	for i in f.readlines():
		try:
			temp= i.lstrip("  ")
			temp = [tuple(map(eval, temp.split("  ")))]
			dataSet.append(temp)
		except ValueError, e:
			print "error",e,"on line", i
# Calculate similarity


# Locate neighbors


# Generate a response


# Calculate accuracy


# Main

for i in dataSet:
	print i