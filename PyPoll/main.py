import os
import csv


csvpath = os.path.join('Resources','election_data.csv')
candidates=set() # Define a set() to get distinct candidate names
candidates_votes=[] # Define a list to hold candidates name who got the vote per voter
candidate_total_votes={} # Define a dictionary to hold the total votes for each candidate

#open the election_data.csv file
with open(csvpath, encoding='utf8') as electiondata:
    electionreader = csv.reader(electiondata, delimiter=',')
    csvheader=next(electionreader) # skip the title, store the header in a variable

    # get the distinct candidates and the candidates who got the vote per voter id
    for voterrow in electionreader:
        candidates_votes.append((voterrow[2])) # candidate per voter
        candidates.add(voterrow[2]) #distinct candidate names

# get the total votes for each candidate and put it a dictionary
for this_candidate in candidates:
    candidate_total_votes[this_candidate]=candidates_votes.count(this_candidate) # Total up the voted per candidate

# write the results into the analysis file and print it on the terminal as per the defined formatting
analysisoutput = os.path.join('analysis','ElectionResults.txt')
with open(analysisoutput,'w') as analysiswriter:
    analysiswriter.write("```text\n")
    print("```text")
    analysiswriter.write("Election Results\n")
    print("Election Results")
    analysiswriter.write("-------------------------\n")
    print("-------------------------")
    analysiswriter.write(f"Total Votes: {len(candidates_votes)}\n")
    print(f"Total Votes: {len(candidates_votes)}") 
    analysiswriter.write("-------------------------\n")
    print("-------------------------")
    for candidate, total_votes in sorted(candidate_total_votes.items()): # Sort alphabetically and show the total votes and percentage using the format func
        analysiswriter.write(f'{candidate}: {((total_votes*100)/len(candidates_votes)):.3f}% ({total_votes:.0f})\n')
        print(f'{candidate}: {((total_votes*100)/len(candidates_votes)):.3f}% ({total_votes:.0f})')
    analysiswriter.write("-------------------------\n")
    print("-------------------------")
    analysiswriter.write(f'Winner: {max(candidate_total_votes, key=lambda key:candidate_total_votes[key])}\n') #use the lambda or anonymous function to get the candidate with the maxumum votes
    print(f'Winner: {max(candidate_total_votes, key=lambda key:candidate_total_votes[key])}')
    analysiswriter.write("-------------------------\n")
    print("-------------------------")
    analysiswriter.write("```\n")
    print("```")