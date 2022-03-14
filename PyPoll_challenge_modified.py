# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os
from email import header

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
countyname_highturnout = ""
largest_county_vote=0
largest_county_percentage=0


# Read the csv and convert it into a list of dictionaries
#creating opening  the data variable
election_data=open(file_to_load,"r")

#crearing data reader variable
file_reader = csv.reader(election_data)

#read the header row
headers = next(file_reader)

#print headers
print(headers)

# For each row in the CSV file.
for row in file_reader:

   # Add to the total vote count
    total_votes += 1

    # Get the candidate name from each row.
    candidate_name = row[2]

    # Extract the county name from each row
    county_name = row[1]

    # If the candidate does not match any existing candidate add it to
        # the candidate list
    if candidate_name not in candidate_options:

       # Add the candidate name to the candidate list.
       candidate_options.append(candidate_name)

       # And begin tracking that candidate's voter count.
       candidate_votes[candidate_name] = 0

    # Add a vote to that candidate's count
    candidate_votes[candidate_name] += 1

    
        # 4a: Write an if statement that checks that the
    # county does not match any existing county in the county list.
    if county_name not in county_list:


        #4b: add the existing county  to the list of counties
       county_list.append(county_name)

        # 4c: Begin tracking the county's vote count.
       county_votes[county_name]=0


    # 5: Add a vote to that county's vote count
    county_votes[county_name] +=1


# Save the results to our text file.   
txt_file=open(file_to_save,"w")
election_results =(
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n\n"
        f"County_voutes\n")

print(election_results, end="")

# Save the final vote count to the text file.
txt_file.write(election_results)

# 6a: Write a for loop to get the county from the county dictionary.
for county_name in county_votes:
    # 6b: Retrieve the county vote count.
    votes_c=county_votes[county_name]
        
    # 6c: Calculate the percentage of votes for the county.
    county_percentage = round(float(votes_c) / float(total_votes) * 100,3)

    # 6d: Print the county results to the terminal.
    county_result=(
        f"{county_name}: {county_percentage:.1f}% ({votes_c:,})\n")
    print(county_result)
    # 6e: Save the county votes to a text file.
    txt_file.write(county_result)


    # 6f: Write an if statement to determine the winning county and get its vote count.
    if (votes_c>largest_county_vote) and (county_percentage>largest_county_percentage):
        #  If true then set winning_county_vote = votes_c and winning_county_percentage =
         # county_percentage.
        largest_county_vote=votes_c
        largest_county_percentage=county_percentage
        # And, set the winning_county equal to the county's name
        countyname_highturnout = county_name
        
# 7: Print the county with the largest turnout to the terminal.
largest_countyvote_summary = (
    f"-------------------------\n"
    f"County Name with largest turnout: {countyname_highturnout}\n"
    f"Largest county Vote Count: {largest_county_vote:,}\n"
    f"largest Percentage: {largest_county_percentage:.1f}%\n"
    f"-------------------------\n")
print(largest_countyvote_summary)

# 8: Save the county with the largest turnout to a text file.
txt_file.write(largest_countyvote_summary)

# Save the final candidate vote count to the text file.
for candidate_name in candidate_votes:

    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = round(float(votes) / float(total_votes) * 100,2)

    #  Print the candidate name and percentage of votes.
    candidate_result=(
        f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #print candidate result
    print(candidate_result)

    #save the candidate result to our text file
    txt_file.write(candidate_result)
    
    # Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

# Print the winning candidate (to terminal)
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Save the winning candidate's name to the text file
txt_file.write(winning_candidate_summary)


election_data.close()
