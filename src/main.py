from .player import *
from .getsite import *
from .position import *
from .table import MakeTable
from .year import year
import sys

def main():
    scrape()
    position()

    if len(sys.argv) > 1:
        if sys.argv[1] == 'print':
            MakeTable(sys.argv[2])
        else:
            year(sys.argv[1]) 
    else:
        print('no input')
    

