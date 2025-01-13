
def findMin(s, k):
	# Write your code here
	#check for max number of char together
	#number of k
	group_mx = 0
	window = 0
	number_of_k = 0
	for char in s:
		if char == k:
			window+=1
			number_of_k+=1
		else:
			window = 0
		if group_mx < window:
			group_mx = window
	return number_of_k - group_mx

print(findMin('mohhhittthaahth', 'h'))

print(findMin('programing', 'g'))

print(findMin('hello', 'l'))

print(findMin('hellolal', 'l'))
