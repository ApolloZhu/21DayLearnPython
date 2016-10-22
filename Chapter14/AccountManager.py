_file = "accounts.azlogin"

buffered = []

def update():
    try:
        with open(_file,'r') as lib:
            global buffered
            temp = [line.strip() for line in lib.readlines()]
            buffered = [decode(line) for line in temp if line != '']
    except:
        open(_file,'a').close()

def decode(encoded):
    return encoded.replace('\n','').split('\t',1)

def encode(user,password):
    return user + '\t' + password + '\n'

def append(user,password=''):
    if len(buffered) == 0:
        update()
    if not isValid(user, password):
        with open(_file,'a') as lib:
            lib.write(encode(user,password))
        update()

def isValid(user,password=''):
    if len(buffered) == 0:
        update()
    for info in buffered:
        if user == info[0] and password == info[1]:
            return True
    return False
    