import json
from .player import players

def makeJson():
    playerData = [{"Name": u.name, "First Year": u.frstYear, "Last Year": u.lstYear, "Role": u.catagory, "Position":u.pos, "Rookie Card":u.rc} for u in players]

    with open("data.json", "w") as f:
        json.dump(playerData, f, indent=2)