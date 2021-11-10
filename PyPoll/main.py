import os
import csv
election = os.path.join("Resources", "election_data.csv")
total_votes = 0

khan = 0
correy = 0
li = 0
otooley = 0

candidate_votes = {}
percent = []

with open(election) as election_file:
    csvreader = csv.reader(election_file, delimiter = ',')

    header = next(csvreader)

    for row in csvreader:

        total_votes += 1
        
        candidate = row[2]

        if candidate in candidate_votes.keys():
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

for candidate in candidate_votes.keys():
    if candidate == "Khan":
        khan = candidate_votes.get(candidate)
        percent.append("{:.3%}".format(khan/total_votes))
    elif candidate == "Correy":
        correy = candidate_votes.get(candidate)
        percent.append("{:.3%}".format(correy/total_votes))
    elif candidate == "Li":
        li = candidate_votes.get(candidate)
        percent.append("{:.3%}".format(li/total_votes))
    elif candidate == "O'Tooley":
        otooley = candidate_votes.get(candidate)
        percent.append("{:.3%}".format(otooley/total_votes))

winner = max(candidate_votes, key=candidate_votes.get)

election_result = ("Election Results\n"
                    "----------------------\n"
                    f"Total Votes: {total_votes}\n"
                    "----------------------\n"
                    f"Khan: {percent[0]} ({khan})\n"
                    f"Correy: {percent[1]} ({correy})\n"
                    f"Li: {percent[2]} ({li})\n"
                    f"O'Tooley: {percent[3]} ({otooley})\n"
                    "----------------------\n"
                    f"Winner: {winner}\n"
                    "----------------------")

print(election_result)

output_path = os.path.join("Text File","Poll.txt")

with open(output_path, "w") as txtfile:
    txtfile.write(election_result)