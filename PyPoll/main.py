import csv
import os

# Define the path to the dataset
file_path = os.path.join('Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidates_votes = {}

# Open and read the CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    
    # Skip the header row
    next(reader)
    
    # Loop through each row in the CSV file
    for row in reader:
        # Increment the total number of votes
        total_votes += 1
        
        # Get the candidate name from the row
        candidate = row[2]
        
        # Increment the candidate's vote count
        if candidate in candidates_votes:
            candidates_votes[candidate] += 1
        else:
            candidates_votes[candidate] = 1

# Calculate the election results
results = []
results.append("Election Results")
results.append("-------------------------")
results.append(f"Total Votes: {total_votes}")
results.append("-------------------------")

# Determine the winner
max_votes = 0
winner = ""

# Loop through each candidate's votes
for candidate, votes in candidates_votes.items():
    # Calculate the percentage of votes
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Determine if this candidate is the winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Add the winner to the results
results.append("-------------------------")
results.append(f"Winner: {winner}")
results.append("-------------------------")

# Output results to console
for final in results:
    print(final)

# Output results to a text file
with open('election_outcome.txt', 'w') as output_file:
    for final in results:
        output_file.write(final + '\n')