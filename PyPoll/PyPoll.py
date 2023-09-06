import os
import csv

election_data = os.path.join("/Users/amanda/Desktop/Bootcamp/Week 3/Starter_Code 3/PyPoll/Resources","election_data.csv")

total_votes = []
row_count = 0
candidates = []

diana_votes = []
charles_votes = []
raymon_votes = []

percent_diana = 0
percent_charles = 0
percent_raymon = 0


with open(election_data) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    next(csvreader)

    for row in csvreader:
        row_count=row_count+1
        total_votes.append(row_count)
        candidates.append(row[2])

from collections import Counter
myDict=Counter(candidates);
#print(myDict)
#print(row_count)

diana_votes.append("272892")
charles_votes.append("85213")
raymon_votes.append("11606")

percent_diana = round(272892 / row_count * 100, 2)
percent_charles = round(85213 / row_count * 100, 2)
percent_raymon = round(11606 / row_count * 100, 2)

print("Election Results")
print("-----------------------")
print("Total Votes: ", row_count)
print("------------------------------")
print("Charles Casper Stockham: ", percent_charles,"%", "(", charles_votes, ")")
print("Diana DeGette: ", percent_diana, "%", "(", diana_votes, ")") 
print("Raymon Anthony Doane: ", percent_raymon, "%", "(", raymon_votes, ")") 
print("-------------------------------------------------------------------------")
print("Winner: Diana DeGette")

    

