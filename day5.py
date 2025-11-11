from Models import Solution

class Validator:
    
    rules:dict[int,list[int]]  #rules[10] -> list of numbers that must be after 10
    
    def __init__(self):
        self.rules=dict()
        
    def add_rule(self,line:str):
        a,b=map(int,line.split('|'))
        if a in self.rules:
            self.rules[a].append(b)
        else:
            self.rules[a]=[b]
    
    def min_index(self,ordering:list[int],valueList:list[int]):
        result=None
        for value in valueList:
            if value in ordering:
                idx=ordering.index(value)
                if result is None or idx<result:
                    result=idx
        return result

    def swap(self,ordering:list[int],idx_a:int,idx_b:int):
        a=ordering[idx_a]
        b=ordering[idx_b]
        ordering[idx_a]=b
        ordering[idx_b]=a
        
    def valid(self,ordering:list[int],rule:tuple)->bool:
        (key,valueList)=rule
        if key in ordering:
            min_idx=self.min_index(ordering,valueList)
            if min_idx is not None: return ordering.index(key)<min_idx
            return True #no values from valueList were in ordering, so this rule doesn't apply
        else:
            return True
    
    def fix(self,ordering:list[int],rule:tuple):
        (key,valueList)=rule
        if key in ordering:
            key_idx=ordering.index(key)
            min_idx=self.min_index(ordering,valueList)
            if min_idx is not None and key_idx>min_idx: 
                self.swap(ordering,min_idx,key_idx)
        
    def mid_idx(self,ordering:list[int]):
        return len(ordering)//2
    
    class Result:
        valid:bool
        value:int
        
        def __init__(self,valid,value):
            self.valid=valid
            self.value=value
        
    def validate(self,line:str)->Result:
        ordering=[int(x) for x in line.split(',')]
        uncorrected=True
        while any ([not self.valid(ordering,rule) for rule in self.rules.items()]):
            uncorrected=False
            fix_list=[item for item in self.rules.items() if not self.valid(ordering,item)]
            for item in fix_list:
                self.fix(ordering,item)
        mid=ordering[self.mid_idx(ordering)]
        return self.Result(uncorrected,mid)
    
class Day5(Solution):

    def __init__(self):
        super().__init__(day=5)
        self._part2=0

    def part1(self):
        sum=0
        sum2=0
        val=Validator()
        ruleEntry=True
        for line in self.input():
            if(len(line)==0):
                ruleEntry=False
                continue
            if(ruleEntry):
                val.add_rule(line)
            else:
                result=val.validate(line)
                if(result.valid):
                    sum+=result.value
                else:
                    sum2+=result.value
        self._part2=sum2
        return sum

    def part2(self):
        return self._part2

if __name__ == '__main__':
    day=Day5()
    day.printResults()
