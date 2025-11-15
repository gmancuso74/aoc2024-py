from Models import Solution
from typing import Any
from enum import Enum

class Map2D:
    #map[(row,col),'something']
    map:dict[tuple:Any]
    #minRange[dimensionIdx,minValue]
    minIdx:dict[int,int]
    maxIdx:dict[int,int]
    def __init__(self):
        self.minIdx={0:0,1:0}
        self.maxIdx={0:0,1:0}
        self.map=dict()
        
    def load(self,input:list[str]):
        result=dict()
        r=0
        for line in input:
            c=0
            for char in line:
                result[(r,c)]=char
                if(c>self.maxIdx[1]):
                    self.maxIdx[1]=c
                c=c+1
            if r>self.maxIdx[0]:
                self.maxIdx[0]=r
            r=r+1
        self.map=result

    def valid(self,coords:tuple)->bool:
        return (coords[0]>=self.minIdx[0] and coords[0]<=self.maxIdx[0] and coords[1]>=self.minIdx[1] and coords[1]<=self.maxIdx[1])
    
    def iterate(self,apply,context):
        """Takes a function(map,coord,context) as argument, apply function to each coordinate in the map, using context to store results as necdessary"""
        for rowIdx in range(self.minIdx[0],self.maxIdx[0]+1):
            for colIdx in range(self.minIdx[1],self.maxIdx[1]+1):
                apply(self,(rowIdx,colIdx),context)

    def plot(self):
        header='   '
        for idx in range(self.minIdx[1],self.maxIdx[1]+1):
            header+=str(idx)[-1]
        print(header)
        for rowIdx in range(self.minIdx[0],self.maxIdx[0]+1):
            row=f'{rowIdx:2}:'
            for colIdx in range(self.minIdx[1],self.maxIdx[1]+1):
                row=row+self.map[(rowIdx,colIdx)]
            print(row)

class Direction(Enum):
    N=(-1,0)
    S=(1,0)
    E=(0,1)
    W=(0,-1)
    NE=(-1,1)
    SE=(1,1)
    NW=(-1,-1)
    SW=(1,-1)

    def __init__(self,r,c):
        self.r=r
        self.c=c

def from_dir(map2d:Map2D,coord:tuple,direction:Direction,target_len:int)->str:
    map=map2d.map
    result=""
    if(not map2d.valid(coord)): return result
    for idx in range(target_len):
        end_idx=(coord[0]+(target_len-1)*direction.r,coord[1]+(target_len-1)*direction.c)
        if(map2d.valid(end_idx)):
            result+=map[(coord[0]+idx*direction.r,coord[1]+idx*direction.c)]
    return result

def search(map2d:Map2D,coord:tuple,context):
    map=map2d.map
    cha=map[coord]
    if(cha=='X'):
        count=0
        for dir in Direction:
            result=from_dir(map2d,coord,dir,len('XMAS'))
            if result=='XMAS':
                # print(f'{coord}:{dir}')
                count=count+1
        if(count>0):
            context.append(count)

def search2(map2d:Map2D,coord:tuple,context):
    map=map2d.map
    cha=map[coord]
    if(cha=='A'):
        count=0
        tl=(coord[0]+Direction.NW.r,coord[1]+Direction.NW.c)
        tr=(coord[0]+Direction.NE.r,coord[1]+Direction.NE.c)
        tl_str=from_dir(map2d,tl,Direction.SE,3)
        tr_str=from_dir(map2d,tr,Direction.SW,3)
        if (tl_str=="SAM" or tl_str=="MAS") and (tr_str=="SAM" or tr_str=="MAS"):
            count=count+1
        if(count>0):
            context.append(count)
        
class Day4(Solution):
    map:Map2D
    def __init__(self):
        super().__init__(day=4)
        map=Map2D()
        map.load(self.input())
        self.map=map
    
    def part1(self):
        # self.map.plot()
        context=list()
        self.map.iterate(search,context)
        return sum(context)

    def part2(self):
        context=list()
        self.map.iterate(search2,context)
        return sum(context)

if __name__ == '__main__':
    day=Day4()
    day.printResults()
