#TNPG: Worship Warship
#Roster: Samson, Joshua, Aahan
#Time Spent: 1.5 hrs
'''
DISCO:
*returning a list will display a cool looking json page
*we can change the route from "/" to "/anyplace" so when we goto localhost:5000/anyplace it displays what we returned under the "/anyplace" route.
*<br/> creates a new line instead of \n
'''

from flask import Flask
import random

list_occupation = open("occupations.csv").read().replace("\n", "<br/>")

def main():
    jobs = []
    weight = []
    # parseinfo takes in a csv file and 2 lists. It parses the jobs in the csv file to the jobs list and the weights to the weight list, not including the total
    parseinfo("occupations.csv", jobs, weight)
    return str(random.choices(jobs, weights = weight))[2:-2]
    
def parseinfo(file, jobs, weight):
    occ_wei = open(file, "r").read()
    
    # Creates a list of all occupation,weight pairs, excluding the first line, which isn't relevant.
    occ_wei = occ_wei.split("\n")[1:]
    
    for pair in occ_wei:
        # first see if pair is empty.
        if(len(pair) != 0):
            # rsplit() splits from  the left, and the second argument decides how many times to split.
            job_percent_pair = pair.rsplit(",", 1)
            # Dont include the Total,percent pair
            if(job_percent_pair[0] != "Total"):
                jobs.append(job_percent_pair[0])
                # Because we are using the choices method, the weights list has to only include integers, since
                weight.append(int(float(job_percent_pair[1]) * 10))

app = Flask(__name__) # ...

@app.route("/") # ...
def TNPG():
    job = main()
    print(__name__)
    return "TNPG: Worship Warship, Roster: Samson, Joshua, Aahan <br/><br/>" +\
     "List of occupations:<br/>" + list_occupation + "<br/>Random Occupation: " + \
        "<a href=https://www.google.com/search?q="+ job.replace(" ", "+") + "+jobs+near+me target=_blank rel=noopener noreferrer>" + job + "</a>"

app.debug = True
app.run()