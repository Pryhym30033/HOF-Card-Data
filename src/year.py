import sys
import json

output = []

def year():
    
    with open("data.json", "r") as f:
        players = json.load(f)

    for player in players:
        if player["Role"] == 'Player':
            if player["First Year"] == "n/a" or player["Last Year"] == "n/a" or player["Last Year"] == "--":
                continue
            if int(sys.argv[1]) >= int(player["First Year"]) and int(sys.argv[1]) <= int(player["Last Year"]):
                output.append(f"{player["Name"]} - POSITION:{player["Position"]} - RC:{player["Rookie Card"]}")
    if output:
        output.sort()
        for line in output:
            print(line)
    else:
        print('No Match!!')