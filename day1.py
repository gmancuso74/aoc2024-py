from Models import Solution

class Day1(Solution):

    def __init__(self):
        super().__init__(day=1)

    def part1(self):
        left=list()
        right=list()
        sum=0
        for line in self.input():
            (a,b)=[int(x) for x in line.split()]
            left.append(a)
            right.append(b)
        left.sort()
        right.sort()
        for i in range(len(left)):
            sum += abs((right[i]-left[i]))
        return sum


    def part2(self):
        left=list()
        right=list()
        for line in self.input():
            (a,b)=[int(x) for x in line.split()]
            left.append(a)
            right.append(b)
        sum=0
        for num in left:
            val  = len( [i for i in right if i==num ])
            sum += num*val
        return sum

if __name__ == '__main__':
    day=Day1()
    day.printResults()
