# This scrpit creates apikey.py file and copies your api key to this file. 

# add some basic colors

from __future__ import print_function

class Colors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

print "Please, paste your api key file"

user_input = raw_input("> ")

print user_input
