import os
import csv

# Path to the CSV file
file_csv = os.path.join("Resources/election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
w_votes = 0

# Reading of the csv file 
with open(file_csv, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    # looping through each row
    for row in csv_reader:
        # Total number of votes cast
        total_votes += 1
        
        # locating the candidate's name
        candidate_n = row[2]
        
        # Update the candidates dictionary
        if candidate_n in candidates:
            candidates[candidate_n] += 1
        else:
            candidates[candidate_n] = 1

# Printing the results 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------") 

# Going through the candidates and calculate percentages
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Finding the winner
    if votes > w_votes:
        winner = candidate
        w_votes = votes
print('-------------------------')
print(f"Winner: {winner}")
print("-------------------------")

