import os
import csv
csvpath = os.path.join("..", "pypoll","election_data_test.csv")

with open(csvpath, newline="") as csvfile: #open the file
    csvreader = csv.reader(csvfile, delimiter = ",")
    newreader = next(csvreader)

    candidate = [] #all entries
    candlist = [] #list of 4 candidiates
   
    votesum = []
    #finalname = []
    totcount = []
    percentvote = []

    for row in csvreader:
        #print(row)
        candidate.append(row[2])
        if row[2] not in candlist:
            candlist.append(row[2]) 
    
    print(str(len(candidate))) #TOTAL NUMBER OF VOTES
    print(candlist) #LIST OF CANDIDATES
    
    ###########################

    for x in candlist:
        candcount = str(candidate.count(x))
        print(str(x)+": "+ candcount) #VOTE FOR EA CANDIDATE