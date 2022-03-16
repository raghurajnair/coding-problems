def twoNumberSum(array, targetSum):
    # Write your code here.
	resultSet = {}
	for number in array:
		potentialMatch = targetSum - number
		if potentialMatch in resultSet:
			return [potentialMatch, number]
		else:
			resultSet[number] = True
	return []