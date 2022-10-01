#Samson Wu and Harry Zhu
#Soft Dev
#Mr. Mykolyk
#9/30/22
#Time Spent:

'''
DISCO:

QCC:

HOW THIS SCRIPT WORKS:

DESIGN:
-Put into dict part
*The dict will read each line of the csv file
*Then will separate the contents of each line by its comma
*The occupation will be the keys
*The percentage will be the values
*In case of multiple commas, we will try to special split it
*Don't include the last line (total line) and first line
-Return random with percent part
*Thinking about multiplying all the percents by 10 and then appending that number of occupations in a list
*Then we would randomly select from that list
'''

import random
import math

file = open("occupations.csv")
data = file.read()
lines = data.splitlines()[1:-1] #The ending here exludes the total line

def split_data(d):
    final = []
    for line in d: #works with every individual line
        if ", " in line: #special case where the occupation has a comma too
            line = line[::-1].split(",", 1) #reverse the string and split the first comma only
            line = [[line[1][::-1]]+[line[0][::-1]]] #reverse the contents of the lists again and put the lists in a list
            final+=line #add this to final
            continue #skip the step below
        final+=[line.split(",")]
    return final

def put_into_dict(l):
    dict = {}
    for list in l:
        dict[list[0]] = list[1][0:]
    return dict

def make_frequency_list(d):
    l = []
    occ = list(d.keys())
    for i in range(len(occ)):
        l+=[occ[i]]*int((float(d[occ[i]])*10))
    return l

def find_random_occupation(l):
    random_index = math.floor(random.random()*len(l))
    return l[random_index]

splitted_data = split_data(lines)
dict_data = put_into_dict(splitted_data)
freq_list = make_frequency_list(dict_data)
random_occupation = find_random_occupation(freq_list)

print(splitted_data)
print()
print(dict_data)
print()
print(freq_list)
print()
print(random_occupation)
