# In this project, we will read election data to determine:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote.

# csv module
import csv
import os
dir(os)

# initialize variables
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# assigning variable to file path
load1 = os.path.join("resources", "election_results.csv")
save1 = os.path.join("analysis", "election_analysis.txt")
outfile1 = open(save1, "w")
bar = "----------------------------\n"
election_results_header = (
    f"Elections Results\n"
    f"{bar}")

print(election_results_header)
outfile1.write(election_results_header)

with open(load1,"r") as election_results:
    #Read, Analyze
    file_reader = csv.reader(election_results)
    # Print header row
    headers = next(file_reader)

    for row in file_reader:
        #Sum votes
        total_votes += 1

        #specify where the candidate name is found in the csv
        candidate_name = row[2]

        #if not in list of candidate
        if candidate_name not in candidate_options:

            #then add them
            candidate_options.append(candidate_name)

            #initialize vote tallying
            candidate_votes[candidate_name] = 0
    
        #tally votes over each row iteration
        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:

    #name votes value
    votes = candidate_votes[candidate_name]

    #calculate percentages as float
    vote_percentage = float(votes) / float(total_votes) * 100

    #print candidate names and voting percentages in sentences. Round to nearest hundreth
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})")
    outfile1.write(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #update winner
    if votes > winning_count:
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
        winning_count = votes

winning_candidate_summary = (
    f"{bar}"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"{bar}")

print(winning_candidate_summary)
outfile1.write(winning_candidate_summary)

election_results.close