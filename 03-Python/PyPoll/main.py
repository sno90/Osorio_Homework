# import modules
import os
import csv

# path to get polling data
polling_data_path = os.path.join('Resources',  'election_data.csv')

# set variables 
candidate_1 = 0
candidate_2 = 0
candidate_3 = 0
candidate_4 = 0
total_votes = 0


# open polling data file
with open(polling_data_path, newline='') as electionfile:
    csvreader = csv.reader(electionfile, delimiter =',')
    header = next(csvreader)

# create an empty list for the unique candidates
    unique_candidates = []

# for loop to go through the election data
    for row in csvreader:
        candidate_list = [row[2]]
# iteration through the candidates column and add the unique values to the unique candidates list
        for i in candidate_list:
            if i not in unique_candidates:
                unique_candidates.append(i)  
# calculate the number of total votes in the file
        if row[2] == unique_candidates[0]:
            candidate_1 += 1
        elif row[2] == unique_candidates[1]:
            candidate_2 += 1
        elif row[2] == unique_candidates[2]:
            candidate_3 += 1
        elif row[2] == unique_candidates[3]:
            candidate_4 += 1    
        else:
            print("candidate not listed please add to the number of candidates")
# dictionary of candidates
candidates = unique_candidates
# get total votes
total_votes = candidate_1 + candidate_2 + candidate_3 + candidate_4

# dictionary of votes
votes = [candidate_1, candidate_2, candidate_3, candidate_4]

# zip 
dict_candidates_votes = dict(zip(candidates, votes))

# max function will determine who got the most votes
key = max(dict_candidates_votes, key=dict_candidates_votes.get)

# calculate percentage for each candidate
can1_percentage = (candidate_1/total_votes) * 100
can2_percentage = (candidate_2/total_votes) * 100
can3_percentage = (candidate_3/total_votes) * 100
can4_percentage = (candidate_4/total_votes) * 100

# print summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"{unique_candidates[0]}: {can1_percentage:.3f}%  ({candidate_1})")
print(f"{unique_candidates[1]}: {can2_percentage:.3f}%  ({candidate_2})")
print(f"{unique_candidates[2]}: {can3_percentage:.3f}%  ({candidate_3})")
print(f"{unique_candidates[3]}: {can4_percentage:.3f}%  ({candidate_4})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

#Output files
output_file = os.path.join('Resources','election_results.csv')

with open(output_file, "w") as file:

#Write files
   file.write(f"Election Results")
   file.write("\n")
   file.write(f"----------------------------")
   file.write("\n")
   file.write(f"Total Votes: {total_votes}")
   file.write("\n")
   file.write(f"----------------------------")
   file.write("\n")
   file.write(f"{unique_candidates[0]}: {can1_percentage:.3f}%  ({candidate_1})")
   file.write("\n")
   file.write(f"----------------------------")
   file.write("\n")
   file.write(f"{unique_candidates[1]}: {can2_percentage:.3f}%  ({candidate_2})")
   file.write("\n")
   file.write(f"----------------------------")
   file.write("\n")
   file.write(f"{unique_candidates[2]}: {can3_percentage:.3f}%  ({candidate_3})")
   file.write("\n")
   file.write(f"----------------------------")
   file.write("\n")
   file.write(f"{unique_candidates[3]}: {can4_percentage:.3f}%  ({candidate_4})")
   file.write("\n")
   file.write(f"----------------------------")
   file.write("\n")
   file.write(f"Winner: {key}")
   file.write("\n")
   file.write(f"----------------------------")
   file.write("\n")