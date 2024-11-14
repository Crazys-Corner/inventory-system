session = {}

def setSession(key, value):
    session[key] = value

def getSession(key):
    return session.get(key)