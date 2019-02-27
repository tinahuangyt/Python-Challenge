import os
import csv
csvpath = os.path.join("..", "pybank","budget_data.csv")

months = []
money = []

with open(csvpath) as csvfile: #open the file
    csvreader = csv.reader(csvfile, delimiter = ",") #read the csv
    
    for row in csvreader:
        #print(row)
        months.append((row[0])) #create a list of months
        newmonths = months[1:] #remove first item 
        money.append((row[1])) #create a list of money
        newmoney = money[1:] #remove first item
        
    #print(str(len(newmonths))) #TOTAL MONTHS
    
    moneyint = list(map(int,newmoney)) #convert to list of int
    sm = sum(moneyint) #NET TOTAL

    diffs = []
    for i in range(len(newmoney)-1):
        diffs.append(int(newmoney[i+1]) - int(newmoney[i]))
    
    #print(diffs) #list of all the differences 
    #print(len(diffs))
    totdiff = list(map(int,diffs)) #convert to list of int
    #print(totdiff)
    avgchange = round(sum(totdiff)/len(totdiff), 2) #AVERAGE CHANGES, round to 2 decimals
    

    maxdiff = max(totdiff) #MAX DIFF
    maxdiffindex = totdiff.index(maxdiff)+1 #index of max diff
    newmonths[maxdiffindex] #MONTH OF MAX DIFF

    mindiff = min(totdiff) #MIN DIFF
    mindiffindex = totdiff.index(mindiff)+1
    newmonths[mindiffindex] #MONTH OF MIN DIFF

print("Financial Analysis")
print("------------------------------------------")
print("Total Months: "+str(len(newmonths)))
print("Total: $"+str(sm))
print("Average Change: $"+str(avgchange))
print("Greatest Increase in Profits: "+ str(newmonths[maxdiffindex])+ " ($" + str(max(totdiff)) + ")")
print("Greatest Decrease in Profits: "+ str(newmonths[mindiffindex])+ " ($" + str(min(totdiff)) + ")")




f=open("results.txt","w") #creates a file
f.write("Financial Analysis")
f.write("------------------------------------------")

f.close() #write and saves the file

###### Export result to txt file

#in terminal python main.py > result.txt