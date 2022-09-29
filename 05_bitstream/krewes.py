#Samson Wu and Harry Zhu

import random
import math

file = open("krewes.txt")
data = file.read()#have to read a file after opening returns a string

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
        answer[i[1]] = {}#Initializes an empty dict for each name
    for i in datalist:#every list of data per individual again because we dont want to overwrite repeating names/ we add instead
        answer[i[1]]['PD'] = i[0] #creates a 'PD' key for each individual's dict and assigns it the period value
        answer[i[1]]['DUCKY'] = i[2] #creates a 'DUCKY' key for each individual's dict and assigns it the ducky name
    return answer#returns the organized dict

cool_dict = makeDict(data)

def randomDevo(dict):
    names = list(dict.keys()) #turns all the dict's keys into a list
    index = math.floor(random.random() * len(names)) #gets a random index integer from  0 - length of # of keys
    random_name = names[index] #chooses the random name with the random index
    ducky_name = dict[random_name]['DUCKY'] #gets the ducky name for that random person
    period = dict[random_name]['PD'] #gets the period value for that random person
    answer = "Name: " + str(random_name) + ", Ducky: " + str(ducky_name) + ", Period: " + str(period) #makes neat answer
    return answer

print(randomDevo(cool_dict))
    

