from player import *
from getsite import *
from position import *

def main():
    for player in players:
        if player.catagory == "Player":
            print(f"{player.name} {player.pos} {player.frstYear} {player.rc} ")
if __name__ == "__main__":
    scrape()
    position()
    main()
