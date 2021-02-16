# Alexander Smith
# 2/16/2021


# For a given list of numbers 'nums', determine how many are above and below the number 'threshold'
def aboveBelow(nums, threshold):
	# The count of numbers above and below the given threshold, both initialized to 0
	numAbove = numBelow = 0
	
	# For every number in the list 'nums', check if it is above or below the threshold
	for num in nums:
		if num > threshold:
			numAbove+=1
		elif num < threshold:
			numBelow+=1
	
	print("above: "+str(numAbove)+", below: "+str(numBelow))
	