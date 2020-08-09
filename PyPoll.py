# In this project, we will read election data to determine:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote.

# csv module
import csv
import os
dir(csv)

# assigning variable to file path
load1 = os.path.join("resources", "election_results.csv")
save1 = os.path.join("analysis", "election_analysis.txt")
with open(load1,"r") as election_results:
    #Read, Analyze
    file_reader = csv.reader(election_results)
    # Print header row
    headers = next(file_reader)
    print(headers)


    
election_results.close
