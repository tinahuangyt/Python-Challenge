import os
import csv
csvpath = os.path.join("..", "pypoll","election_data.csv")

with open(csvpath, newline="") as csvfile: #open the file
    csvreader = csv.reader(csvfile, delimiter = ",")
    newreader = next(csvreader)

    candidate = [] 
    candlist = [] 
    countlist = []
   
    for row in csvreader:
        #print(row)
        candidate.append(row[2])
        if row[2] not in candlist:
            candlist.append(row[2]) #LIST OF CANDIDIDATES
    
    print("Election Results")
    print("------------------------")
    print("Total Votes: " + str(len(candidate))) #TOTAL NUMBER OF VOTES
    print("------------------------")

    for x in candlist:
        candcount = candidate.count(x)
        countlist.append(int(candcount)) #add count to list 
        percentvote = int(candcount)/int(len(candidate))
        adjpercent = round(percentvote*100,2)
        print(str(x)+": "+ str(adjpercent) + "% " + "("+ str(candcount)+")") #OUTPUT
    
    #print(countlist)
    winnerindex = countlist.index(max(countlist))
    print("------------------------")
    print("Winner: "+ candlist[winnerindex])
    print("------------------------")



#The total number of votes cast
#A complete list of candidates who received votes

#The total number of votes each candidate won
#The percentage of votes each candidate won

#The winner of the election based on popular vote