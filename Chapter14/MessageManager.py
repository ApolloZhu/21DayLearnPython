current = "shared"

def switch(session):
    __setcurto(session)
    try:
        open(__getcurlog(),'r').close()
    except:
        with open(__getcurlog(),'a') as log:
            log.write("--[[{0}]]--\n\n".format(session))

def __setcurto(session):
    global current
    current = session

def __getlog(session):
    return session+'.azhistory'

def __getcurlog():
    return __getlog(current)

def __new(session):
    open(__getlog(session),'w').close()

def retrieve(session=current,index=None, decode=True):
    lib = retrieveall(session)
    if index == None:
        index = -1
    line = lib[index]
    if decode:
        return transcript(line)
    return line

def retrieveall(session=current, decode=True):
    try:
        with open(__getlog(session),'r') as log:
            lines = [line.strip() for line in log.readlines()]
            if decode:
                return transcript(lines)
            return lines
    except:
        __new(session)
        retrieve(session,index)

def append(session=current,user="Anonymous",message="Lorem Ipsum"):
    try:
        with open(__getlog(session),'a') as log:
            log.write("{0}|az|{1}\n".format(user,message))
    except:
        __new(session)
        append(session,user,message)
        
    
def transcript(lines):
    transcripted = []
    for line in lines:
        partial = line.split('|az|',1)
        if len(partial) == 2:
            transcripted.append(partial)
    return transcripted

if __name__ == "__main__":
    append(user="Tester",message="Hi")
    print(retrieveall())
