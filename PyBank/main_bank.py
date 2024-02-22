import csv

# File path to the CSV file
csv_file_path = "Resources/budget_data.csv"

# Initialize veriables
total_months = 0 
net_total = 0
previous_p_l = 0
p_l_changes = []
months = []

# Reading of the CSV file
with open(csv_file_path, 'r') as file:
    csvreader = csv.reader(file)

    # Skipping of the tiles in the file 
    next(csvreader)
    
    # Looping in each row of the file
    for row in csvreader:

        # Adding the total amounts of months 
        total_months += 1
        # Adding the net total amount in profit and loss 
        net_total += int(row[1])
        
        profit_loss = int(row[1])
        profit_loss_change = profit_loss - previous_p_l

        if total_months > 1 :
            p_l_changes.append(profit_loss_change)
            months.append(row[0])
        previous_p_l = profit_loss

# Calculate the average change in "Profit/Losses"
average_change = sum(p_l_changes) / len(p_l_changes)

# Locating the greatest increase 
g_increase = max(p_l_changes)
increase_index = p_l_changes.index(g_increase)
g_increase_month = months[increase_index]

# Locating the greatest decrease
g_decrease = min(p_l_changes)
decrease_index = p_l_changes.index(g_decrease)
g_decrease_month = months[decrease_index]


print ('Financial Analysis')

print ('-------------------------------')

print(f"Total Months: {total_months}")

print ( f'Total: ${net_total}')

print (f'Average Change: ${round(average_change, 2)}')

print(f"Greatest Increase in Profits: {g_increase_month} (${g_increase})")

print(f"Greatest Decrease in Profits: {g_decrease_month} (${g_decrease})")
