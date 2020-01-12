'''
# Countdown is infinite
def countdown(i):
	print(i)
	countdown(i - 1)
'''
def countdown(i):
	if i <= 0: # Base case
		return
	else: # Recursion case
		print(i)
		countdown(i - 1)

countdown(5)