import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument('--location', '-l',
    help='your location')
  
args = parser.parse_args()

print(args.location)
