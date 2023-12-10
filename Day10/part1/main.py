import os
import pandas
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = os.path.join(FILE_PATH, "../data/input.txt")
TEST_FILE_PATH = os.path.join(FILE_PATH, "../data/test.txt")

class Pipe:
    def __init__(self, position, type):
        self.type = type
        if type == "-":
            self.end1 = (position[0],position[1]-1)
            self.end2 = (position[0],position[1]+1)
        elif type == "|":
            self.end1 = (position[0]-1,position[1])
            self.end2 = (position[0]+1,position[1])
        elif type == "L":
            self.end1 = (position[0]-1,position[1])
            self.end2 = (position[0],position[1]+1)
        elif type == "F":
            self.end1 = (position[0]+1,position[1])
            self.end2 = (position[0],position[1]+1)
        elif type == "7":
            self.end1 = (position[0]+1,position[1])
            self.end2 = (position[0],position[1]-1)
        elif type == "J":
            self.end1 = (position[0]-1,position[1])
            self.end2 = (position[0],position[1]-1)
        elif type == "S":
            self.end1 = position
            self.end2 = position
        else:
            self.end1 = (-2,-2)
            self.end2 = (-2,-2)

    def __str__(self):
        return self.type
        
    __repr__ = __str__

    def canenter(self, position):
        if position == self.end1:
            return self.end1
        elif position == self.end2:
            return self.end2
        else:
            return False
        
    def gothrough(self, start):
        if start == self.end1:
            return self.end2
        elif start == self.end2:
            return self.end1
        else:
            return False


up = []
down = []
left = []
right = []

def processpath(start,direction,maze):
    position = (-1,-1)

    match direction:
        case "up":
            if start[0] > 0:
                next = maze.loc[start[0]-1][start[1]]
                if next.canenter(start) != False:
                    position = (start[0]-1,start[1])
                else:
                    return
                path = up
                path.append(start)
            else:
                return
        case "down":
            if start[0] < len(maze)-1:
                next = maze.loc[start[0]+1][start[1]]
                if next.canenter(start) != False:
                    position = (start[0]+1,start[1])
                else:
                    return
                path = down
                path.append(start)
            else:
                return
        case "left":
            if start[1] > 0:
                next = maze.loc[start[0]][start[1]-1]
                if next.canenter(start) != False:
                    position = (start[0],start[1]-1)
                else:
                    return
                path = left
                path.append(start)
            else:
                return
        case "right":
            if start[1]<len(maze.loc[0])-1:
                next = maze.loc[start[0]][start[1]+1]
                if next.canenter(start) != False:
                    position = (start[0],start[1]+1)
                else:
                    return
                path = right
                path.append(start)
            else:
                return

    path.append(position)
    lstart = (start[0],start[1])
    while True:
        nextposition = next.gothrough(lstart)
        next = maze.loc[nextposition[0]][nextposition[1]]
        if next.type == "S":
            return
        if next.canenter(position) != False:
            lstart = position
            position = nextposition
            path.append(position)
        else:
            path.clear()
            return



        



def main():
    # with open(TEST_FILE_PATH,"r") as file:
    with open(INPUT_FILE_PATH,"r") as file:
        lines = []
        i=0
        start = (0,0)
        for line in file:
            j=0
            row = []
            for el in list(line.strip()):
                row.append(Pipe((i,j),el))
                if el == "S":
                    start = (i,j)
                j += 1
            lines.append(row)
            i += 1
        maze = pandas.DataFrame(lines)

    processpath(start,"up",maze)
    processpath(start,"down",maze)
    processpath(start,"left",maze)
    processpath(start,"right",maze)
    
    print(len(up)/2)
    print(len(down)/2)
    print(len(left)/2)
    print(len(right)/2)
    print("Done")


if __name__ == '__main__':
    main()