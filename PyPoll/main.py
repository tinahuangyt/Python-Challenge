import os
import csv
csvpath = os.path.join("..", "pypoll","election_data_test.csv")

voter = []
candidate = []
uniquelist = []
votesum = 0
finalname = []
totcount = []
percentvote = []

with open(csvpath) as csvfile: #open the file
    csvreader = csv.reader(csvfile, delimiter = ",")

    for row in csvreader:
        #print(row)
        voter.append(row[0])
        newvoter = voter[1:] #list of voter ID
        candidate.append(row[2])
        newcand = candidate[1:] #list of candidate
    
    print(str(len(newvoter))) #TOTAL NUMBER OF VOTES

    for i in range(len(newcand)):
        if str(newcand[i]) not in uniquelist:
            uniquelist.append(str(newcand[i]))
    
    print(uniquelist) #LIST OF CANDIDATES


    for i in range(len(uniquelist)):
        for a in range(len(newcand)):
            if str(uniquelist[i]) == str(newcand[a]):
                votesum = votesum + 1
        # print(str(uniquelist[i]) + " " + str(votesum)) #CANDIDATE NAME: TOT VOTE COUNT
        finalname.append(uniquelist[i])
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