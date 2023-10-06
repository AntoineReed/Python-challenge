import os
import csv

#create the path to the csv file
budget_data = os.path.join('budget_data.csv')

total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

#open with the csv file
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # pass over the header row during calaculations
    header = next(csv_reader)
    
    #iterate through the rows
    for row in csv_reader:
        #collect date and profit_loss from the current row
        date = row[0]
        profit_loss = int(row[1])

        #update total months and total profit/loss
        total_months += 1
        total_profit_loss += profit_loss

        if total_months > 1:
            #calculate the change in profit/loss
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)

            #check for the greatest increase and decrease
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        #update the previous profit/loss
        previous_profit_loss = profit_loss

#calculate the average change
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

#print the financial analysis results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit/Loss: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")
#it printed for me a few times then my code broke on line 5 I moved the file but its back in the folder and not working. 