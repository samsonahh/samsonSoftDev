#Samson Wu and Harry Zhu
#Soft Dev
#Mr. Mykolyk
#9/29/22
#Time Spent: 1.5 hrs

#DISCO:
#you can use string.split("x") to separate string into a list that excludes x
#you must read a file after opening it
#
#QCC:
#Does the assignment have to be done with a list of dicts?
#Is using a dict of dicts fine?
#

import random
import math

file = open("krewes.txt")
data = file.read()#have to read a file after opening returns a string
file1 = open("devofam.csv")
data1 = file1.read()

#create a function that separates the @@@s and puts them all into a list
def separate(d):
    if len(d) < 3 or not '@' in d or not '$' in d: #checks if the data is valid
        return "Bad data"
    return d.split("@@@")[:-1]#can use split to remove strings and separates the leftovers into a list

def separateAgain(d): #will modify the list created from separate()
    temp = [] #gonna put lists into this one big list
    for data in d: #takes each 
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
    

