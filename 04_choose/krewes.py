"""
Kevin Wang and Samson Wu
SoftDev
K04 -- Using dictionaries and random to extract a random devo from a dictionary of krewes
2022-09-22
time spent: 1.5 hrs

DISCO:
* the dictionary can span multiple lines for readability
* random.choice(list) can alternatively be list[math.floor(random.random() * len(list)]
* random.random() returns a float between 0 inclusive and 1 exclusive
* random and math are built in libraries but need to be imported
QCC:
What is a krew?
Why do I have to typecast the dict_keys object to a list before looping?

OPS SUMMARY:

randomDevoPeriod
1. Have user select a period
2. To generate a random index, use math.floor(random.random() * len(array))
3. Return that devo at that random index

randomDevoOverall
1. Generate a random period using math.floor(random.random() * len(array))
2. Insert that period into the randomDevoPeriod function

"""

import random
import math

krewes = {
    2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "Ruiwen"], 
    7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
    8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "Wanying", "Kevin"]
}


#takes a period and returns a random devo from that period
def randomDevoPeriod(period):
    if (period in krewes.keys()): #validates that the user input is actually an existing period
        devosFromPeriod = krewes[period] #array of devos
        index = math.floor(random.random() * len(devosFromPeriod)) #random index of devosFromPeriod

        return devosFromPeriod[index]
    else:
        return None

print(randomDevoPeriod(2))



"""
#returns a random devo across any period
def randomDevoOverall():
    #generate a random period using the same algorithm
    periods = list(krewes.keys())
    randomIndex = math.floor(random.random() * len(periods))
    randomPeriod = periods[randomIndex]

    #reuse randomDevoPeriod
    return randomDevoPeriod(randomPeriod)

print(randomDevoOverall())

"""
