import os
import csv

# Path to the CSV file
file_csv = os.path.join("Resources/election_data.csv")

# Store headers in variables
csv_headers = ['Ballot ID', 'County', 'Candidate']

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
w_votes = 0

# Reading of the csv file 
with open(file_csv, 'r') as file:
    csv_reader = csv.reader(file)
    csv_header = next(csv_reader)  # Read header row
    # Check if headers match
    if csv_header != csv_headers:
        print("CSV file headers do not match expected headers.")
        print(f"Expected headers: {csv_headers}")
        print(f"Actual headers: {csv_header}")
        exit()

    # Loop through each row
    for row in csv_reader:
        # Total number of votes cast
        total_votes += 1
        
        # Locating the candidate's name
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

# Write election results to text file
text_file_path = "Analysis/election_results.txt"
with open(text_file_path, 'w') as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        text_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    text_file.write('-------------------------\n')
    text_file.write(f"Winner: {winner}\n")
    text_file.write("-------------------------\n")

print("Election results have been saved to:", text_file_path)
