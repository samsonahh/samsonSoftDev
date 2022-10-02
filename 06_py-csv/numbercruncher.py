#Samson Wu and Harry Zhu
#Soft Dev
#Mr. Mykolyk
#9/30/22
#Time Spent: 1 hr.

'''
DISCO:
*string.split() can actually take two parameters to restrict the length of the created list. Ex: string.split(a, 1) will only make sure to split at the first occurence of a.
*string.splitlines() can be useful when dealing with csv file data. It automatically creates a list for you separating the whole data by its lines.
QCC:
*Is there a function that chooses from a list based on its weight? In other words, is there an alternative to our make_frequency_list() function?
*In the special case the name of the occupation includes a comma, is there another way to split the line only at the last comma without using our method?
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
data = file.read() #must read a file after opening it
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
    for list in l: #For each list in the list
        dict[list[0]] = list[1][0:] #Assign the occupation as key and the percentage as the value. [0:] to remove extra quotes.
    return dict

def make_frequency_list(d):
    l = []
    occ = list(d.keys()) #puts all the occupations in a list
    for i in range(len(occ)): #gets indices up to the number of occupations
        l+=[occ[i]]*int((float(d[occ[i]])*10))
        #int((float(d[occ[i]])*10)): d[occ[i]]: Grabs the percentage at the index, i
        #float(d[occ[i]]): Converts the percentage from a string to a float. Ex: '6.8' -> 6.8
        #(float(d[occ[i]])*10): Multiplies the percentage by 10. Ex: 6.8 -> 68.0
        #int((float(d[occ[i]])*10)): Turns the new float into an int. Ex: 68.0 -> 68
        #[occ[i]]*int((float(d[occ[i]])*10)): Adds int((float(d[occ[i]])*10)) number of the occupation to the final list.
        #Since total percentage according to the data is 99.8, the length of the final list should be 998.
    return l

def find_random_occupation(l):
    random_index = math.floor(random.random()*len(l)) #gets a random int from 0-998. Doesn't include 998.
    return l[random_index] #gets the occupation at that index

splitted_data = split_data(lines)
dict_data = put_into_dict(splitted_data)
freq_list = make_frequency_list(dict_data)
random_occupation = find_random_occupation(freq_list)

#print(splitted_data)
#print()
#print(dict_data)
#print()
#print(freq_list)
#print()
print('Random occupation: ' + str(random_occupation))
