# Imort the CSV and OS paths

import os
import csv

# Path to collect data from the resource folder

bank_csv = os.path.join ('..', 'Resources', 'budget_data.csv')

# For readability, assign variables wigth descriptive names

months = 0
toal_profitloss = 0
difference = 0
holding_value = 0
dates = []
profit =[]

# Read in the CSV file

with open (bank_csv, 'r') as csvfile:

 # Split the data on commas

    csvreader = csv.reader(csvfile, delimiter=',')

 # Header row & First Row defined

    header = next(csvreader)
    firstrow = next(csvreader)
    # Total number of months in the dataset can be count by finding the number of rows of data
 
    months +=1
    toal_profitloss += int(firstrow[1])

    #   Place holder to have a holding value

    holding_value = int(firstrow[1])
    

    #Read through every row

    for row in csvreader:
        dates.append(row[0])
        difference = int(row[1]) - holding_value
        profit.append(difference)

        #holding value to keep track og change in profit
        holding_value = int(row[1])

        months +=1

        toal_profitloss = toal_profitloss +int(row[1])

#Use Max Min function to calculate greatest increase or decrease

    greatest_increase = max(profit)
    greatest_row = profit.index(greatest_increase)
    greatest_date = dates[greatest_row]

greatest_decrease = min(profit)
least_row = profit.index(greatest_decrease)
least_date = dates[least_row]

average_change = sum(profit)/len(profit)

#Print using printf where necessary

print("Financial Analysis")
print("..........................")
print(f"Total Months: {str(months)}")
print(f"Total: $ {str(toal_profitloss)}")
print(f"Average Change: $ {str(round(average_change,2))}")
print (f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print (f"Greatest Decrease in Profits: {least_date} (${str(greatest_decrease)})")

# Exporting the results to text file
result = open ("output.txt", "w")
line1 = ("Financial Analysis")
line2 = ("..........................")
line3 = str(f"Total Months: {str(months)}")
line4= str(f"Total: $ {str(toal_profitloss)}")
line5 = str(f"Average Change: $ {str(round(average_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7= str(f"Greatest Decrease in Profits: {least_date} (${str(greatest_decrease)})")
result.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5, line6, line7))

