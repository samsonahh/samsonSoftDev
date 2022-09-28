#Samson Wu and Harry Zhu

import random

file = open("krewes.txt")
data = file.read()#have to read a file after opening

#create a function that separates the @@@s and puts them all into a list
def separate(d):
    return d.split("@@@")[:-1]#can use split to remove strings and separates the leftovers into a list

def separateAgain(d):
    temp = []
    for data in d:
        temp+=[data.split("$$$")]#typecast [] to make a list in a list
    return temp

def makeDict(d):
    messylist = separate(d)#creates a single list split at @@@ Ex: [a$$$b, c$$$d, e$$$f]
    datalist = separateAgain(messylist)#creates a list of lists that split at $$$ Ex: [[a,b], [c,d], [e,f]]
    answer = {}#creates empty dict
    for i in datalist:#loops through every list of data per individual
        answer[i[0]] = {}#creates a key for every period number and an empty dict as the pd values
    for i in datalist:#every list of data per individual again because we dont want to overwrite repeating periods/ we want to add instead
        answer[i[0]][i[1]] = i[2] #creates a key for the dicts inside each period that corresponds to a name and the value as their ducky name
    return answer#returns the organized dict

print(makeDict(data))
