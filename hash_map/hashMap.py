book = dict()
new_book = {}

book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49

print(book)
print(book["avocado"])

voted = {}

def check_voter(name):
	if voted.get(name):
		print("Kick them out")
	else:
		voted[name] = True
		print("let them vote")

check_voter("Tom")
check_voter("Clark")
check_voter("Emilie")
check_voter("Tom")


