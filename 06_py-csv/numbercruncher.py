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
*The first line will be assigned as keys
*In case of multiple commas, we will try to use a special split function
*Don't include the last line (total line)
-Return random with percent part
*Thinking about multiplying all the percents by 10 and then appending that number of occupations in an array
*Then we would randomly select from that array
'''

file = open("occupations.csv")
data = file.read()
lines = data.splitlines()[:-1] #The ending here exludes the total line

def split_data(d):
    final = []
    for line in d: #works with every individual line
        if ", " in line: #special case where the occupation has a comma too
            line = line[::-1].split(",", 1) #reverse the string and split the first comma only
            line = [[[line[1][::-1]],[line[0][::-1]]]] #reverse the contents of the lists again and put the lists in a list
            final+=line #add this to final
            continue #skip the step below
        final+=[[[line.split(",")[0]],[line.split(",")[1]]]]
    return final

def put_into_dict(l):
    dict = {}
    list_without_first = l[1:]
    for list in list_without_first:
        dict[l[0][0]] = list[0]
        dict[l[0][1]] = list[1]
    return dict


print(split_data(lines))
print()
print(put_into_dict(split_data(lines)))