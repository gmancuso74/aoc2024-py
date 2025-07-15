from Models import Solution

class Day2(Solution):

    def __init__(self):
        super().__init__(day=2)

    def descending(self, input:list)->bool:
        return all(input[i] > input[i+1] for i in range(len(input) - 1))

    def ascending(self,input:list)->bool:
        return all(input[i] < input[i+1] for i in range(len(input) - 1))

    def big_diff(self,input:list)->int:
        return max([ abs(input[i+1]-input[i]) for i in range(len(input)-1)] )
                   
    def safe(self,input:list)->bool:
        return (self.descending(input) or self.ascending(input)) and self.big_diff(input)<=3

    def safe2(self,input:list)->bool:
        if(self.safe(input)) : return True
        for i in range(len(input)):
            new_list=list()
            for x in range(len(input)):
                if(x!=i): new_list.append(input[x]) 
            if self.safe(new_list) : return True
        return False

    def part1(self):
        result =0
        line_arr = [ [int(y) for y in x.split()] for x in [line for line in self.input()] ]
        for line in line_arr:
            res=self.safe(line)
            result += 1 if res else 0
        return result

    def part2(self):
        result =0
        line_arr = [ [int(y) for y in x.split()] for x in [line for line in self.input()] ]
        for line in line_arr:
            res=self.safe2(line)
            result += 1 if res else 0        
        return result

if __name__ == '__main__':
    day=Day2()
    day.printResults()
