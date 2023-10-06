import os
import csv

#create the file path to the csv file
file_path = "election_data.csv"

#create variables to store the analysis results
total_votes = 0
candidates = {}  # Dictionary 

#readthe csv file
with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    #step trough the header row
    header = next(csv_reader)
    
    for row in csv_reader:
        total_votes += 1
        candidate_name = row[2]
        
        #if the candidate is already in the dictionary; if not, add them
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] += 1

#percentage of votes each candidate won
percentage_votes = {}
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    percentage_votes[candidate] = percentage

#find the winner by popular vote
winner = max(candidates, key=candidates.get)

#print the analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    print(f"{candidate}: {percentage_votes[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
#The winner was Diana Degette