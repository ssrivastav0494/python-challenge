import os
import csv
budget = os.path.join("Resources", "budget_data.csv")
total_months = 0
total_amount = 0
change = []
change_months = []

with open(budget) as budget_file:
    csvreader = csv.reader(budget_file, delimiter = ',')

    header = next(csvreader)
    
    first_row = next(csvreader)
    total_months += 1
    total_amount = int(first_row[1])

    previous_amount = int(first_row[1])

    for row in csvreader:
        
        total_months += 1
        
        total_amount += int(row[1])

        change.append(int(row[1])-previous_amount)

        change_months.append(row[0])
        
        previous_amount = int(row[1])

average_change = round(sum(change)/len(change),2)

greatest_increase = max(change)

greatest_decrease = min(change)

greatest_increase_month = change_months[change.index(greatest_increase)]
greatest_decrease_month = change_months[change.index(greatest_decrease)]

financial_analysis = ("Financial Analysis\n"
                        "--------------------------\n"
                        f"Total Months: {total_months}\n"
                        f"Total: ${total_amount}\n"
                        f"Average Change: ${average_change}\n"
                        f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
                        f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

print(financial_analysis)

output_path = os.path.join("Text file","Bank.txt")

with open(output_path, "w") as txtfile:
    txtfile.write(financial_analysis)