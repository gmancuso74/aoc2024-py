import argparse
from aocd.models import Puzzle, AocdError
import os

class Solution(object):
	useShort: bool
	printInput: bool
	args:object
	parser:argparse.ArgumentParser
 
	def set_token(self):
		if 'AOC_SESSION' not in os.environ.keys():
			with open('token','r') as file:
				token=file.read()
				os.environ["AOC_SESSION"]=token.strip()

	def __init__(self,day):
		self.day=day
		self.useShort=False
		self.printInput=False
		self.result1=None
		self.result2=None
		self.set_token()
		# print(f'Token: {os.environ["AOC_SESSION"]}')
		self.puzzle=Puzzle(year=2024, day=self.day)
		self.parser=argparse.ArgumentParser(description='AOC 2024')
		self.parser.add_argument('-s', action='store_true', help='use the small input file')
		self.parser.add_argument('-p', action='store_true', help='print the input')
		self.parser.add_argument('-w', action='store_true', help='Write input file to data/')
		self.args,unknown = self.parser.parse_known_args()
		if(self.args.s): self.useShort=True
		if(self.args.p): self.printInput=True
		if(self.args.w):
			filename=f'data/day{self.day}'
			if not self.args.s:
				with open(filename,'w') as datafile:
					datafile.write(self.puzzle.input_data)
			else:
				i=0
				for example in self.puzzle.examples:
					exampleFile=f'{filename}.small'
					if i>0:exampleFile=f'{exampleFile}.{i}'
					with open(exampleFile,'w') as datafile:
						datafile.write(example.input_data)
					i=i+1

	def input(self,idx=0):
		if self.useShort:
			return self.puzzle.examples[idx].input_data.split('\n')
		else:
			try:
				return self.puzzle.input_data.split('\n')
			except AocdError as e:
				print(f'error retreiving solution input; have you refreshed your token?')
				print('~/.config/aocd/token')
				raise
				
	def printResults(self):
		if(self.printInput):
			for line in self.input(): print(line)
		self.result1=str(self.part1()) # type: ignore
		self.result2=str(self.part2()) # type: ignore
		print(f'Day {self.day}:\t{self.result1}\t{self.result2}')

