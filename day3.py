from Models import Solution
from regex import *

class Day3(Solution):
    do:Pattern
    dont:Pattern
    mul:Pattern
    all:list[Pattern]
    
    def ordered_matches(self,exprs:list[str],text:str)->list[Match]:
        all_matches=[]
        for expr in exprs:
            for match in finditer(expr,text):
                all_matches.append((match.start(),match)) 
        all_matches.sort()
        return [match[1] for match in all_matches]

    def __init__(self):
        super().__init__(day=3)
        self.do=compile("do\(\)")
        self.dont=compile("don't")
        self.mul=compile("mul\((\d+),(\d+)\)")
        self.all=[self.do,self.dont,self.mul]
        
    def part1(self):
        
        sum=0
        for line in self.input():
            # for match in findall(self.mul,line):
            for match in self.ordered_matches([self.mul],line):
                groups=match.groups()
                sum+=int(groups[0])*int(groups[1])
        return sum

    def part2(self):
        sum=0
        enable=True
        
        if(self.args.s):
            input=self.input(1)
        else:
            input=self.input()    
        for line in input:
            for match in self.ordered_matches(self.all,line):
                if match.re==self.do:
                    enable=True
                elif match.re==self.dont:
                    enable=False
                elif match.re==self.mul:
                    if enable:
                        groups=match.groups()
                        sum+=int(groups[0])*int(groups[1])
        return sum

if __name__ == '__main__':
    day=Day3()
    day.printResults()
