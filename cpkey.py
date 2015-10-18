from __future__ import print_function

class Colors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

print (Colors.BLUE + "Please, paste your api key:" + Colors.END)

user_input = raw_input("> ")

print(user_input)
