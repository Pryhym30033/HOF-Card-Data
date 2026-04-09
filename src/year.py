import sys
from player import players



year = sys.argv[1]

output = []

def year():
    for player in players:
        if player.catagory == 'Player'or'Negro Leag.':
            if player.frstYear[:3] == sys.argv[1][:3]:
                output.append(f"{player.name}-{player.frstYear}-{player.pos}-{player.rc}")

    if output:
        for line in output:
            print(line)
    else:
        print('No Match!!')