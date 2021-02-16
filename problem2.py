# Alexander Smith
# 2/16/2021


def rotateChars(word, offset):
	
	# In case of no rotation, return the input word
	if offset == 0:
		return word
	
	# In cases where offset is negative or greater than len(word), fit back to scope
	# It is assumed that a negative number indicates a left shift, as a positive number indicates a right shift
	offset %= len(word)
	
	# Take the last 'offset' characters and place them at the beginning of the return string
	newWord = word[-offset:]
	
	# Take the remaining letters, and place them at the end of the return string
	newWord += word[0:(len(word) - offset)]
	return newWord
	