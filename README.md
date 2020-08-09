# Election-Analysis
Python project for tallying election results

### Background
This Python program is intended to facilitate vote tallying at scale. Excel is unfit for this job as the row count exceeds 360K. Our program tallies all votes by county and candidate, then determines the winner. Then printed into a text file, the Election-Analysis progam is easy to read, easy to use, and 100% reproduceable.

### Election-Audit Results
In running the program on Election_Results.csv as provided by the election commission, we've determined the following:
* A total of 369,711 votes were cast in the election.
* Denver county had the highest voter turnout by vote count.
* A breakdown of votes by county and percentage of vote by county is presented below:
<p align="center">
  <img width="800" height="300" src="https://github.com/DenverSherman/Election-Analysis/blob/master/resources/Voter_Breakdown.png">
</p>
<p align="center">
  <img width="650" height="300" src="https://github.com/DenverSherman/Election-Analysis/blob/master/resources/Total_Vote_Breakdown.png">
</p>

* A breakdown of votes and vote percentage won by each candidate is presented above.

* **Diana DeGette** is the winner of this election with **272,892 votes representing 74% of ballots cast.**

### Election-Audit Summary
The PyPoll_Challenge.py program is neither limited to the scope nor scale of this project. It is equipped to handle another dataset of the same form. Should the shape of the new dataset be different than Election_Results.csv, changes are required. Namely, the column indexing within the candidate_name and county_name requires update.
```
#specify candidate name column for row[x] where x = column number
candidate_name = row[2]

#specify county name column for row[x] where x = column number
county_name = row[1]
```
With this change in mind, PyPoll_Challenge.py is a malleable program that is ready for work in the field.
