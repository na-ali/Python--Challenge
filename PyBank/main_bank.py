import csv
import os

# File paths
csv_file_path = "Resources/budget_data.csv"
text_file_path = "Analysis/financial_analysis.txt"

# Store headers in variables
csv_headers = ['Date', 'Profit/Losses']

# Initialize variables
total_months = 0 
net_total = 0
previous_p_l = 0
p_l_changes = []
months = []

# Reading the CSV file
with open(csv_file_path, 'r') as file:
    csvreader = csv.reader(file)
    csv_header = next(csvreader)  # Read header row
    # Check if headers match
    if csv_header != csv_headers:
        print("CSV file headers do not match expected headers.")
        print(f"Expected headers: {csv_headers}")
        print(f"Actual headers: {csv_header}")
        exit()

    for row in csvreader:
        total_months += 1
        net_total += int(row[1])
        
        profit_loss = int(row[1])
        profit_loss_change = profit_loss - previous_p_l

        if total_months > 1:
            p_l_changes.append(profit_loss_change)
            months.append(row[0])
        previous_p_l = profit_loss

# Calculate metrics
average_change = sum(p_l_changes) / len(p_l_changes)
g_increase = max(p_l_changes)
g_increase_month = months[p_l_changes.index(g_increase)]
g_decrease = min(p_l_changes)
g_decrease_month = months[p_l_changes.index(g_decrease)]

# Print financial analysis to terminal
analysis_output = (
    f"Financial Analysis\n"
    f"-------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${round(average_change, 2)}\n"
    f"Greatest Increase in Profits: {g_increase_month} (${g_increase})\n"
    f"Greatest Decrease in Profits: {g_decrease_month} (${g_decrease})\n"
)

print(analysis_output)

# Write financial analysis to text file
with open(text_file_path, 'w') as text_file:
    text_file.write(analysis_output)

print("Financial analysis has been saved to:", text_file_path)
