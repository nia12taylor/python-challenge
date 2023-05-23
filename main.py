#Import the csv module
import csv

#Specify the file path
file_path = "Resources/budget_data.csv"

#List of Dates
date = []

#List of Profit/Losses
pl = []

#Open the csv
with open(file_path,'r') as csvfile:

    #Read the csv
    csvreader = csv.reader(csvfile, delimiter=',')

    #Store and skip the header
    csv_header = next(csvreader)

    #Loop through the csv
    for row in csvreader:

        #Append index 0 to the list of Dates
        date.append(row[0])

        #Append index 1 to the list of Profit/Losses
        pl.append(int(row[1]))

#Store the number of months
total_months = len(date)

#Store the sum of the Profit/Losses
total = sum(pl)

#Store the sum of the differences in Profit/Losses
diftotal = 0

#Store how many times we calculated a difference
numdiff = 0

#Store the greatest increase in profits
greatestincrease = 0

#Store the month of the greatest increase in profits
greatestincreasemonth = 0

#Store the greatest decrease in profits
greatestdecrease = 0

#Store the month of the greatest increase in profits
greatestdecreasemonth = 0

#Loop through the Profit/Losses list, starting with the second index
for cabbage in range(1,len(pl)):

    #Calculate the difference in Profit/Losses and add it to the sum of differences
    diff = (int(pl[cabbage])-int(pl[cabbage-1]))
    diftotal = diftotal + diff

    #If the calculated difference is bigger than the greatest increase
    if diff > greatestincrease:

        #Overwrite the greatest increase
        greatestincrease = diff

        #Overwrite the greatest increase month
        greatestincreasemonth = str(date[cabbage])
    
    #Else if the calculated difference is smaller than the greatest decrease
    elif diff < greatestdecrease:

        #Overwrite the greatest decrease
        greatestdecrease = diff

        #Overwrite the greatest decrease month
        greatestdecreasemonth = str(date[cabbage])

    #Add one to how many differences we calculated
    numdiff += 1

#Calculate the average change rounded to two decimals
avgchng = round(diftotal/numdiff, 2)

#Store the Profit/Loss analysis in a variable
pl_analysis = (f"Financial Analysis"
"\n----------------------------"
f"\nTotal Months: {total_months}"
f"\nTotal: ${total}"
f"\nAverage change: ${avgchng}"
f"\nGreatest Increase in Profits: {greatestincreasemonth} (${greatestincrease})"
f"\nGreatest Decrease in Profits: {greatestdecreasemonth} (${greatestdecrease})"
)

#Print the Profit/Losses analysis to the terminal
print(pl_analysis)

#Specify the location of the .txt file where we will print the results
text_path = "analysis/results.txt"

#Open the file 
with open(text_path, "w") as f:

    #Print the analysis
    f.write(pl_analysis)
