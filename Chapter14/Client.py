import AccountManager, MessageManager

class Client():
    def __init__(self, name="Client"):
        self.name = name

    def __repr__(self):
        return "Client named " + name
    
    def login(user,password):
        isValid(user, password)
    
    def logout(user):
        print("Exiting...")
