def factorial(n):
	if n == 1:
		return 1
	else:
		print('Factorial n: ', n)
		return n * factorial(n - 1)

print('Result: ', factorial(5))