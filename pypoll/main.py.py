#just packages
import csv
from collections import Counter

# Initialize total_votes to count the number of votes
total_votes = 0

# Initialize a Counter object to count votes for each candidate
candidates = Counter()

# Open the CSV file in read mode
with open('Resources.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    
    # Read each row in the CSV file
    for row in csv_reader:
        total_votes += 1  # Increment total votes for each row
        candidates[row[2]] += 1  # Increment the vote count for the candidate in the current row

# List to store the results
results = []
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100  # Calculate the percentage of total votes for each candidate
    results.append((candidate, percentage, votes))  # Append candidate's name, vote percentage, and total votes to results list

# Sort results by the number of votes in descending order
results.sort(key=lambda x: x[2], reverse=True)

# Determine the winner by the highest number of votes
winner = results[0][0]

# Print the election results
print("Election Results")
print("------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------")

# Print the results for each candidate
for candidate, percentage, votes in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("------------------------------")
print(f"Winner: {winner}")
print("------------------------------")
