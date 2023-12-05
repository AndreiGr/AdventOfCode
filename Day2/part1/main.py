import os
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = os.path.join(FILE_PATH, "../data/input.txt")

RED = 12
GREEN = 13
BLUE = 14

def processTurn(turn):
    cubes = turn.split(", ")
    for cube in cubes:
        cube = cube.split(" ")
        if cube[1]=="red" and int(cube[0])> RED:
            return False
        elif cube[1]=="green" and int(cube[0])> GREEN:
            return False
        elif cube[1]=="blue" and int(cube[0])> BLUE:
            return False
    return True

def processLine(line):
    id = int(line[0])
    for turn in line[1].split("; "):
        if(not processTurn(turn.strip())):
            return 0
    return id

def main():
    with open(INPUT_FILE_PATH,"r") as file:
        lines = file.readlines()
    total = 0
    for line in lines:
        line = line.replace("Game ","")
        total += processLine(line.split(": "))
    
    print(total)

if __name__ == '__main__':
    main()