import os
import csv

election_data_file = os.path.join("Resources","election_data.csv")
election_results_file = os.path.join('Output',"election_results.txt")

election_report = {
    "report": "",
    "total_votes": 0,
    "candidates": [],
    "winner": ""
}

with open(election_data_file, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader)

    candidates = []

    for row in csv_reader:

        candidate_name = row[2]

        #create list of candidates who received votes

        if not (candidate_name in candidates):
            candidates.append(candidate_name)

    #create dictionaries for the candidates

    [election_report["candidates"].append({"name":candidate,"vote_count":0, "vote_pct": 0}) for candidate in candidates]
    

with open(election_data_file, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader)

    for row in csv_reader:

        candidate_name = row[2]        
        county = row[1]
        voter_id = row[0]

        #get total number of votes cast

        election_report["total_votes"] += 1

        #tally vote

        for candidate in election_report["candidates"]:
            if (candidate_name == candidate["name"]):
                candidate["vote_count"] += 1
                
#determine total votes per candidate

for candidate in election_report["candidates"]:
    total_votes = election_report["total_votes"]
    candidate_votes = candidate["vote_count"]

    #rounding to a whole number because there is never a fraction of a person voting 

    candidate["vote_pct"] = round(((candidate_votes / total_votes) * 100),0)

#determine winner

    winner = {"vote_count":0}

    for candidate in election_report["candidates"]:
        for other_candidate in election_report["candidates"]:

            if (candidate is other_candidate):
                continue

            elif ((candidate["vote_count"] > other_candidate["vote_count"]) & candidate["vote_count"] > winner["vote_count"]):
                winner = candidate

    election_report["winner"] = winner

#determine total votes

total_votes = election_report["total_votes"]

#create report string

report = f"\nElection Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n"

for candidate in election_report["candidates"]:
    report += f"{candidate['name']} {candidate['vote_pct']}% ({candidate['vote_count']})\n"

report += f"-------------------------\nWinner: {election_report['winner']['name']}\n-------------------------"

#output report to console/terminal

election_report["report"] = report

print(report)

#output report to file

er = open(election_results_file,"w")
er.write(election_report["report"])
er.close()


