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
            MakeTable()
        else:
            year() 
    else:
        print('no input')
    

