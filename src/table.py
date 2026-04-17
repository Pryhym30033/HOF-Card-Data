import pandas as pd
from pathlib import Path
import json

def safeInt(val):
    try:
        return int(val)
    except (ValueError, TypeError):
        return 0

def MakeTable(year):
    
    win_user = input("Enter Computer UserName: ")
    folder = Path(f"/mnt/c/Users/{win_user}")

    while not folder.exists():
        win_user = input("Wrong username, retry: ")
        folder = Path(f"/mnt/c/Users/{win_user}")
    
    with open("data.json", "r") as f:
        playerData = json.load(f)

    if year == "all":
        df = pd.DataFrame(playerData)
        df.to_excel(f"/mnt/c/Users/{win_user}/Desktop/HOF.xlsx", index=False)

    elif year == 'negro':
        output = []
        for player in playerData:
            if player["Role"] == "Negro Leag.":
                output.append({
                    "Name" : player["Name"],
                    "Position":player["Position"],
                    "RC" : player["Rookie Card"]
                })
        output.sort(key=lambda x: x["Name"])
        df = pd.DataFrame(output)
        df.to_excel(f"/mnt/c/Users/{win_user}/Desktop/NegroHOF.xlsx", index=False)

    elif year == "old":
        output = []
        for player in playerData:
            if safeInt(player["Last Year"]) < 1920 and player["Role"] == 'Player':
                output.append({
                    "Name" : player["Name"],
                    "Position":player["Position"],
                    "RC" : player["Rookie Card"]
                })
        output.sort(key=lambda x: x["Name"])
        df = pd.DataFrame(output)
        df.to_excel(f"/mnt/c/Users/{win_user}/Desktop/oldHOF.xlsx", index=False)

    else:
        output = []
        for player in playerData:
            if player["Role"] == "Player":    
                if safeInt(player["First Year"]) <= safeInt(year) and safeInt(player["Last Year"]) >= safeInt(year):
                    output.append({
                    "Name" : player["Name"],
                    "Position":player["Position"],
                    "RC" : player["Rookie Card"]
                })  
        output.sort(key=lambda x: x["Name"])
        df = pd.DataFrame(output)
        df.to_excel(f"/mnt/c/Users/{win_user}/Desktop/{year}HOF.xlsx", index=False)