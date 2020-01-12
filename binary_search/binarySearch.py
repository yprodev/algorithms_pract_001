def binary_search(list, item):
	lowPoint = 0
	highPoint = len(list) - 1

	while lowPoint <= highPoint:
		middlePoint = (lowPoint + highPoint)
		guess = list[middlePoint]

		if guess == item:
			return middlePoint

		if guess > item:
			highPoint = middlePoint - 1
		else:
			lowPoint = middlePoint + 1

	return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))

