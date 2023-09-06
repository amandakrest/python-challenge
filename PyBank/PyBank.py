import os
import csv

budget_data = os.path.join("/Users/amanda/Desktop/Bootcamp/Week 3/Starter_Code 3/PyBank/Resources", "budget_data.csv")

total_months=[]
total_profit=[]
average_change=[]
greatest_increase=[]
greatest_decrease=[]
row_count = 0
revenue = []
date = []
rev_change = []


with open(budget_data) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    next(csvreader)

    for row in csvreader:
        row_count=row_count+1
        revenue.append(float(row[1]))
        date.append(row[0])
    #print(row_count)

    total_months.append(row_count)
    #print(total_months)




for i in range(1, len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])
        avg_rev_change= sum(rev_change)/len(rev_change)
        max_rev_change = max(rev_change)
        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))+1])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))+1])


print("Financial Analysis")
print("-------------------------")
print("Total Months:", total_months )
print("Total Revenue: $", sum(revenue))
print("Average Revenue Change: $", round(avg_rev_change))
print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")

        

        
