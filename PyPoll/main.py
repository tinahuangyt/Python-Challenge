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
    









    for i in range(len(uniquelist)):
        for a in range(len(newcand)):
            if str(uniquelist[i]) == str(newcand[a]):
                votesum = votesum + 1
        # print(str(uniquelist[i]) + " " + str(votesum)) #CANDIDATE NAME: TOT VOTE COUNT
        #finalname.append(uniquelist[i])
        totcount.append(votesum)
        votesum = 0
    print(finalname) #LIST OF NAMES
    print(totcount) #LIST OF TOTAL COUNT

    for i in range(len(totcount)):
        percentvote.append(int(totcount[i])/int(len(newvoter)))
    print(percentvote) #LIST OF PERCENTAGE






#The total number of votes cast
#A complete list of candidates who received votes

#The total number of votes each candidate won
#The percentage of votes each candidate won

#The winner of the election based on popular vote