import random
from pymongo import Connection

conn = Connection()

db = conn['1247']
tdic = {'username': 'testing', 'password':'testing'}
db.usertable.insert(tdic)

def printData():
    cres = db.usertable.find()
    #{}, {'_id':False})
    #print cres
    #res = [r
    for r in cres:
        print r

def addUser(usernamei, passwordi):
    cres = db.usertable.find({'username':usernamei})
    res = [r for r in cres]
    print res
    if len(res)>0:
        return False
    nu = {'username': usernamei, 'password':passwordi}
    db.usertable.save(nu)
    return True

def validate(usernamei, passwordi):
    res = db.usertable.find({'username': usernamei,'password':passwordi})
    if len(res)>0:
        return True
    return False

def updateUser(usernamei, passwordi):
    res = db.usertable.find({'username':usernamei})
    if len(res)>0:
        return False
    db.usertable.update({'username': usernamei,'password':passwordi})
    return True
    
