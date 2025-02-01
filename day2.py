from Models import Solution

class Day2(Solution):

    def __init__(self):
        super().__init__(day=2)

    def part1(self):
        for line in self.input():
            print(line)
        return 0


    def part2(self):
        return 0

if __name__ == '__main__':
    day=Day2()
    day.printResults()
