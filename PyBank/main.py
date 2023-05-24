import os
import csv


csvpath = os.path.join('Resources','budget_data.csv')

#open the budget_data.csv file
with open(csvpath, encoding='utf8') as budgetdata:
    csvreader = csv.reader(budgetdata, delimiter=',')
   
    #Get the data into a list
    budgetrows=[row for row in csvreader]
    csvheader = budgetrows.pop(0) # Remove the header from the list
    
    total_change=0
    change_dict={} # dictionary to store the increase or decrease in profit / loss
    for i in range(len(budgetrows)):
        if i > 0:
            profit_loss_change=  int(budgetrows[i][1]) - int(budgetrows[i-1][1])
            change_dict[budgetrows[i][0]]= profit_loss_change
            total_change = total_change+profit_loss_change
             
    total_months=len(budgetrows) #Total number of months, exclude the header

    total_profit_loss=0
    for monthly_budget in budgetrows:
        total_profit_loss = total_profit_loss+int(monthly_budget[1]) # Total profit/loss

# write the results into the analysis file and print it on the terminal  
analysisoutput = os.path.join('analysis','FinancialAnalysis.txt')
with open(analysisoutput,'w') as analysiswriter:
    analysiswriter.write("```text\n")
    print("```text")
    analysiswriter.write("Financial Analysis\n")
    print("Financial Analysis")
    analysiswriter.write("----------------------------\n")
    print("----------------------------")
    analysiswriter.write(f"Total Months: {total_months}\n")
    print(f"Total Months: {total_months}")
   
    analysiswriter.write(f'Total: {total_profit_loss:.0f}\n')
    print(f'Total: ${total_profit_loss:.0f}')
   
    analysiswriter.write(f'Average change: ${(total_change/(len(budgetrows)-1)):.2f}\n')
    print(f'Average change: ${(total_change/(len(budgetrows)-1)):.2f}')
   
   #use the lambda or anonymous function to get the greatest profit increase and decrease from change_dict dictionary
    analysiswriter.write(f'Greatest Increase in Profits: {max(change_dict, key=lambda key:change_dict[key])}  (${(change_dict[max(change_dict, key=lambda key:change_dict[key])]):.0f})\n')
    print(f'Greatest Increase in Profits: {max(change_dict, key=lambda key:change_dict[key])}  (${(change_dict[max(change_dict, key=lambda key:change_dict[key])]):.0f})')
   
    analysiswriter.write(f'Greatest Decrease in Profits: {min(change_dict, key=lambda key:change_dict[key])}  (${(change_dict[min(change_dict, key=lambda key:change_dict[key])]): .0f})\n')
    print(f'Greatest Decrease in Profits: {min(change_dict, key=lambda key:change_dict[key])}  (${(change_dict[min(change_dict, key=lambda key:change_dict[key])]): .0f})')
   
    analysiswriter.write("```\n")
    print("```")