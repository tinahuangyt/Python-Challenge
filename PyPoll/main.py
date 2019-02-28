import os
import csv
csvpath = os.path.join("..", "pypoll","election_data.csv")

with open(csvpath, newline="") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ",")
    newreader = next(csvreader)

    candidate = [] 
    candlist = [] 
    countlist = []
   
    for row in csvreader:
        #print(row)
        candidate.append(row[2])
        if row[2] not in candlist:
            candlist.append(row[2]) #Candidate list
    
    
    f=open("result.txt", "w") #Open txt file
    
    print("Election Results", file=f)
    print("------------------------", file=f)
    print("Total Votes: " + str(len(candidate)),file=f) #Total votes/candidate
    print("------------------------",file=f)

    for x in candlist:
        candcount = candidate.count(x)
        countlist.append(int(candcount)) #Add count to list
        percentvote = int(candcount)/int(len(candidate))
        adjpercent = round(percentvote*100,2)
        print(str(x)+": "+ str(adjpercent) + "% " + "("+ str(candcount)+")",file=f) #Output for ea candidate
    
    #print(countlist)
    winnerindex = countlist.index(max(countlist))
    print("------------------------",file=f)
    print("Winner: "+ candlist[winnerindex],file=f)
    print("------------------------",file=f)

    f.close()

resultpath = os.path.join("..", "pypoll","result.txt") #Print txt content in terminal
with open(resultpath) as resultfile:
    data = resultfile.read()
    print(data)