#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
#You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: 
# "Voter ID", "County", and "Candidate". 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
#The total number of votes cast
#A complete list of candidates who received votes
# #The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

# Import modules and libraries
import os
import csv
import collections

# Create csv path to resource file
csvpath = r'\Users\Louie\uci\Python-Challenge\PyPoll\Resources\election_data.csv'

total_votes = 0


#1

sumkhan = 0
d=[]
# Opening and reading the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
    #print(f'CSV Header: {csv_header}')
    print ("Election Results")
    print ("--------------------------------------------")

    #total_votes = 0
    #candidates = []
    #percentage_votes = 0
    #total_num_votes = 0
    #votes = {}

    #for row in csvreader:
        #total_votes += 1

        #if row[2] not in candidates:
            #candidates.append(row[2])
            #index = candidate.inder
    result = {}
    for line in csvreader:
        candidate = line[2]
        total_votes += 1
        if candidate in result:
            result[candidate]['vote_count'] += 1
        else:
            result[candidate] = {'vote_count': 1}
    winner = list(result.keys())[0]
    output = []

# Displaying information 
    for candidate in result:
        result[candidate]['percentage_vote'] = (result[candidate]['vote_count']/ total_votes) * 100
        result[candidate]['candidate'] = candidate
        if result[winner]['vote_count'] < result[candidate]['vote_count']:
            winner = candidate
        output.append(result[candidate])    

# Exporting info to .txt file           
with open('output.txt', 'w') as output_file:
    print('Total Votes: ', total_votes)
    output_file.write('Total Votes: {} \n'.format(total_votes))
    print('-------------------------')
    output_file.write('------------------------- \n')
    for candidate in sorted(output, key= lambda x: x['vote_count'], reverse=True):     
        print('{}: {}% ({})'.format(candidate['candidate'], round(candidate['percentage_vote'], 3), candidate['vote_count']))
        output_file.write('{}: {}% ({}) \n'.format(candidate['candidate'], round(candidate['percentage_vote'], 3), candidate['vote_count']))
    print('-------------------------')
    output_file.write('------------------------- \n')
    print('Winner: ',winner)
    output_file.write('Winner: {}'.format(winner))