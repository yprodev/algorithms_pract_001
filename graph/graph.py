from collections import deque

graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
graph["claire"] = []
graph["mike"] = []

def person_is_seller(name):
	return name[-1] == 'm'


def search(graph, name):
	search_queue = deque()
	search_queue += graph[name]
	searched = [] # Keep track of the people we've searched before

	while search_queue: # While the queue is not empty
		person = search_queue.popleft() # grab the first person from the queue
		if not person in searched:
			if person_is_seller(person): # check whether the person is a needed person
				print(person + " is a seller")
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	return False

print(search(graph, "mike"))


