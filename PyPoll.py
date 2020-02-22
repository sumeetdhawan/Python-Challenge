# Imort the CSV and OS paths

import os
import csv

# Assign variables with descriptive names

Total_Votes = 0             #Total number of votes
Candidate_List = []         # List of Candidates
Candidates = []             # List of Unique Candidates
Candidate_Votes = []        # Number of votes to each candidate 
Candidate_Percentage = []   # Percentage of votes to each candidate

# Path to collect data from the resource folder

csvpath = os.path.join ('..', 'Resources', 'election_data.csv')


with open (csvpath, 'r') as csvfile:

 #Split the data on commas

    csvreader = csv.reader(csvfile, delimiter=',')
    #remove header
    header = next(csvreader)
    
    for row in csvreader:
        Total_Votes += 1 
        
        if row[2] not in Candidates:       
            Candidates.append(row[2])   #get the  uniques list of candidates
        
        Candidate_List.append(row[2])

    for Candidates1 in Candidates:   #Loop through each candidate in List of unique candidates
                          
        Candidate_Votes.append(Candidate_List.count(Candidates1))       # number of votes to each candidate
        #calculate percentage of each candidate

        Candidate_Percentage.append(round(Candidate_List.count(Candidates1)/Total_Votes*100, 2))  # percentage of votes to each candidate

    # find the winner with maximum number of votes
    winner = Candidates[Candidate_Votes.index(max(Candidate_Votes))]
    
#print all results
print('Election Results:')
print('-------------------------------')
print('Total Votes: ' + str(Total_Votes))   # Print the total number of votes
# print(Candidates)    # Print the names of the candidates
print('-------------------------------')
for i in range(len(Candidates)):
    print(f'{Candidates[i]}: {Candidate_Percentage[i]}% ({Candidate_Votes[i]})')
print('-------------------------------')
print(f'Winner: {winner}')
print('-------------------------------')

# Exporting the results to text file
result = open ("PyPollResult.txt", "w")
line1 = ("Election Results")
line2 = ('-------------------------------')
line3 = ('Total Votes: ' + str(Total_Votes))   # Print the total number of votes
line4 = ('-------------------------------')
result.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(Candidates)):
    line = (f'{Candidates[i]}: {Candidate_Percentage[i]}% ({Candidate_Votes[i]})')
    result.write('{}\n'.format(line))
line5 = ('-------------------------------')
line6 = (f'Winner: {winner}')
line7 = ('-------------------------------')
result.write('{}\n{}\n{}\n'.format(line5, line6, line7))


    

    