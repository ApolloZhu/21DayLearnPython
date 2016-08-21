lib = [
	{'name': 'john', 'password':'2354kdd','usertype':'1'},
	{'name': 'a', 'password':'b','usertype':'2'},
        {'name': 'a', 'password':'b','usertype':'3'}
]

def login(name, password):
	user = list(filter(lambda u: u['name'] == name and u['password'] == password, lib))
	if len(user) == 1:
		return user[0]['usertype']
	elif len(user) > 1:
		return -1
	else:
		return 0
