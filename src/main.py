from player import *
from getsite import *
from position import *
from table import MakeTable
from year import year
import sys

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'print':
            MakeTable()
            return
        else:
            year()
            return
    
    else:
        return
    
    
    

    
if __name__ == "__main__":
    scrape()
    position()
    main()
    
