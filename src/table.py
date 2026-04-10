from .player import players
import pandas as pd


def MakeTable():
    playerData = [{"Name": u.name, "Role": u.catagory, "First Year": u.frstYear, "Position":u.pos, "Rookie Card":u.rc} for u in players]
    df = pd.DataFrame(playerData)
    df.to_excel("/mnt/c/Users/Pryhym/Desktop/HOF.xlsx", index=False)
