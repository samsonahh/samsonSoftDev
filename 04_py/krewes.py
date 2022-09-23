"""
Kevin Wang and Samson Wu
SoftDev
K04 -- Using dictionaries and random to extract a random devo from a dictionary of krewes
2022-09-22
time spent: 

DISCO:
* the dictionary can span multiple lines for readability

QCC:
OPS SUMMARY:
1. Have user select a period
2. Generate a random value from 0 to the length of the array
3. Return that value
"""

import random
import math
krewes = {
    2: ["Jeff", "Anna"],
    7: ["Mom", "Grandma"],
    8: ["Dad", "Grandpa"]
}

def randomDevoOverall():
    periods = list(krewes.keys())
    randomIndex = math.floor(random.random() * len(periods))
    randomPeriod = periods[randomIndex]
    return randomDevoPeriod(randomDevoPeriod)

def randomDevoPeriod(period):
    devos = krewes[period]
    if len(devos) == 0:
        return
    else:
        index = math.floor(random.random() * len(devos))
        return devos[index]

print(randomDevoPeriod(2))
print(randomDevoOverall())
