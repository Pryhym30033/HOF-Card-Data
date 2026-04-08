from player import *
from getsite import *
from position import *

def main():
    for player in players:
        print(player.name)

if __name__ == "__main__":
    scrape()
    position()
