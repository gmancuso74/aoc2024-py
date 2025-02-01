import argparse
import os.path

parser = argparse.ArgumentParser(description='AOC solution template builder')
parser.add_argument('day', type=int , help='day number')
args = parser.parse_args()

filename=f'day{args.day}.py'
if(not os.path.isfile(filename)):
	with open('day.template') as template:
		with(open(filename,'w')) as newday:
			newday.write(template.read().replace('___DAY___',str(args.day)))
else:
	print(f'file {filename} already exists, skipping')