import sys
import json

output = []

def safeInt(val):
    try:
        return int(val)
    except (ValueError, TypeError):
        return 0

def year(year):

    with open("data.json", "r") as f:
            players = json.load(f)

    if year == 'negro':
        for player in players:
            if player["Role"] == "Negro Leag.":
                output.append(f"{player["Name"]} - POSITION:{player["Position"]} - RC:{player["Rookie Card"]}")

    elif  year == 'old':
            for player in players:
                if safeInt(player["Last Year"]) < 1920 and player["Role"] == 'Player':
                    output.append(f"{player["Name"]} - POSITION:{player["Position"]} - RC:{player["Rookie Card"]}")

    else: 
        for player in players:
            if player["Role"] == 'Player':
                if player["First Year"] == "n/a" or player["Last Year"] == "n/a" or player["Last Year"] == "--":
                    continue
                if int(year) >= int(player["First Year"]) and int(year) <= int(player["Last Year"]):
                    output.append(f"{player["Name"]} - POSITION:{player["Position"]} - RC:{player["Rookie Card"]}")
    if output:
        output.sort()
        for line in output:
            print(line)
    else:
        print('No Match!!')